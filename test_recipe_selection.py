#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试菜品选择功能（不发送邮件）
"""

import sys
sys.path.insert(0, '/workspace')
from send_daily_recipe import get_all_recipes, select_recipe, read_recipe_content

def main():
    print("=" * 60)
    print("🥗 老乡鸡健康菜品选择测试")
    print("=" * 60)
    
    # 获取所有健康菜品
    print("\n📋 正在扫描健康菜品...")
    recipes = get_all_recipes()
    print(f"✅ 找到 {len(recipes)} 个低油低盐菜品\n")
    
    # 按分类统计
    categories = {}
    for recipe in recipes:
        cat = recipe['category']
        if cat not in categories:
            categories[cat] = []
        categories[cat].append(recipe)
    
    print("📊 分类统计：")
    for cat in sorted(categories.keys()):
        count = len(categories[cat])
        priority = categories[cat][0]['priority']
        reason = categories[cat][0]['reason']
        print(f"  {cat}: {count}个 (优先级{priority} - {reason})")
    
    # 随机选择一个菜品
    print("\n" + "=" * 60)
    recipe = select_recipe(recipes)
    
    if recipe:
        print(f"🎲 随机选择的菜品：")
        print(f"  📛 名称：{recipe['name']}")
        print(f"  📂 分类：{recipe['category']}")
        print(f"  ⭐ 优先级：{recipe['priority']}")
        print(f"  💚 健康理由：{recipe['reason']}")
        print(f"  📄 文件：{recipe['file']}")
        
        # 显示菜品内容
        print("\n" + "=" * 60)
        print("📖 菜品详细内容：")
        print("=" * 60)
        content = read_recipe_content(recipe['file'])
        print(content)
        print("=" * 60)
        
    else:
        print("❌ 选择菜品失败")
    
    print("\n✨ 测试完成！")
    print("\n💡 提示：如需发送邮件，请配置环境变量后运行 send_daily_recipe.py")

if __name__ == '__main__':
    main()
