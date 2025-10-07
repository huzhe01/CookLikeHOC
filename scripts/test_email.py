#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
邮件发送测试脚本 - 用于诊断SMTP连接问题
"""

import os
import smtplib
import ssl
from email.mime.text import MIMEText
from email.header import Header

def test_smtp_connection():
    """测试SMTP连接"""
    print("=" * 60)
    print("📧 QQ邮箱 SMTP 连接测试")
    print("=" * 60)
    
    # 读取配置
    from_email = os.getenv('FROM_EMAIL')
    email_password = os.getenv('EMAIL_PASSWORD')
    to_email = input("请输入收件邮箱（按回车使用发件邮箱）: ").strip() or from_email
    
    if not from_email or not email_password:
        print("❌ 错误: 请先设置环境变量 FROM_EMAIL 和 EMAIL_PASSWORD")
        print("\n示例:")
        print('export FROM_EMAIL="your@qq.com"')
        print('export EMAIL_PASSWORD="your_auth_code"')
        return
    
    print(f"\n配置信息:")
    print(f"  发件邮箱: {from_email}")
    print(f"  收件邮箱: {to_email}")
    print(f"  授权码长度: {len(email_password)} 字符")
    print(f"  授权码前4位: {email_password[:4]}****")
    
    # 测试不同的配置
    configs = [
        ("smtp.qq.com", 465, "SSL"),
        ("smtp.qq.com", 587, "TLS"),
    ]
    
    for smtp_server, smtp_port, protocol in configs:
        print(f"\n{'=' * 60}")
        print(f"🔍 测试配置: {smtp_server}:{smtp_port} ({protocol})")
        print(f"{'=' * 60}")
        
        try:
            # 创建邮件
            message = MIMEText("这是一封测试邮件\n\nCookLikeHOC 健康菜品推送系统", 'plain', 'utf-8')
            message['From'] = from_email  # QQ邮箱要求From必须是纯邮箱地址
            message['To'] = to_email
            message['Subject'] = Header("SMTP 连接测试", 'utf-8')
            
            # 连接服务器
            print(f"📡 正在连接到 {smtp_server}:{smtp_port}...")
            
            if smtp_port == 465:
                # SSL连接
                context = ssl.create_default_context()
                server = smtplib.SMTP_SSL(smtp_server, smtp_port, context=context, timeout=10)
            else:
                # TLS连接
                server = smtplib.SMTP(smtp_server, smtp_port, timeout=10)
                print("🔐 启动TLS加密...")
                server.starttls()
            
            print("✓ 连接成功")
            
            # 登录
            print(f"🔑 正在登录 {from_email}...")
            server.set_debuglevel(0)  # 关闭调试输出，避免显示密码
            server.login(from_email, email_password)
            print("✓ 登录成功")
            
            # 发送邮件
            print(f"📤 正在发送测试邮件到 {to_email}...")
            server.sendmail(from_email, [to_email], message.as_string())
            print("✓ 邮件发送成功")
            
            # 关闭连接
            server.quit()
            print("\n✅ 成功！此配置可以正常工作")
            print(f"   建议使用: SMTP_SERVER={smtp_server}, SMTP_PORT={smtp_port}")
            return True
            
        except smtplib.SMTPAuthenticationError as e:
            print(f"❌ 认证失败: {e}")
            print("   可能的原因:")
            print("   1. 授权码不正确")
            print("   2. SMTP服务未开启")
            print("   3. 授权码已过期，需要重新生成")
            
        except smtplib.SMTPServerDisconnected as e:
            print(f"❌ 服务器断开连接: {e}")
            print("   可能的原因:")
            print("   1. 授权码格式不正确（有无多余空格？）")
            print("   2. QQ邮箱安全策略限制")
            print("   3. 网络连接问题")
            
        except smtplib.SMTPException as e:
            print(f"❌ SMTP错误: {e}")
            
        except Exception as e:
            print(f"❌ 连接失败: {type(e).__name__}: {e}")
    
    print("\n" + "=" * 60)
    print("❌ 所有配置都失败了")
    print("=" * 60)
    
    print("\n🔧 故障排查建议:")
    print("\n1. 检查授权码:")
    print("   - 确保授权码是从QQ邮箱生成的16位字符")
    print("   - 不是QQ密码！")
    print("   - 检查是否有多余的空格")
    print("   - 尝试重新生成授权码")
    
    print("\n2. 确认SMTP服务已开启:")
    print("   - 登录 https://mail.qq.com")
    print("   - 设置 -> 账户 -> POP3/IMAP/SMTP服务")
    print("   - 确认显示'已开启'")
    
    print("\n3. 检查网络:")
    print("   - 确认可以访问smtp.qq.com")
    print("   - 检查防火墙设置")
    print("   - 尝试切换网络（比如手机热点）")
    
    print("\n4. 尝试其他邮箱:")
    print("   - 163邮箱: smtp.163.com:465")
    print("   - Gmail: smtp.gmail.com:587")
    
    return False

def quick_test():
    """快速测试 - 不发送邮件，只测试连接和登录"""
    print("=" * 60)
    print("⚡ 快速连接测试（不发送邮件）")
    print("=" * 60)
    
    from_email = os.getenv('FROM_EMAIL')
    email_password = os.getenv('EMAIL_PASSWORD')
    
    if not from_email or not email_password:
        print("❌ 错误: 请先设置环境变量")
        return
    
    print(f"发件邮箱: {from_email}")
    print(f"授权码: {email_password[:4]}{'*' * (len(email_password)-4)}")
    
    try:
        print("\n正在测试 smtp.qq.com:465...")
        context = ssl.create_default_context()
        server = smtplib.SMTP_SSL("smtp.qq.com", 465, context=context, timeout=10)
        server.set_debuglevel(1)
        print("\n尝试登录...")
        server.login(from_email, email_password)
        server.quit()
        print("\n✅ 连接和登录成功！")
        return True
    except Exception as e:
        print(f"\n❌ 失败: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "quick":
        quick_test()
    else:
        test_smtp_connection()

