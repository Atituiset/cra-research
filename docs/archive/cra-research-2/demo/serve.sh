#!/usr/bin/env bash
# 启动 Jupyter 打开 CRA 演示笔记本
set -euo pipefail
cd "$(dirname "$0")/.."
exec .venv/bin/jupyter lab demo/cra_lifecycle_demo.ipynb "$@"
