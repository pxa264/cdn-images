#!/usr/bin/env python3
"""生成占位图片"""
from PIL import Image, ImageDraw, ImageFont
import os

# 创建输出目录
os.makedirs("products/1", exist_ok=True)
os.makedirs("products/2", exist_ok=True)
os.makedirs("products/3", exist_ok=True)
os.makedirs("products/4", exist_ok=True)
os.makedirs("products/5", exist_ok=True)
os.makedirs("products/6", exist_ok=True)
os.makedirs("products/7", exist_ok=True)
os.makedirs("products/8", exist_ok=True)
os.makedirs("products/1/carousel", exist_ok=True)
os.makedirs("products/2/carousel", exist_ok=True)
os.makedirs("products/3/carousel", exist_ok=True)
os.makedirs("products/4/carousel", exist_ok=True)
os.makedirs("products/5/carousel", exist_ok=True)
os.makedirs("products/6/carousel", exist_ok=True)
os.makedirs("products/7/carousel", exist_ok=True)
os.makedirs("products/8/carousel", exist_ok=True)
os.makedirs("avatars", exist_ok=True)
os.makedirs("categories", exist_ok=True)
os.makedirs("banners", exist_ok=True)

# 商品数据
products = [
    {"id": 1, "name": "智能手表 Pro", "color": "#3B82F6"},
    {"id": 2, "name": "无线蓝牙耳机", "color": "#10B981"},
    {"id": 3, "name": "便携式充电宝", "color": "#F59E0B"},
    {"id": 4, "name": "智能家居音箱", "color": "#8B5CF6"},
    {"id": 5, "name": "4K超高清显示器", "color": "#EC4899"},
    {"id": 6, "name": "机械键盘 RGB", "color": "#6366F1"},
    {"id": 7, "name": "人体工学鼠标", "color": "#14B8A6"},
    {"id": 8, "name": "高清网络摄像头", "color": "#F97316"},
]

def create_placeholder(text, size, color, filename, subtitle=""):
    """创建占位图片"""
    img = Image.new('RGB', size, color)
    draw = ImageDraw.Draw(img)

    try:
        font_large = ImageFont.truetype("/System/Library/Fonts/PingFang.ttc", 48)
        font_small = ImageFont.truetype("/System/Library/Fonts/PingFang.ttc", 24)
    except:
        font_large = ImageFont.load_default()
        font_small = ImageFont.load_default()

    # 绘制文本
    text_bbox = draw.textbbox((0, 0), text, font=font_large)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]

    x = (size[0] - text_width) // 2
    y = (size[1] - text_height) // 2

    draw.text((x, y), text, fill="white", font=font_large)

    if subtitle:
        subtitle_bbox = draw.textbbox((0, 0), subtitle, font=font_small)
        subtitle_width = subtitle_bbox[2] - subtitle_bbox[0]
        subtitle_x = (size[0] - subtitle_width) // 2
        draw.text((subtitle_x, y + 60), subtitle, fill="rgba(255,255,255,0.7)", font=font_small)

    img.save(filename)
    print(f"✅ Created: {filename}")

# 为每个商品创建图片
for product in products:
    pid = product["id"]
    name = product["name"]
    color = product["color"]

    # 主图 (800x800)
    create_placeholder(name, (800, 800), color, f"products/{pid}/main.jpg", f"Product ID: {pid}")

    # 缩略图 (300x300)
    create_placeholder(name, (300, 300), color, f"products/{pid}/thumb.jpg", "缩略图")

    # 轮播图
    carousel_count = 3 if pid in [1, 4, 5] else 2
    for i in range(1, carousel_count + 1):
        create_placeholder(f"{name}", (800, 800), color, f"products/{pid}/carousel/{i}.jpg", f"轮播图 {i}")

# 创建默认头像
create_placeholder("默认头像", (200, 200), "#9CA3AF", "avatars/default.jpg", "Default Avatar")

# 创建一些示例分类图片
categories = [
    {"name": "数码家电", "color": "#3B82F6"},
    {"name": "时尚美妆", "color": "#EC4899"},
    {"name": "家居百货", "color": "#10B981"},
]

for i, cat in enumerate(categories, 1):
    filename = f"categories/{cat['name']}.jpg".replace(" ", "-")
    create_placeholder(cat["name"], (400, 300), cat["color"], filename, f"Category {i}")

# 创建示例banner
create_placeholder("首页轮播 Banner 1", (1200, 400), "#6366F1", "banners/home-banner-1.jpg", "Promotion")
create_placeholder("首页轮播 Banner 2", (1200, 400), "#8B5CF6", "banners/home-banner-2.jpg", "New Arrival")

print("\n✅ 所有占位图片已创建完成！")
