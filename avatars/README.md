# 用户头像目录

## 说明

用户头像按用户ID命名：`{user_id}.jpg`

## 默认头像

`default.jpg` - 当用户没有上传头像时使用

## 头像规范

- **尺寸**: 200x200px
- **格式**: JPG
- **大小**: < 50KB
- **命名**: {user_id}.jpg

## CDN访问格式

```
https://cdn.jsdelivr.net/gh/pxa264/cdn-images@main/avatars/{user_id}.jpg
https://cdn.jsdelivr.net/gh/pxa264/cdn-images@main/avatars/default.jpg
```

## 示例

```
avatars/
├── default.jpg    # 默认头像
├── 1.jpg         # 用户ID=1的头像
├── 2.jpg         # 用户ID=2的头像
└── 3.jpg         # 用户ID=3的头像
```
