# 每日健康菜品推送配置指南

## 📋 功能说明

这个功能会在每个工作日（周一到周五）自动从菜谱中选择一个低油低盐的健康菜品，并发送到您的邮箱。

### 🥗 健康菜品筛选标准

系统会优先推送以下分类的菜品：
- **蒸菜**：蒸制方式，保留营养，少油少盐
- **汤**：清淡营养，易消化  
- **烫菜**：水煮烫制，清淡健康
- **主食**：主食类，适量食用
- **早餐**：早餐选择，营养均衡

同时会自动排除含有以下关键词的高油高盐菜品：
- 炸、油炸、油焖、红烧、糖醋
- 辣、麻辣、卤、盐焗
- 酱、豉油、剁椒等

## 🚀 配置步骤

### 1. Fork 本仓库到您的GitHub账号

### 2. 配置邮箱服务

您需要准备一个用于发送邮件的邮箱（建议使用Gmail、QQ邮箱或163邮箱等）。

#### Gmail配置示例：
- SMTP服务器: `smtp.gmail.com`
- SMTP端口: `465`
- 需要开启"应用专用密码"功能

#### QQ邮箱配置示例：
- SMTP服务器: `smtp.qq.com`
- SMTP端口: `465` 或 `587`
- 需要开启SMTP服务并获取授权码

#### 163邮箱配置示例：
- SMTP服务器: `smtp.163.com`
- SMTP端口: `465` 或 `994`
- 需要开启SMTP服务并获取授权码

### 3. 在GitHub仓库中配置Secrets

进入您Fork的仓库，依次点击：**Settings** → **Secrets and variables** → **Actions** → **New repository secret**

添加以下5个Secrets：

| Secret名称 | 说明 | 示例值 |
|-----------|------|--------|
| `TO_EMAIL` | 接收邮件的邮箱地址 | `huzhe01@foxmail.com` |
| `FROM_EMAIL` | 发送邮件的邮箱地址 | `your_email@gmail.com` |
| `EMAIL_PASSWORD` | 发送邮箱的密码或授权码 | `your_app_password` |
| `SMTP_SERVER` | SMTP服务器地址 | `smtp.gmail.com` |
| `SMTP_PORT` | SMTP端口 | `465` |

### 4. 启用GitHub Actions

1. 进入仓库的 **Actions** 标签页
2. 点击 **I understand my workflows, go ahead and enable them**
3. 找到 "每日健康菜品推送" 工作流
4. 点击 **Enable workflow**

### 5. 测试运行

您可以手动触发一次测试：

1. 进入 **Actions** 标签页
2. 点击左侧的 "每日健康菜品推送"
3. 点击右侧的 **Run workflow** 按钮
4. 选择分支并点击绿色的 **Run workflow** 按钮

几秒钟后，您应该会收到一封测试邮件！

## ⏰ 推送时间

- 默认设置为每个工作日（周一到周五）**北京时间上午9点**
- 如需修改时间，请编辑 `.github/workflows/daily_recipe.yml` 文件中的 cron 表达式

### Cron表达式说明：
```yaml
'0 1 * * 1-5'  # 每个工作日UTC时间1点（北京时间9点）
```

格式：`分钟 小时 日 月 星期`
- 星期：0-6（0表示周日，1-5表示周一到周五）
- 时区：GitHub Actions使用UTC时区，北京时间需要减8小时

### 时间修改示例：
- 北京时间早上7点：`'0 23 * * 0-4'`（前一天UTC 23点）
- 北京时间中午12点：`'0 4 * * 1-5'`（当天UTC 4点）
- 北京时间下午6点：`'0 10 * * 1-5'`（当天UTC 10点）

## 📧 邮件内容

每封邮件包含：
- ✅ 菜品名称和分类
- ✅ 健康提示说明
- ✅ 完整的食材配料
- ✅ 详细的制作步骤
- ✅ 精美的HTML排版
- ✅ 推送时间记录

## 🔧 本地测试

如果您想在本地测试脚本：

```bash
# 1. 克隆仓库
git clone https://github.com/YOUR_USERNAME/CookLikeHOC.git
cd CookLikeHOC

# 2. 设置环境变量
export TO_EMAIL="huzhe01@foxmail.com"
export FROM_EMAIL="your_email@gmail.com"
export EMAIL_PASSWORD="your_password"
export SMTP_SERVER="smtp.gmail.com"
export SMTP_PORT="465"

# 3. 运行脚本
python3 send_daily_recipe.py
```

## 🛠️ 自定义配置

### 修改健康菜品分类

编辑 `send_daily_recipe.py` 文件中的 `HEALTHY_CATEGORIES` 字典：

```python
HEALTHY_CATEGORIES = {
    '蒸菜': {'priority': 1, 'reason': '蒸制方式，保留营养，少油少盐'},
    '汤': {'priority': 1, 'reason': '清淡营养，易消化'},
    # 添加更多分类...
}
```

### 修改排除关键词

编辑 `send_daily_recipe.py` 文件中的 `EXCLUDE_KEYWORDS` 列表：

```python
EXCLUDE_KEYWORDS = [
    '炸', '油炸', '油焖', '红烧', '糖醋', '辣', '麻辣',
    # 添加更多关键词...
]
```

## ❓ 常见问题

### Q: 没有收到邮件？
A: 请检查：
1. GitHub Actions是否成功运行（查看Actions标签页）
2. Secrets配置是否正确
3. 发送邮箱的SMTP服务是否已开启
4. 垃圾邮件文件夹中是否有邮件

### Q: 邮件发送失败？
A: 可能的原因：
1. 邮箱密码/授权码错误
2. SMTP服务器或端口配置错误
3. 邮箱安全设置阻止了第三方登录
4. 网络连接问题

### Q: 想修改推送频率？
A: 修改 `.github/workflows/daily_recipe.yml` 中的 cron 表达式，例如：
- 每天推送：`'0 1 * * *'`
- 每周一、三、五：`'0 1 * * 1,3,5'`
- 每月1号：`'0 1 1 * *'`

### Q: 想停止推送？
A: 有两种方法：
1. 禁用工作流：进入Actions → 选择工作流 → 点击右上角的"..."→ Disable workflow
2. 删除文件：删除 `.github/workflows/daily_recipe.yml` 文件

## 📝 注意事项

1. ⚠️ GitHub Actions的免费额度为每月2000分钟，这个简单任务每次运行不到1分钟，完全够用
2. ⚠️ 请妥善保管您的邮箱密码/授权码，不要泄露给他人
3. ⚠️ 建议使用应用专用密码而不是邮箱主密码
4. ⚠️ 如果长期不使用，建议禁用工作流以节省资源

## 💡 技术支持

如有问题，欢迎在仓库中提Issue讨论！

---

祝您健康饮食，生活愉快！🥗✨
