# 🥗 每日健康菜品推送 - 快速开始

## 📌 功能概述

自动在每个**工作日上午9点**（北京时间）推送一个**低油低盐**的健康菜品到您的邮箱 `huzhe01@foxmail.com`。

系统已筛选出 **66个健康菜品**，包括：
- 🍜 蒸菜 (21个)
- 🥣 早餐 (20个) 
- 🍝 主食 (14个)
- 🥬 烫菜 (8个)
- 🍲 汤 (3个)

## ⚡ 三步配置

### 步骤1：Fork仓库
将本仓库Fork到您的GitHub账号

### 步骤2：配置邮箱Secrets
进入 **Settings** → **Secrets and variables** → **Actions**，添加以下5个Secret：

| 名称 | 值 | 说明 |
|-----|---|------|
| `TO_EMAIL` | `huzhe01@foxmail.com` | 接收邮箱 |
| `FROM_EMAIL` | 您的发送邮箱 | 如：`yourmail@gmail.com` |
| `EMAIL_PASSWORD` | 邮箱授权码 | 不是登录密码！ |
| `SMTP_SERVER` | SMTP服务器 | Gmail: `smtp.gmail.com` |
| `SMTP_PORT` | SMTP端口 | Gmail: `465` |

### 步骤3：启用Actions
1. 进入 **Actions** 标签页
2. 点击启用工作流
3. 点击 **Run workflow** 测试

## 📧 常用邮箱配置

### Gmail
```
SMTP_SERVER: smtp.gmail.com
SMTP_PORT: 465
需要开启"两步验证"并生成"应用专用密码"
```

### QQ邮箱
```
SMTP_SERVER: smtp.qq.com
SMTP_PORT: 465
需要开启SMTP服务并获取授权码
```

### 163邮箱
```
SMTP_SERVER: smtp.163.com
SMTP_PORT: 465
需要开启SMTP服务并获取授权码
```

## 📖 详细文档

完整配置指南请查看：[详细配置文档](./docs/daily_recipe_setup.md)

## ✨ 特色功能

✅ 自动筛选低油低盐菜品（排除炸、卤、红烧等高油高盐菜品）  
✅ 优先推送蒸菜、汤类等最健康的菜品  
✅ 精美的HTML邮件排版  
✅ 完整的食材和步骤说明  
✅ 工作日自动推送，周末休息  

## 🛠️ 本地测试

```bash
# 设置环境变量
export TO_EMAIL="huzhe01@foxmail.com"
export FROM_EMAIL="yourmail@gmail.com"
export EMAIL_PASSWORD="your_app_password"
export SMTP_SERVER="smtp.gmail.com"
export SMTP_PORT="465"

# 运行脚本
python3 send_daily_recipe.py
```

## ❓ 遇到问题？

1. 查看 [详细配置文档](./docs/daily_recipe_setup.md)
2. 检查Actions运行日志
3. 确认Secrets配置正确
4. 检查垃圾邮件文件夹

---

祝您健康饮食，享受美食！🍽️✨
