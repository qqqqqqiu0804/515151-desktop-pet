# 桌面小猫 (Desktop Cat)

基于 PyQt5 开发的 Windows 桌面宠物程序，支持透明背景、自由行走、鼠标拖拽、系统托盘等功能。

## ✨ 功能特性

- **始终置顶**：宠物窗口始终显示在所有窗口最前端
- **自由行走**：小猫在桌面上随机左右行走，自动边界反弹
- **待机呼吸**：停止行走时有轻微呼吸动画效果
- **鼠标拖拽**：按住左键可自由拖动宠物到任意位置
- **双击跳跃**：双击宠物触发跳跃动作
- **系统托盘**：右下角托盘图标，右键菜单控制
- **多种形象**：内置站立、坐姿、趴卧三种形象切换
- **右键菜单**：宠物身上右键快速操作

## 📁 项目结构

```
desktop-pet/
├── main.py              # 主程序入口
├── process_images.py    # 图片背景去除脚本
├── requirements.txt     # Python依赖列表
├── desktop_pet.spec     # PyInstaller打包配置
├── build.bat            # 一键打包脚本（Windows）
├── README.md            # 使用说明
└── assets/              # 资源目录
    ├── cat_stand.jpg    # 站立形象（原图）
    ├── cat_sit.jpg      # 坐姿形象（原图）
    ├── cat_lie.jpg      # 趴卧形象（原图）
    ├── cat_stand.png    # 处理后透明背景图（自动生成）
    ├── cat_sit.png
    ├── cat_lie.png
    └── tray_icon.ico    # 托盘图标（自动生成）
```

## 🚀 快速开始

### 方式一：直接运行Python源码

1. **安装依赖**
```bash
pip install -r requirements.txt
```

2. **处理图片（去除背景）**
```bash
python process_images.py
```

3. **运行程序**
```bash
python main.py
```

### 方式二：打包成EXE可执行文件

双击运行 `build.bat` 即可一键打包，生成的 `DesktopCat.exe` 位于 `dist/` 目录下。

或手动执行：
```bash
pip install -r requirements.txt
python process_images.py
pyinstaller desktop_pet.spec --clean
```

打包完成后，`dist\DesktopCat.exe` 即为可直接运行的单文件程序，无需安装Python环境。

## 🎮 操作说明

### 鼠标交互
| 操作 | 效果 |
|------|------|
| 左键按住拖动 | 移动宠物位置 |
| 双击左键 | 触发跳跃动作 |
| 右键点击宠物 | 弹出快捷菜单 |

### 系统托盘
右键点击任务栏右下角的小猫图标：
- **显示/隐藏宠物**：切换宠物可见性
- **开始/停止行走**：控制是否自动走动
- **让它跳一下**：手动触发跳跃
- **切换形象**：在站立/坐姿/趴卧之间切换
- **退出**：关闭程序

### 双击托盘图标
快速显示或隐藏宠物。

## 🎨 自定义形象

### 替换默认图片
1. 将你的小猫照片放入 `assets/` 目录
2. 分别命名为 `cat_stand.jpg`、`cat_sit.jpg`、`cat_lie.jpg`
3. 运行 `python process_images.py` 自动去除背景
4. 重新运行程序或重新打包

### 调整背景去除阈值
编辑 `process_images.py` 中的 `threshold` 参数：
- 数值越大（如240）：只去除纯白色背景，保留更多细节
- 数值越小（如200）：去除更多浅色区域，可能误伤主体

根据你的图片背景亮度调整，默认230。

## ⚙️ 技术参数

### 行走参数（main.py 中可调）
- `walk_speed = 2`：移动速度（像素/帧）
- `walk_timer.start(50)`：刷新间隔（毫秒），越小越快
- 随机转向概率：1%/帧

### 跳跃参数
- 初速度：-12
- 重力加速度：0.8
- 刷新间隔：20ms

### 窗口尺寸
- 默认：120 × 140 像素
- 修改 `self.pet_size = QSize(120, 140)` 调整大小

## 🔧 环境要求

- **操作系统**：Windows 7 / 10 / 11
- **Python版本**：3.8 ~ 3.11（推荐3.9）
- **运行内存**：约 50MB

## 📝 常见问题

**Q: 宠物背景不透明，有白色方块？**
A: 运行 `python process_images.py` 生成透明背景PNG。如果效果不佳，调整阈值参数。

**Q: 打包后EXE文件很大？**
A: PyQt5打包后约 50-80MB，属于正常范围。可使用 UPX 压缩进一步减小体积。

**Q: 宠物不显示/闪退？**
A: 确保 `assets/` 目录下有图片文件，且图片格式正确。可通过命令行运行查看错误信息。

**Q: 如何开机自启动？**
A: 将 `DesktopCat.exe` 的快捷方式放入 `shell:startup` 目录（Win+R 输入即可打开）。

## 📄 许可证

仅供学习和个人使用。
