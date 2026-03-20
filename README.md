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
https://cdn.jsdelivr.net/gh/pxa264/cdn-images@main/products/1/main.jpg
```

## 各目录说明

- `avatars/`: 用户头像资源，详见 `avatars/README.md`
- `banners/`: 首页轮播 Banner，详见 `banners/README.md`
- `categories/`: 商品分类图片，详见 `categories/README.md`
- `products/`: 商品主图、缩略图和轮播图，详见 `products/README.md`

## 商品图片约定

推荐以商品 ID 作为一级目录，常用结构如下：

```text
products/
└── 1/
    ├── main.jpg
    ├── thumb.jpg
    └── carousel/
        ├── 1.jpg
        ├── 2.jpg
        └── 3.jpg
```

对应访问地址：

```text
https://cdn.jsdelivr.net/gh/pxa264/cdn-images@main/products/1/main.jpg
https://cdn.jsdelivr.net/gh/pxa264/cdn-images@main/products/1/thumb.jpg
https://cdn.jsdelivr.net/gh/pxa264/cdn-images@main/products/1/carousel/1.jpg
```

## 使用建议

- 优先使用 JPG 或 WebP
- 文件名保持稳定，避免频繁变更路径
- 上传后等待 jsDelivr 刷新缓存再验证访问
- 大图建议先压缩，避免不必要的带宽消耗

## 维护说明

- 仓库地址：`git@github.com:pxa264/cdn-images.git`
- 默认分支：`main`
- 建议所有图片资源按业务目录分类存放，避免把无关文件混入根目录
