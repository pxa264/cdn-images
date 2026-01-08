# CDN Images Repository

本仓库用于存放电商平台的所有图片资源，通过 [jsDelivr CDN](https://www.jsdelivr.com/) 加速访问。

## 📁 目录结构

```
cdn-images/
├── products/                    # 商品图片
│   ├── {product_id}/           # 按商品ID分目录
│   │   ├── main.jpg           # 主图 (800x800px, < 500KB)
│   │   ├── thumb.jpg          # 缩略图 (300x300px, < 100KB)
│   │   └── carousel/          # 轮播图 (800x800px, < 500KB)
│   │       ├── 1.jpg
│   │       ├── 2.jpg
│   │       └── 3.jpg
│   └── README.md              # 商品图片说明
│
├── avatars/                     # 用户头像
│   ├── {user_id}.jpg          # 用户ID命名 (200x200px, < 50KB)
│   └── default.jpg            # 默认头像
│
├── categories/                  # 分类图片
│   ├── {slug}.jpg             # 用分类的slug命名 (400x300px)
│   └── README.md
│
└── banners/                     # 轮播banner
    ├── home-banner-1.jpg      # 首页轮播 (1200x400px)
    └── home-banner-2.jpg
```

## 🔗 jsDelivr CDN URL格式

### 基本规则

**格式**:
```
https://cdn.jsdelivr.net/gh/pxa264/cdn-images@{branch}/{path}
```

**示例**:
```javascript
// 商品主图
https://cdn.jsdelivr.net/gh/pxa264/cdn-images@main/products/1/main.jpg

// 商品缩略图
https://cdn.jsdelivr.net/gh/pxa264/cdn-images@main/products/1/thumb.jpg

// 商品轮播图
https://cdn.jsdelivr.net/gh/pxa264/cdn-images@main/products/1/carousel/1.jpg

// 用户头像
https://cdn.jsdelivr.net/gh/pxa264/cdn-images@main/avatars/1.jpg

// 默认头像
https://cdn.jsdelivr.net/gh/pxa264/cdn-images@main/avatars/default.jpg

// 分类图片
https://cdn.jsdelivr.net/gh/pxa264/cdn-images@main/categories/electronics.jpg
```

### 版本管理

- **`@main`**: 使用main分支（最新版本）
- **`@latest`**: 自动获取最新版本
- **`@v1.0`**: 使用标签版本（稳定版本，推荐生产环境）

## 📐 图片规范

### 商品图片

| 类型 | 尺寸 | 格式 | 大小限制 | 说明 |
|------|------|------|----------|------|
| 主图 | 800x800px | JPG | < 500KB | 商品详情页主图 |
| 缩略图 | 300x300px | JPG | < 100KB | 商品列表页缩略图 |
| 轮播图 | 800x800px | JPG | < 500KB | 商品详情页轮播 |

### 用户头像

| 类型 | 尺寸 | 格式 | 大小限制 |
|------|------|------|----------|
| 头像 | 200x200px | JPG | < 50KB |

### 分类图片

| 类型 | 尺寸 | 格式 | 大小限制 |
|------|------|------|----------|
| 分类图 | 400x300px | JPG | < 200KB |

### Banner图片

| 类型 | 尺寸 | 格式 | 大小限制 |
|------|------|------|----------|
| 首页Banner | 1200x400px | JPG | < 1MB |

## 📝 当前商品列表

| ID | 商品名称 | 目录 | 轮播图数量 |
|----|----------|------|------------|
| 1 | 智能手表 Pro | `products/1/` | 3张 |
| 2 | 无线蓝牙耳机 | `products/2/` | 2张 |
| 3 | 便携式充电宝 | `products/3/` | 2张 |
| 4 | 智能家居音箱 | `products/4/` | 3张 |
| 5 | 4K超高清显示器 | `products/5/` | 2张 |
| 6 | 机械键盘 RGB | `products/6/` | 2张 |
| 7 | 人体工学鼠标 | `products/7/` | 1张 |
| 8 | 高清网络摄像头 | `products/8/` | 2张 |

## 🚀 使用方式

### 1. 添加新商品图片

```bash
# 1. 创建商品目录
mkdir -p products/{product_id}/carousel

# 2. 准备图片文件
# - main.jpg: 800x800px
# - thumb.jpg: 300x300px
# - carousel/1.jpg, 2.jpg, 3.jpg...

# 3. 放入对应目录
cp your-main.jpg products/{product_id}/main.jpg
cp your-thumb.jpg products/{product_id}/thumb.jpg
cp your-carousel-*.jpg products/{product_id}/carousel/

# 4. 提交到Git
git add products/{product_id}/
git commit -m "Add product {product_id} images"
git push origin main
```

### 2. 图片URL格式化

```javascript
// 在代码中生成CDN URL
const productId = 1;
const branch = 'main';

const mainImage = `https://cdn.jsdelivr.net/gh/pxa264/cdn-images@${branch}/products/${productId}/main.jpg`;
const thumbImage = `https://cdn.jsdelivr.net/gh/pxa264/cdn-images@${branch}/products/${productId}/thumb.jpg`;
```

### 3. 缓存说明

- jsDelivr会自动缓存图片
- 更新图片后，CDN缓存通常在1-5分钟内生效
- 如需立即清除缓存，可在URL后添加版本参数：`?v=timestamp`

## 📌 注意事项

### 文件命名

1. **使用小写字母和数字**
2. **避免特殊字符和空格**
3. **使用连字符`-`代替空格**
4. **文件扩展名使用小写**：`.jpg`, `.png`

### 图片质量

1. **压缩图片**：使用TinyPNG、ImageOptim等工具压缩
2. **保持尺寸**：严格遵守上述尺寸规范
3. **选择合适格式**：照片用JPG，透明图用PNG
4. **优化文件大小**：在保证质量前提下尽量减小文件

### 缓存策略

- 图片文件名不变时，CDN会缓存旧版本
- 如需更新图片且立即生效：
  - 方法1：修改文件名（如`main-v2.jpg`）
  - 方法2：添加查询参数（如`main.jpg?v=2`）
  - 方法3：等待CDN自动刷新（1-5分钟）

## 🔧 工具推荐

### 图片压缩
- [TinyPNG](https://tinypng.com/) - 在线图片压缩
- [ImageOptim](https://imageoptim.com/) - Mac图片优化工具
- [Squoosh](https://squoosh.app/) - Google图片压缩工具

### 图片编辑
- [Photoshop](https://www.adobe.com/products/photoshop.html)
- [GIMP](https://www.gimp.org/) - 免费开源
- [Photopea](https://www.photopea.com/) - 在线编辑器

### 批量处理
```bash
# 使用ImageMagick批量调整尺寸
convert input.jpg -resize 800x800 output.jpg

# 批量压缩
find . -name "*.jpg" -exec jpegoptim --max=80 {} \;
```

## 📄 License

本仓库图片资源仅供电商平台使用，未经授权不得用于其他商业用途。

## 🤝 贡献

添加图片时请遵循以下步骤：

1. 按照目录结构创建文件夹
2. 遵循图片尺寸和大小规范
3. 使用描述性文件名
4. 提交前确保图片质量
5. 更新本README文档

---

**最后更新**: 2026-01-08
**维护者**: pxa264
**CDN提供商**: [jsDelivr](https://www.jsdelivr.com/)
