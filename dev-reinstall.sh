#!/bin/bash

# 清理操作
python setup.py clean --all

# 檢查 dist 目錄是否存在，如果存在則刪除
if [ -d "./dist" ]; then
    rm -r ./dist
fi

# 尋找當前目錄及子目錄下所有的 __pycache__ 目錄並刪除
find . -name "__pycache__" -type d -exec rm -r {} +

# 卸載現有的 Django app
pip uninstall -y django-simple-third-party-jwt-dev-dashboard

# 創建分發檔案
python setup.py sdist

# 尋找創建的分發檔案的完整路徑
packagePath=$(find ./dist -name "*-*.tar.gz" | head -n 1)

# 檢查是否找到檔案
if [ -z "$packagePath" ]; then
    echo "未找到分發檔案。"
    exit 1
fi

# 安裝找到的分發檔案
python -m pip install "$packagePath"
