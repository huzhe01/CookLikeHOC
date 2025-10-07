#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
每日推送低油低盐菜品到邮箱
"""

import os
import json
import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from datetime import datetime
from pathlib import Path

# 低油低盐的健康菜品分类
HEALTHY_CATEGORIES = {
    '蒸菜': {'priority': 1, 'reason': '蒸制方式，保留营养，少油少盐'},
    '汤': {'priority': 1, 'reason': '清淡营养，易消化'},
    '烫菜': {'priority': 1, 'reason': '水煮烫制，清淡健康'},
    '主食': {'priority': 2, 'reason': '主食类，适量食用'},
    '早餐': {'priority': 2, 'reason': '早餐选择，营养均衡'}
}

# 需要排除的高油高盐菜品（关键词）
EXCLUDE_KEYWORDS = [
    '炸', '油炸', '油焖', '红烧', '糖醋', '辣', '麻辣',
    '卤', '盐焗', '咕咾', '农家小炒肉', '鱼香',
    '酱', '豉油', '剁椒', '外婆菜', '梅干菜'
]


def get_all_recipes():
    """获取所有低油低盐的菜品"""
    recipes = []
    
    for category, info in HEALTHY_CATEGORIES.items():
        category_path = Path(f'/workspace/{category}')
        if not category_path.exists():
            continue
            
        for recipe_file in category_path.glob('*.md'):
            if recipe_file.name == 'README.md':
                continue
            
            recipe_name = recipe_file.stem
            
            # 排除含有高油高盐关键词的菜品
            if any(keyword in recipe_name for keyword in EXCLUDE_KEYWORDS):
                continue
            
            recipes.append({
                'name': recipe_name,
                'category': category,
                'file': str(recipe_file),
                'priority': info['priority'],
                'reason': info['reason']
            })
    
    return recipes


def read_recipe_content(recipe_file):
    """读取菜品内容"""
    try:
        with open(recipe_file, 'r', encoding='utf-8') as f:
            content = f.read()
        return content
    except Exception as e:
        return f"读取菜品内容失败: {str(e)}"


def select_recipe(recipes):
    """选择一个菜品，优先选择健康度更高的"""
    if not recipes:
        return None
    
    # 按优先级分组
    priority_groups = {}
    for recipe in recipes:
        priority = recipe['priority']
        if priority not in priority_groups:
            priority_groups[priority] = []
        priority_groups[priority].append(recipe)
    
    # 优先从优先级1（最健康）的菜品中选择
    for priority in sorted(priority_groups.keys()):
        if priority_groups[priority]:
            return random.choice(priority_groups[priority])
    
    return None


def send_email(recipe, to_email, smtp_server, smtp_port, from_email, password):
    """发送邮件"""
    try:
        # 读取菜品内容
        content = read_recipe_content(recipe['file'])
        
        # 创建邮件
        msg = MIMEMultipart('alternative')
        msg['From'] = Header(f"老乡鸡菜品推送 <{from_email}>", 'utf-8')
        msg['To'] = Header(to_email, 'utf-8')
        msg['Subject'] = Header(f"今日推荐：{recipe['name']} ({recipe['category']})", 'utf-8')
        
        # 邮件正文（HTML格式）
        html_content = f"""
        <html>
        <head>
            <meta charset="utf-8">
            <style>
                body {{
                    font-family: 'Microsoft YaHei', Arial, sans-serif;
                    line-height: 1.6;
                    color: #333;
                    max-width: 800px;
                    margin: 0 auto;
                    padding: 20px;
                }}
                .header {{
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    color: white;
                    padding: 20px;
                    border-radius: 10px;
                    margin-bottom: 20px;
                }}
                .category {{
                    display: inline-block;
                    background: rgba(255,255,255,0.2);
                    padding: 5px 15px;
                    border-radius: 20px;
                    font-size: 14px;
                    margin-top: 10px;
                }}
                .reason {{
                    background: #f0f9ff;
                    border-left: 4px solid #0ea5e9;
                    padding: 15px;
                    margin: 20px 0;
                    border-radius: 0 5px 5px 0;
                }}
                .content {{
                    background: #fff;
                    padding: 20px;
                    border-radius: 10px;
                    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
                }}
                .footer {{
                    text-align: center;
                    margin-top: 30px;
                    padding-top: 20px;
                    border-top: 1px solid #eee;
                    color: #666;
                    font-size: 14px;
                }}
                h2 {{
                    color: #667eea;
                }}
                code {{
                    background: #f4f4f4;
                    padding: 2px 6px;
                    border-radius: 3px;
                }}
            </style>
        </head>
        <body>
            <div class="header">
                <h1>🍽️ 今日健康菜品推荐</h1>
                <h2>{recipe['name']}</h2>
                <span class="category">📂 {recipe['category']}</span>
            </div>
            
            <div class="reason">
                <strong>💚 健康提示：</strong>{recipe['reason']}
            </div>
            
            <div class="content">
                {content.replace('\n', '<br>').replace('# ', '<h2>').replace('## ', '<h3>').replace('- ', '• ')}
            </div>
            
            <div class="footer">
                <p>📅 推送时间：{datetime.now().strftime('%Y年%m月%d日 %H:%M')}</p>
                <p>💡 提示：这是一份来自《老乡鸡菜品溯源报告》的菜谱，已为您筛选出低油低盐的健康选择</p>
                <p>🔗 更多菜品请访问：<a href="https://github.com/Gar-b-age/CookLikeHOC">CookLikeHOC</a></p>
            </div>
        </body>
        </html>
        """
        
        html_part = MIMEText(html_content, 'html', 'utf-8')
        msg.attach(html_part)
        
        # 发送邮件
        server = smtplib.SMTP_SSL(smtp_server, smtp_port)
        server.login(from_email, password)
        server.sendmail(from_email, to_email, msg.as_string())
        server.quit()
        
        print(f"✅ 邮件发送成功！")
        print(f"📧 收件人：{to_email}")
        print(f"🍳 菜品：{recipe['name']} ({recipe['category']})")
        return True
        
    except Exception as e:
        print(f"❌ 邮件发送失败: {str(e)}")
        return False


def main():
    """主函数"""
    print("=" * 50)
    print("🥗 老乡鸡健康菜品每日推送")
    print("=" * 50)
    
    # 获取环境变量
    to_email = os.environ.get('TO_EMAIL', 'huzhe01@foxmail.com')
    smtp_server = os.environ.get('SMTP_SERVER', 'smtp.gmail.com')
    smtp_port = int(os.environ.get('SMTP_PORT', '465'))
    from_email = os.environ.get('FROM_EMAIL', '')
    password = os.environ.get('EMAIL_PASSWORD', '')
    
    if not from_email or not password:
        print("❌ 错误：请设置 FROM_EMAIL 和 EMAIL_PASSWORD 环境变量")
        return
    
    # 获取所有健康菜品
    print("\n📋 正在扫描健康菜品...")
    recipes = get_all_recipes()
    print(f"✅ 找到 {len(recipes)} 个低油低盐菜品")
    
    if not recipes:
        print("❌ 没有找到符合条件的菜品")
        return
    
    # 选择一个菜品
    recipe = select_recipe(recipes)
    if not recipe:
        print("❌ 选择菜品失败")
        return
    
    print(f"\n🎲 随机选择：{recipe['name']} ({recipe['category']})")
    print(f"💚 健康理由：{recipe['reason']}")
    
    # 发送邮件
    print(f"\n📧 正在发送邮件到 {to_email}...")
    success = send_email(recipe, to_email, smtp_server, smtp_port, from_email, password)
    
    if success:
        print("\n✨ 任务完成！")
    else:
        print("\n❌ 任务失败！")


if __name__ == '__main__':
    main()
