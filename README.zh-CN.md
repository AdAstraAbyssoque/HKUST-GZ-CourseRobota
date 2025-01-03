# HKUST-GZ 课程抓取器

这是一个用于抓取港科大(广州)课程信息的 Python 爬虫工具。

[English](README.md)

## 功能特性

- 自动抓取指定学期的所有课程信息
- 支持提取课程代码、名称、描述、学分等基本信息
- 获取课程时间、地点、教师、配额等详细信息
- 数据自动保存至 SQLite 数据库

## 环境要求

- Python 3.6+
- requests
- beautifulsoup4
- tqdm
- sqlite3

## 安装说明

1. 克隆仓库：

```bash
git clone https://github.com/AdAstraAbyssoque/HKUST-GZ-CourseRobota.git
```

2. 安装依赖：

```bash
pip install -r requirements.txt
```

## 使用方法

1. 运行爬虫：

```bash
python robot.py
```

2. 默认抓取当前学期课程，如需指定学期，修改代码中的`termnumber`参数：

```python
scraper = CourseScraper(termnumber=2340)  # 2340表示2023-24学年第4学期
```

## 数据存储

- 所有课程数据将保存在`courses_[termnumber].db`数据库文件中
- 使用 SQLite 数据库，可以方便地查询和导出数据

## 注意事项

- 请合理控制爬取频率，避免对目标服务器造成压力
- 抓取的数据仅供参考，具体选课信息请以官方系统为准
