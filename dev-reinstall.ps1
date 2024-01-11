# 清理操作
python setup.py clean --all

# 檢查 dist 目錄是否存在
if (Test-Path "./dist") {
    # 如果存在，則刪除 dist 目錄
    Remove-Item "./dist" -Recurse
}

# 尋找當前目錄及子目錄下所有的 __pycache__ 文件夾
$pycacheDirectories = Get-ChildItem -Path . -Recurse -Directory -Filter "__pycache__"

# 遍歷並刪除每一個找到的 __pycache__ 文件夾
foreach ($dir in $pycacheDirectories) {
    Remove-Item $dir.FullName -Recurse -Force
}

# 卸載現有的 Django app
pip uninstall -y django-simple-third-party-jwt-dev-dashboard

# 創建分發檔案
python setup.py sdist

# 尋找創建的分發檔案的完整路徑
$packagePath = Get-ChildItem ./dist/ -Filter "*-*.tar.gz" | Select-Object -First 1

# 檢查是否找到檔案
if ($packagePath -eq $null) {
    Write-Error "未找到分發檔案。"
    Exit
}

# 安裝找到的分發檔案
python -m pip install $packagePath.FullName