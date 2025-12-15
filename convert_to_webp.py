#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
图片格式转换脚本：将PNG/JPG转换为WebP格式
优化网站图片加载性能
"""

from PIL import Image
import os
from pathlib import Path

def convert_to_webp(input_path, output_path=None, quality=85):
    """
    将图片转换为WebP格式

    Args:
        input_path: 输入图片路径
        output_path: 输出图片路径（可选，默认替换扩展名）
        quality: WebP质量（0-100，默认85）
    """
    try:
        # 打开图片
        img = Image.open(input_path)

        # 如果是RGBA模式，转换为RGB（WebP不支持透明度的某些情况）
        if img.mode == 'RGBA':
            # 创建白色背景
            background = Image.new('RGB', img.size, (255, 255, 255))
            background.paste(img, mask=img.split()[3])  # 使用alpha通道作为mask
            img = background
        elif img.mode != 'RGB':
            img = img.convert('RGB')

        # 确定输出路径
        if output_path is None:
            output_path = str(Path(input_path).with_suffix('.webp'))

        # 保存为WebP
        img.save(output_path, 'WEBP', quality=quality, method=6)

        # 获取文件大小
        original_size = os.path.getsize(input_path)
        webp_size = os.path.getsize(output_path)
        reduction = (1 - webp_size / original_size) * 100

        print(f"[OK] {Path(input_path).name} -> {Path(output_path).name}")
        print(f"   Original: {original_size / 1024:.1f}KB")
        print(f"   WebP: {webp_size / 1024:.1f}KB")
        print(f"   Reduced: {reduction:.1f}%\n")

        return True
    except Exception as e:
        print(f"[ERROR] Failed to convert {input_path}: {e}")
        return False

def main():
    """主函数：批量转换images文件夹中的图片"""
    images_dir = Path(__file__).parent / 'images'

    if not images_dir.exists():
        print(f"[ERROR] Images folder not found: {images_dir}")
        return

    print("Starting image conversion to WebP format...\n")

    # 支持的图片格式
    supported_formats = ['.png', '.jpg', '.jpeg']

    # 统计信息
    total_converted = 0
    total_original_size = 0
    total_webp_size = 0

    # 遍历images文件夹
    for img_file in images_dir.iterdir():
        if img_file.suffix.lower() in supported_formats:
            original_size = os.path.getsize(img_file)

            # 转换图片
            webp_path = img_file.with_suffix('.webp')
            if convert_to_webp(str(img_file), str(webp_path), quality=85):
                total_converted += 1
                total_original_size += original_size
                total_webp_size += os.path.getsize(webp_path)

    # 输出总结
    if total_converted > 0:
        total_reduction = (1 - total_webp_size / total_original_size) * 100
        print("=" * 50)
        print(f"[SUCCESS] Conversion completed!")
        print(f"   Files converted: {total_converted}")
        print(f"   Original total size: {total_original_size / 1024:.1f}KB")
        print(f"   WebP total size: {total_webp_size / 1024:.1f}KB")
        print(f"   Total reduction: {total_reduction:.1f}%")
        print("=" * 50)
    else:
        print("[WARNING] No images found to convert")

if __name__ == '__main__':
    main()
