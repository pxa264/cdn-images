# 商品图片目录

## 说明

商品图片按商品 ID 组织，每个商品一个目录。

推荐结构：

```text
products/
└── {product_id}/
    ├── main.jpg
    ├── thumb.jpg
    └── carousel/
        ├── 1.jpg
        ├── 2.jpg
        └── 3.jpg
```

## 文件说明

- `main.jpg`: 商品主图
- `thumb.jpg`: 商品缩略图
- `carousel/*.jpg`: 商品详情轮播图

## 图片规范

- 主图尺寸：`800x800px`
- 缩略图尺寸：`300x300px`
- 轮播图建议尺寸：`1200px` 宽或同一比例
- 格式：`JPG` 或 `WebP`
- 单张大小：建议控制在 `1MB` 以内

## CDN 访问格式

```text
https://cdn.jsdelivr.net/gh/pxa264/cdn-images@main/products/{product_id}/main.jpg
https://cdn.jsdelivr.net/gh/pxa264/cdn-images@main/products/{product_id}/thumb.jpg
https://cdn.jsdelivr.net/gh/pxa264/cdn-images@main/products/{product_id}/carousel/{index}.jpg
```

## 示例

```text
products/
├── 1/
│   ├── main.jpg
│   ├── thumb.jpg
│   └── carousel/
│       ├── 1.jpg
│       └── 2.jpg
└── 2/
    ├── main.jpg
    ├── thumb.jpg
    └── carousel/
        ├── 1.jpg
        ├── 2.jpg
        └── 3.jpg
```
