# Log Analysis Tool

A simple command-line tool that analyses application log files and produces clear summaries for troubleshooting and reporting.

## Why this exists

Manual log review is slow and error-prone, especially during incidents.
This tool automates log analysis by extracting log levels, safely handling malformed entries, and producing human-readable or machine-readable summaries.

## Features

- Parses structured log files line by line
- Safely ignores malformed log entries
- Counts log levels (ERROR, WARNING, INFO)
- Optional filtering by log level
- Outputs results to the terminal or a CSV file
- Clean, modular Python codebase

## How to run

From the project directory:

python3 logtool.py

Filter by log level:

python3 logtool.py --level ERROR

Write results to a CSV file:

python3 logtool.py --output report.csv

## Example output

Log level counts:
ERROR : 2
WARNING : 1
INFO : 1

## Project structure

log_analyser/
├── logtool.py      # CLI entry point
├── parser.py       # Log file parsing and validation
├── analyser.py     # Data aggregation logic
├── reporter.py     # Output formatting and file writing
├── sample_logs/
│   └── example.log
└── README.md

## What I learned

- Building command-line tools with argparse
- Parsing and validating real-world text data
- Defensive programming and error handling
- Separating concerns into reusable modules
- Refactoring working code safely

## Future improvements

- JSON output support
- Time-window analysis for incidents
- Automated scheduling (cron)
- Unit tests
- Support for additional log formats


------------------------------------
------------------------------------

# 日志分析工具（Log Analysis Tool）

这是一个命令行日志分析工具，用于分析应用程序日志文件，并生成清晰的错误和事件摘要，方便故障排查和报告。

## 项目背景（为什么做这个）

在实际工作中，人工查看日志既耗时又容易出错，尤其是在系统故障或事件处理中。
本工具通过自动化方式分析日志文件，提取日志级别，安全地处理格式错误的日志，并生成清晰的统计结果。

## 功能特点

- 逐行解析结构化日志文件
- 安全地忽略格式不正确的日志行
- 统计日志级别（ERROR、WARNING、INFO）
- 支持按日志级别筛选结果
- 支持在终端输出结果或导出为 CSV 文件
- 代码结构清晰，采用模块化设计

## 使用方法

在项目目录中运行：

python3 logtool.py

按日志级别筛选（例如只查看 ERROR）：

python3 logtool.py --level ERROR

将结果输出为 CSV 文件：

python3 logtool.py --output report.csv

## 示例输出

Log level counts:
ERROR : 2
WARNING : 1
INFO : 1

## 项目结构

log_analyser/
├── logtool.py      # 命令行入口文件
├── parser.py       # 日志解析与校验逻辑
├── analyser.py     # 日志数据统计分析
├── reporter.py    # 输出格式与文件写入
├── sample_logs/
│   └── example.log
└── README.md

## 学习收获

- 使用 argparse 构建命令行工具
- 解析和处理真实世界中的文本日志数据
- 防御式编程与错误处理
- 按职责拆分代码，实现模块化设计
- 在不破坏功能的情况下重构代码

## 后续改进方向

- 支持 JSON 格式输出
- 基于时间窗口的日志事件分析
- 定时任务自动执行（cron）
- 添加单元测试
- 支持更多日志格式
