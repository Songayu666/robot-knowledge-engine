# Robot Knowledge Engine（机器人知识引擎）

[English](README.md) | [简体中文](README.zh_CN.md)

[![License](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)

一个面向机器人手册、工程文档和源代码的可溯源、版本感知知识引擎。

项目以智元灵犀 X1 作为首个案例，目标是构建能够保留文档出处、产品版本、精确工程标识及资料冲突的技术问答系统。底层设计不绑定单一厂商，后续可以扩展为通用机器人研发知识平台。

## 为什么做这个项目

机器人研发问题经常同时涉及产品手册、BOM 表格、装配图、配置文件和源代码。可靠的技术助手既要理解自然语言，也要准确识别型号、参数、错误码和接口名称，还要区分硬件与固件版本，并为每项结论提供可以核验的证据。

计划采用以下检索方式：

- 向量语义检索；
- 针对型号、参数和错误码的精确关键词检索；
- 产品、硬件版本、固件版本和文档日期过滤；
- BOM、图纸、手册和代码之间的实体关系；
- 检索重排、引用验证及资料冲突检测。

## 当前进度

仓库目前已经包含：

- FastAPI 服务及健康检查、资料源查询接口；
- 带版本信息的资料源与文档元数据模型；
- 第一批智元灵犀 X1 官方资料源配置；
- 不公开本地文件名的资料统计工具；
- PostgreSQL、pgvector 和 Redis 容器配置；
- 自动化测试、代码检查、架构说明、开发路线及数据政策。

## 环境要求

- Ubuntu 22.04 或兼容 Linux 系统；
- Docker Engine 与 Docker Compose；
- `uv`；
- Python 3.12（由 `uv` 自动管理）。

## 快速开始

进入项目并安装依赖：

```bash
cd /home/zhongde/agibot_ws/robot-knowledge-engine
cp -n .env.example .env
uv sync --extra dev
```

启动 PostgreSQL 与 Redis。当前用户尚未重新登录时，可以使用 `sudo`：

```bash
sudo docker compose up -d
sudo docker compose ps
```

启动 API：

```bash
uv run uvicorn robot_knowledge_engine.api.main:app \
  --host 127.0.0.1 \
  --port 8000 \
  --reload
```

浏览器打开 <http://127.0.0.1:8000/docs>，或者在另一个终端验证：

```bash
curl http://127.0.0.1:8000/health
curl http://127.0.0.1:8000/api/v1/sources
```

## 质量检查

```bash
uv run ruff check .
uv run ruff format --check .
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 uv run pytest
```

## 本地 X1 资料

本机资料目录为：

```text
/home/zhongde/agibot_ws/智元灵犀X1_20250307
```

统计本地资料：

```bash
uv run python scripts/inventory_local_sources.py \
  /home/zhongde/agibot_ws/智元灵犀X1_20250307
```

大型文件、工程图纸、官网手册、工具软件和其他可能受再分发限制的资料不会提交到公开仓库。它们通过 `.env` 指向本地目录：

```dotenv
RKE_LOCAL_X1_ROOT=/home/zhongde/agibot_ws/智元灵犀X1_20250307
```

## 开发路线

1. 建立带页码、章节、产品版本和来源信息的文档解析流程。
2. 将 PDF、HTML、Markdown 和 Excel 内容写入 PostgreSQL。
3. 使用 pgvector、关键词查询和元数据过滤实现混合检索。
4. 接入重排模型和大语言模型，生成带原文引用的答案。
5. 增加版本冲突检测、证据不足拒答和标准问题评测。
6. 扩展图纸、BOM、代码、图像和视频之间的知识关系。

详细规划见[架构说明](docs/ARCHITECTURE.md)、[开发路线](docs/ROADMAP.md)和[数据政策](docs/DATA_POLICY.md)。

## 许可证

项目源代码使用 Apache License 2.0。第三方文档和数据仍遵循各自原始许可证及权利声明。
