@echo off
chcp 65001 >nul
echo ========================================
echo   桌面小猫 - 一键打包脚本
echo ========================================
echo.

echo [1/4] 检查Python环境...
python --version
if errorlevel 1 (
    echo 错误: 未找到Python，请先安装Python 3.8+
    pause
    exit /b 1
)
echo Python环境正常
echo.

echo [2/5] 下载图片素材...
python download_assets.py
echo.

echo [3/5] 安装依赖包...
pip install -r requirements.txt
if errorlevel 1 (
    echo 警告: 依赖安装可能不完整，请检查网络
)
echo.

echo [4/5] 处理图片资源（去除背景）...
python process_images.py
echo.

echo [5/5] 开始打包EXE...
pyinstaller desktop_pet.spec --clean
echo.

echo ========================================
echo   打包完成！
echo   生成的EXE位于: dist\DesktopCat.exe
echo ========================================
pause
