import requests
from bs4 import BeautifulSoup
import sqlite3
import re
import json
from tqdm import tqdm

class CourseScraper:
    def __init__(self, termnumber=2430):
        self.termnumber = termnumber
        self.base_url = f"https://w5.hkust-gz.edu.cn/wcq/cgi-bin/{self.termnumber}/subject/"
        self.headers = {"User-Agent": "Mozilla/5.0"}

    def remove_tag(self, soup):
        """移除不需要的HTML标签"""
        for script in soup(["script", "style", "meta", "link"]):
            script.extract()
        return soup

    def extract_departments(self, soup):
        """提取部门列表"""
        depts_div = soup.find("div", class_="depts")
        if not depts_div:
            return []
        subjects = [a.get_text(strip=True) for a in depts_div.find_all("a")]
        return subjects

    def init_db(self):
        """初始化数据库"""
        conn = sqlite3.connect(f"courses_{self.termnumber}.db")
        conn.execute("""CREATE TABLE IF NOT EXISTS courses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            courseTitle TEXT,
            courseCode TEXT,
            courseName TEXT,
            courseDescription TEXT,
            credit INTEGER,
            section TEXT,
            date TEXT,
            room TEXT,
            instructors TEXT,
            quota TEXT,
            enrol TEXT,
            avail TEXT,
            wait TEXT,
            remarks TEXT
        )""")
        return conn

    def extract_course_details(self, course_div):
        """提取单个课程的详细信息"""
        title_tag = course_div.find("h2")
        title_text = title_tag.get_text(strip=True) if title_tag else ""
        credit = 0
        credit_match = re.search(r'\((\d+)\s*units?\)', title_text, re.IGNORECASE)
        if credit_match:
            credit = int(credit_match.group(1))
            title_text = re.sub(r'\(\d+\s*units?\)', '', title_text).strip()

        if " - " in title_text:
            course_code, rest = title_text.split(" - ", 1)
            course_name = rest.rsplit("(", 1)[0].strip()
        else:
            course_code = ""
            course_name = title_text

        course_info_div = course_div.find("div", class_="courseattr")
        course_description = ""
        if course_info_div:
            description = course_info_div.find("th", string="DESCRIPTION")
            if description:
                course_description = description.find_next_sibling("td").get_text(strip=True)

        return title_text, course_code, course_name, course_description, credit

    def extract_sessions(self, courses_div, conn, title_text, course_code, course_name, course_description, credit):
        """提取课程的会话信息并存入数据库"""
        all_courses = []
        for course_div in courses_div.find_all("div", class_="course"):
            title_text, course_code, course_name, course_description, credit = self.extract_course_details(course_div)
            sessions_table = course_div.find("table", class_="sections")
            sessions = []
            if sessions_table:
                rows = sessions_table.find_all("tr", class_=["newsect", "secteven", "sectodd"])
                i = 0
                while i < len(rows):
                    row = rows[i]
                    tds = row.find_all("td")
                    if not tds:
                        i += 1
                        continue
                    section_code = tds[0].get_text(strip=True)
                    row_span = tds[0].get("rowspan")
                    span_length = int(row_span) if row_span else 1

                    remarks_td = tds[8] if len(tds) > 8 else ""
                    remarks = remarks_td.get_text(strip=True) if remarks_td else ""

                    if len(tds) >= 8:
                        date_text = tds[1].get_text(strip=True)
                        room_text = tds[2].get_text(strip=True)
                        instructor_text = tds[3].get_text(";", strip=True)
                        stored_quota = tds[4].get_text(strip=True)
                        stored_enrol = tds[5].get_text(strip=True)
                        stored_avail = tds[6].get_text(strip=True)
                        stored_wait = tds[7].get_text(strip=True)

                        sessions.append({
                            "section": section_code,
                            "dates": [date_text],
                            "rooms": [room_text],
                            "instructors": [instructor_text],
                            "quota": stored_quota,
                            "enrol": stored_enrol,
                            "avail": stored_avail,
                            "wait": stored_wait,
                            "remarks": remarks
                        })

                    for r_idx in range(1, span_length):
                        next_row = rows[i + r_idx]
                        next_tds = next_row.find_all("td")
                        if len(next_tds) >= 3:
                            date_text = next_tds[0].get_text(strip=True)
                            room_text = next_tds[1].get_text(strip=True)
                            instructor_text = next_tds[2].get_text(";", strip=True)
                            remarks_td = next_tds[8] if len(next_tds) > 8 else ""
                            remarks = remarks_td.get_text(strip=True) if remarks_td else ""
                            if sessions:
                                sessions[-1]["dates"].append(date_text)
                                sessions[-1]["rooms"].append(room_text)
                                sessions[-1]["instructors"].append(instructor_text)
                                sessions[-1]["remarks"] = remarks
                    i += span_length

                    for session in sessions:
                        date_text = ";".join(sorted(set(session["dates"])))
                        room_text = ";".join(sorted(set(session["rooms"])))
                        instructor_text = ";".join(sorted(set(session["instructors"])))
                        conn.execute("""INSERT INTO courses 
                            (courseTitle, courseCode, courseName, courseDescription, credit, section, date, room, instructors, quota, enrol, avail, wait, remarks)
                            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
                            (title_text, course_code, course_name, course_description, credit, section_code,
                             date_text, room_text, instructor_text,
                             session["quota"], session["enrol"], session["avail"], session["wait"], session["remarks"]))

            all_courses.append({
                "courseTitle": title_text,
                "courseCode": course_code,
                "courseName": course_name,
                "courseDescription": course_description,
                "sessions": sessions
            })
        return all_courses

    def extract_courses_json(self, soup):
        """提取所有课程并存入数据库"""
        with self.init_db() as conn:
            all_courses = []
            courses_div = soup.find("div", id="classes")
            if not courses_div:
                print(json.dumps(all_courses, ensure_ascii=False))
                return

            all_courses = self.extract_sessions(courses_div, conn, "", "", "", "", 0)
            conn.commit()

    def run(self):
        """执行抓取流程"""
        request = requests.get(self.base_url + "DSAA", headers=self.headers)
        cleaned = self.remove_tag(BeautifulSoup(request.text, "html.parser"))
        subjects = self.extract_departments(cleaned)

        for subject in tqdm(subjects):
            request = requests.get(self.base_url + subject, headers=self.headers)
            cleaned = self.remove_tag(BeautifulSoup(request.text, "html.parser"))
            self.extract_courses_json(cleaned)

if __name__ == "__main__":
    scraper = CourseScraper()
    scraper.run()
