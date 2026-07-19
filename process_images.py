"""
图片预处理脚本 - 将小猫照片背景去除，生成透明背景PNG
运行方式: 
  python process_images.py          # 使用基础算法（纯色背景）
  python process_images.py --ai     # 使用AI抠图（效果最好，需安装rembg）
"""
import os
import sys
from PIL import Image, ImageFilter


def remove_background_simple(input_path, output_path, threshold=200):
    """
    基础背景去除：基于亮度阈值，适合浅色纯色背景
    """
    img = Image.open(input_path).convert('RGBA')
    data = img.getdata()

    new_data = []
    for r, g, b, a in data:
        # 计算亮度
        brightness = (r + g + b) / 3
        # 计算饱和度（排除灰色/白色背景中的彩色主体）
        max_c = max(r, g, b)
        min_c = min(r, g, b)
        saturation = (max_c - min_c) / max_c if max_c > 0 else 0

        # 背景判断：高亮度 + 低饱和度
        if brightness > threshold and saturation < 0.2:
            # 边缘渐变过渡
            edge_factor = (brightness - threshold) / 30
            alpha = max(0, int(255 * (1 - min(1, edge_factor))))
            new_data.append((r, g, b, alpha))
        else:
            new_data.append((r, g, b, 255))

    img.putdata(new_data)
    
    # 轻微模糊alpha通道，消除锯齿
    alpha = img.split()[-1]
    alpha = alpha.filter(ImageFilter.GaussianBlur(radius=1))
    img.putalpha(alpha)
    
    img.save(output_path, 'PNG')
    print(f'处理完成: {output_path}')


def remove_background_ai(input_path, output_path):
    """
    AI智能抠图（使用rembg），效果最好，适合复杂背景
    """
    try:
        from rembg import remove
    except ImportError:
        print('错误: 未安装rembg，请先运行: pip install rembg')
        print('或使用基础模式: python process_images.py')
        sys.exit(1)

    print(f'AI抠图中: {os.path.basename(input_path)} ...')
    input_img = Image.open(input_path)
    output_img = remove(input_img)
    output_img.save(output_path, 'PNG')
    print(f'处理完成: {output_path}')


def crop_to_content(image_path, padding=10):
    """裁剪图片到内容区域（去除多余透明边距）"""
    img = Image.open(image_path)
    bbox = img.getbbox()
    if bbox:
        # 增加一点边距
        left = max(0, bbox[0] - padding)
        top = max(0, bbox[1] - padding)
        right = min(img.width, bbox[2] + padding)
        bottom = min(img.height, bbox[3] + padding)
        cropped = img.crop((left, top, right, bottom))
        cropped.save(image_path)
        print(f'已裁剪: {image_path} ({cropped.width}x{cropped.height})')


def main():
    assets_dir = os.path.join(os.path.dirname(__file__), 'assets')
    
    use_ai = '--ai' in sys.argv

    images = [
        ('cat_stand.jpg', 'cat_stand.png'),
        ('cat_sit.jpg', 'cat_sit.png'),
        ('cat_lie.jpg', 'cat_lie.png'),
    ]

    mode = 'AI智能抠图' if use_ai else '基础亮度抠图'
    print(f'开始处理图片背景（{mode}）...')
    print('-' * 40)

    for src_name, dst_name in images:
        src = os.path.join(assets_dir, src_name)
        dst = os.path.join(assets_dir, dst_name)
        
        if os.path.exists(src):
            if use_ai:
                remove_background_ai(src, dst)
            else:
                remove_background_simple(src, dst, threshold=200)
            crop_to_content(dst)
        else:
            print(f'跳过（文件不存在）: {src}')
        print()

    # 生成托盘图标
    icon_src = os.path.join(assets_dir, 'cat_stand.png')
    icon_dst = os.path.join(assets_dir, 'tray_icon.ico')
    if os.path.exists(icon_src):
        img = Image.open(icon_src)
        # 调整为正方形
        size = max(img.width, img.height)
        square = Image.new('RGBA', (size, size), (0, 0, 0, 0))
        square.paste(img, ((size - img.width) // 2, (size - img.height) // 2))
        square = square.resize((32, 32), Image.LANCZOS)
        square.save(icon_dst, format='ICO', sizes=[(32, 32), (16, 16)])
        print(f'托盘图标已生成: {icon_dst}')

    print('-' * 40)
    print('全部处理完成！')
    if not use_ai:
        print('\n💡 提示: 如果抠图效果不理想，可尝试AI抠图:')
        print('   pip install rembg')
        print('   python process_images.py --ai')


if __name__ == '__main__':
    main()
