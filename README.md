# HKUST-GZ Course Scraper

A Python web scraper for extracting course information from HKUST-GZ.

[简体中文](README.zh-CN.md)

## Features

- Automatically scrape course information for specified terms
- Extract course codes, names, descriptions, and credits
- Collect course schedules, locations, instructors, and quotas
- Save data to SQLite database

## Requirements

- Python 3.6+
- requests
- beautifulsoup4
- tqdm
- sqlite3

## Installation

1. Clone the repository:

```bash
git clone https://github.com/AdAstraAbyssoque/HKUST-GZ-CourseRobota.git
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

1. Run the scraper:

```bash
python robot.py
```

2. By default, it scrapes the current term. To specify a different term, modify the `termnumber` parameter:

```python
scraper = CourseScraper(termnumber=2340)  # 2340 represents Term 4 of 2023-24
```

## Data Storage

- All course data is saved in `courses_[termnumber].db` database file
- Uses SQLite database for easy querying and data export

## Notes

- Please control scraping frequency to avoid server overload
- Data is for reference only, please refer to the official system for enrollment
