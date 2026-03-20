# CDN Images

用于存放 AI Mall 项目的静态图片资源，并通过 GitHub + jsDelivr 对外分发。

## 目录结构

```text
cdn-images/
├── avatars/            # 用户头像
├── banners/            # 首页 Banner
├── categories/         # 分类图片
└── products/           # 商品图片
```

## CDN 地址格式

默认使用 `main` 分支发布，访问格式如下：

```text
https://cdn.jsdelivr.net/gh/pxa264/cdn-images@main/<path>
```

示例：

```text
https://cdn.jsdelivr.net/gh/pxa264/cdn-images@main/avatars/default.jpg
https://cdn.jsdelivr.net/gh/pxa264/cdn-images@main/banners/home-banner-1.jpg
https://cdn.jsdelivr.net/gh/pxa264/cdn-images@main/categories/electronics.jpg
https://cdn.jsdelivr.net/gh/pxa264/cdn-images@main/products/20260213-113149-bb0f1d.jpg
```

## 各目录说明

- `avatars/`: 用户头像资源，详见 `avatars/README.md`
- `banners/`: 首页轮播 Banner，详见 `banners/README.md`
- `categories/`: 商品分类图片，详见 `categories/README.md`
- `products/`: 商品图片上传目录，详见 `products/README.md`

## 商品图片说明

当前 AI Mall 后台上传服务会将商品图片直接写入 `products/` 根目录，并自动生成唯一文件名。

当前命名格式：

```text
YYYYMMDD-HHmmss-随机6位.扩展名
```

示例：

```text
products/20260213-113149-bb0f1d.jpg
products/20260211-102828-7d4cb2.webp
```

对应 CDN 地址：

```text
https://cdn.jsdelivr.net/gh/pxa264/cdn-images@main/products/20260213-113149-bb0f1d.jpg
https://cdn.jsdelivr.net/gh/pxa264/cdn-images@main/products/20260211-102828-7d4cb2.webp
```

如果业务后续需要按商品 ID、用途或轮播图层级做更细的目录设计，应以应用代码实际实现为准；当前仓库以“扁平商品图片目录 + 唯一文件名”作为事实标准。

## 使用建议

- 优先使用 JPG 或 WebP
- 文件名保持稳定，避免频繁变更路径
- 上传后等待 jsDelivr 刷新缓存再验证访问
- 大图建议先压缩，避免不必要的带宽消耗

## 维护说明

- 仓库地址：`git@github.com:pxa264/cdn-images.git`
- 默认分支：`main`
- 建议所有图片资源按业务目录分类存放，避免把无关文件混入根目录
