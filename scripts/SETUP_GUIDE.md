# 每日健康菜品推送 - 快速配置指南

## 📋 配置步骤

### 第一步：获取邮箱授权码

#### 使用 QQ 邮箱（推荐）

1. 登录 [QQ 邮箱](https://mail.qq.com)
2. 点击**设置** → **账户**
3. 找到 **POP3/IMAP/SMTP/Exchange/CardDAV/CalDAV服务**
4. 开启 **IMAP/SMTP服务**
5. 按提示发送短信后，会生成一个**授权码**（保存好，后面要用）

#### 使用 163 邮箱

1. 登录 [163 邮箱](https://mail.163.com)
2. 设置 → POP3/SMTP/IMAP
3. 开启 SMTP 服务
4. 生成授权码

#### 使用 Gmail

1. 开启两步验证
2. 生成应用专用密码
3. 使用 `smtp.gmail.com` 端口 `587`

### 第二步：配置 GitHub Secrets

1. 打开你的 GitHub 仓库页面
2. 点击 **Settings**（设置）
3. 在左侧菜单找到 **Secrets and variables** → **Actions**
4. 点击 **New repository secret** 添加以下两个密钥：

   **密钥 1：FROM_EMAIL**
   - Name: `FROM_EMAIL`
   - Secret: 你的发件邮箱地址（例如：`your_email@qq.com`）

   **密钥 2：EMAIL_PASSWORD**
   - Name: `EMAIL_PASSWORD`
   - Secret: 刚才获取的邮箱授权码（**不是邮箱登录密码**）

### 第三步：修改收件人邮箱（可选）

如果需要修改收件人邮箱，编辑 `scripts/daily_recipe_sender.py` 文件的最后一行：

```python
target_email = "huzhe01@foxmail.com"  # 改成你想要的收件邮箱
```

### 第四步：启用 GitHub Actions

1. 进入仓库的 **Actions** 标签页
2. 如果 Actions 被禁用，点击 **I understand my workflows, go ahead and enable them**
3. 找到 **每日健康菜品推送** workflow

### 第五步：测试运行

**手动触发测试：**

1. 在 Actions 页面选择 **每日健康菜品推送**
2. 点击 **Run workflow** → **Run workflow**
3. 等待运行完成（约10-30秒）
4. 检查你的邮箱是否收到邮件（也检查一下垃圾邮件文件夹）

**查看运行日志：**
- 点击运行记录可以查看详细日志
- 如果失败，日志中会显示错误信息

## 🔧 高级配置

### 修改推送时间

编辑 `.github/workflows/daily-recipe.yml` 文件中的 cron 表达式：

```yaml
schedule:
  - cron: '0 0 * * 1-5'  # 当前：工作日北京时间早8点
```

**常用时间设置：**
- `0 0 * * 1-5`: 北京时间 08:00（周一到周五）
- `0 2 * * 1-5`: 北京时间 10:00（周一到周五）
- `0 4 * * 1-5`: 北京时间 12:00（周一到周五）
- `0 12 * * 1-5`: 北京时间 20:00（周一到周五）

**⚠️ 注意：** GitHub Actions 使用 UTC 时区，北京时间需要减去 8 小时

### 修改筛选条件

编辑 `scripts/daily_recipe_sender.py` 中的筛选逻辑：

```python
# 修改油盐阈值（单位：克）
is_low_oil = total_oil < 50   # 油的上限
is_low_salt = total_salt < 10  # 盐的上限

# 修改优先类别
self.low_oil_categories = ['蒸菜', '烫菜', '汤', '凉拌', '早餐']
```

## 🎯 本地测试

如果想在本地运行脚本进行测试：

**Linux/Mac:**
```bash
export FROM_EMAIL="your_email@qq.com"
export EMAIL_PASSWORD="your_authorization_code"
export SMTP_SERVER="smtp.qq.com"
export SMTP_PORT="465"

python scripts/daily_recipe_sender.py
```

**Windows (PowerShell):**
```powershell
$env:FROM_EMAIL="your_email@qq.com"
$env:EMAIL_PASSWORD="your_authorization_code"
$env:SMTP_SERVER="smtp.qq.com"
$env:SMTP_PORT="465"

python scripts/daily_recipe_sender.py
```

**Windows (CMD):**
```cmd
set FROM_EMAIL=your_email@qq.com
set EMAIL_PASSWORD=your_authorization_code
set SMTP_SERVER=smtp.qq.com
set SMTP_PORT=465

python scripts/daily_recipe_sender.py
```

## ❓ 常见问题

### Q1: 没有收到邮件？
1. 检查垃圾邮件文件夹
2. 确认 GitHub Secrets 配置正确
3. 查看 Actions 运行日志是否有错误
4. 确认收件邮箱地址正确

### Q2: 发送失败，显示认证错误？
1. 确认使用的是**授权码**而不是邮箱登录密码
2. 确认 SMTP 服务已开启
3. QQ 邮箱需要使用授权码，不是QQ密码

### Q3: GitHub Actions 没有自动运行？
1. 确认 Actions 已启用
2. 确认 workflow 文件路径正确：`.github/workflows/daily-recipe.yml`
3. 查看 Actions 标签页是否有错误提示
4. **注意：** GitHub Actions 在仓库没有活动时可能会暂停，手动触发一次即可恢复

### Q4: 想要多个收件人？
修改 `scripts/daily_recipe_sender.py`，将 `target_email` 改为列表：

```python
target_emails = ["email1@example.com", "email2@example.com"]
for email in target_emails:
    sender.run(email)
```

### Q5: 如何更换 SMTP 服务器？
在 `.github/workflows/daily-recipe.yml` 中修改：

```yaml
env:
  SMTP_SERVER: smtp.163.com  # 163邮箱
  SMTP_PORT: 465             # SSL端口
```

## 📧 支持的邮箱服务

| 邮箱服务 | SMTP服务器 | 端口 | 说明 |
|---------|-----------|------|------|
| QQ邮箱 | smtp.qq.com | 465 (推荐) / 587 | 需要授权码，建议用465 |
| 163邮箱 | smtp.163.com | 465/587 | 需要授权码 |
| Gmail | smtp.gmail.com | 587 | 需要应用专用密码 |
| Outlook | smtp.office365.com | 587 | 支持 |
| 阿里云邮箱 | smtp.aliyun.com | 465 | 支持 |

## 🎉 完成

配置完成后，系统会在每个工作日自动为你推送健康菜品！

祝你烹饪愉快！🍳

