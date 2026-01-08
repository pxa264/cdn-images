# 商品图片目录

## 使用说明

每个商品目录应包含以下文件：

```
{product_id}/
├── main.jpg          # 主图 (800x800px)
├── thumb.jpg         # 缩略图 (300x300px)
└── carousel/         # 轮播图目录
    ├── 1.jpg        # 轮播图1 (800x800px)
    ├── 2.jpg        # 轮播图2 (800x800px)
    └── 3.jpg        # 轮播图3 (800x800px)
```

## 当前商品

| ID | 商品名称 | 状态 | 轮播图数量 |
|----|----------|------|------------|
| 1 | 智能手表 Pro | ✅ 已配置 | 3 |
| 2 | 无线蓝牙耳机 | ✅ 已配置 | 2 |
| 3 | 便携式充电宝 | ✅ 已配置 | 2 |
| 4 | 智能家居音箱 | ✅ 已配置 | 3 |
| 5 | 4K超高清显示器 | ✅ 已配置 | 2 |
| 6 | 机械键盘 RGB | ✅ 已配置 | 2 |
| 7 | 人体工学鼠标 | ✅ 已配置 | 1 |
| 8 | 高清网络摄像头 | ✅ 已配置 | 2 |

## 添加新商品

1. 创建目录：`mkdir -p {product_id}/carousel`
2. 添加图片文件
3. 更新此README

## CDN访问格式

```
https://cdn.jsdelivr.net/gh/pxa264/cdn-images@main/products/{product_id}/main.jpg
https://cdn.jsdelivr.net/gh/pxa264/cdn-images@main/products/{product_id}/thumb.jpg
https://cdn.jsdelivr.net/gh/pxa264/cdn-images@main/products/{product_id}/carousel/{n}.jpg
```
