<div align="center">

# HKUST-GZ 课程抓取器 📚

[![Python版本](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![许可证](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![欢迎PR](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/AdAstraAbyssoque/HKUST-GZ-CourseRobota/pulls)

🤖 港科大（广州）课程信息自动抓取工具

[English](README.md) | [简体中文](#)

</div>

## ✨ 功能特性

- 🔄 **自动抓取**: 自动获取指定学期的所有课程信息
- 📋 **丰富数据**: 提取全面的课程详情，包括：
  - 课程代码和名称
  - 课程描述和学分
  - 课程时间和地点
  - 授课教师信息
  - 课程配额和选课状态
- 💾 **数据存储**: 使用 SQLite 数据库高效存储，方便访问

## 🚀 快速开始

### 环境要求

开始之前，请确保：

- Python 3.6 或更高版本
- pip 包管理器

### 安装步骤

1. 克隆仓库：

```bash
git clone https://github.com/AdAstraAbyssoque/HKUST-GZ-CourseRobota.git
cd HKUST-GZ-CourseRobota
```

2. 安装依赖：

```bash
pip install -r requirements.txt
```

## 📖 使用说明

### 基本用法

直接运行：

```bash
python robot.py
```

### 高级配置

指定不同学期：

```python
scraper = CourseScraper(termnumber=2340)  # 2340表示2023-24学年第4学期
```

## 💡 数据结构

所有课程数据存储在 SQLite 数据库中，结构如下：

```sql
courses_[termnumber].db
└── courses表
    ├── courseTitle（课程标题）
    ├── courseCode（课程代码）
    ├── courseName（课程名称）
    ├── courseDescription（课程描述）
    └── ...（其他字段）
```

## ⚠️ 注意事项

- 🕒 请合理控制抓取频率
- 📝 数据仅供参考
- 🔄 可能需要定期更新

## 🤝 贡献

欢迎各种形式的贡献：

- 报告问题
- 提出新功能建议
- 提交代码改进

## 📜 许可证

本项目采用 MIT 许可证 - 详见 [LICENSE](LICENSE) 文件

## 📞 联系方式

如有任何问题，欢迎[提交 issue](https://github.com/AdAstraAbyssoque/HKUST-GZ-CourseRobota/issues)

## 许可证

本项目采用 Commons Clause + Apache 2.0 组合许可证。个人用途免费，商用需授权。
