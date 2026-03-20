# 商品图片目录

## 说明

当前商品图片默认直接存放在 `products/` 根目录。

AI Mall 后台上传服务不会按商品 ID 创建子目录，而是自动生成唯一文件名并直接上传到：

```text
products/{timestamp}-{random}.{ext}
```

当前命名格式：

```text
YYYYMMDD-HHmmss-随机6位.扩展名
```

示例：

```text
products/20260213-113149-bb0f1d.jpg
products/20260211-102828-7d4cb2.webp
```

## 图片规范

- 建议尺寸：按业务前端展示需求控制，商品主图通常建议接近正方形
- 格式：`JPG` 或 `WebP`
- 单张大小：建议控制在 `2MB` 以内

## 当前上传行为

- 上传目录固定为 `products/`
- 文件名由系统自动生成，避免重名覆盖
- 上传后返回 jsDelivr CDN 地址
- 现阶段文档不假定 `main.jpg`、`thumb.jpg`、`carousel/` 这类固定命名结构

## CDN 访问格式

```text
https://cdn.jsdelivr.net/gh/pxa264/cdn-images@main/products/{filename}
```

## 示例

```text
products/
├── 20260211-084830-47b5fe.webp
├── 20260211-102716-10149a.jpg
└── 20260213-113149-bb0f1d.jpg
```
