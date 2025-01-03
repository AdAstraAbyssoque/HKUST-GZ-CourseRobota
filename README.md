<div align="center">

# HKUST-GZ Course Robota 📚

[![Python Version](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/AdAstraAbyssoque/HKUST-GZ-CourseRobota/pulls)

🤖 A powerful course information scraper for HKUST-GZ

[简体中文](README.zh-CN.md) | [English](#)

</div>

## ✨ Features

- 🔄 **Auto Scraping**: Automatically fetch course information for any term
- 📋 **Rich Data**: Extract comprehensive course details including:
  - Course codes and names
  - Course descriptions and credits
  - Class schedules and locations
  - Instructor information
  - Quota and enrollment status
- 💾 **Data Storage**: Efficiently store data in SQLite database for easy access

## 🚀 Quick Start

### Prerequisites

Before you begin, ensure you have:

- Python 3.6 or higher
- pip package manager

### Installation

1. Clone the repository:

```bash
git clone https://github.com/AdAstraAbyssoque/HKUST-GZ-CourseRobota.git
cd HKUST-GZ-CourseRobota
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

> For lower version python, please run `pip install request`.

## 📖 Usage

### Basic Usage

Simply run:

```bash
python robot.py
```

### Advanced Configuration

Specify a different term:

```python
scraper = CourseScraper(termnumber=2340)  # 2340 represents Term 4 of 2023-24
```

## 💡 Data Structure

All course data is stored in SQLite database with the following structure:

```sql
courses_[termnumber].db
└── courses table
    ├── courseTitle
    ├── courseCode
    ├── courseName
    ├── courseDescription
    └── ... (other fields)
```

## ⚠️ Notes

- 🕒 Please use reasonable scraping intervals
- 📝 Data is for reference only
- 🔄 Regular updates may be needed

## 🤝 Contributing

Contributions are welcome! Feel free to:

- Report bugs
- Suggest new features
- Submit pull requests

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Contact

If you have any questions, feel free to [open an issue](https://github.com/AdAstraAbyssoque/HKUST-GZ-CourseRobota/issues).
