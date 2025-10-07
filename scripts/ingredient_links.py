#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
食材购买链接生成器
基于美团小象超市的商品链接
"""

# 食材到美团小象超市的映射
INGREDIENT_LINKS = {
    # 肉类
    '猪肉': 'https://s.meituan.com/v1/mss_126c814fe3f743a29d82aa9e962d2fc2/search/1?q=猪肉',
    '牛肉': 'https://s.meituan.com/v1/mss_126c814fe3f743a29d82aa9e962d2fc2/search/1?q=牛肉',
    '鸡肉': 'https://s.meituan.com/v1/mss_126c814fe3f743a29d82aa9e962d2fc2/search/1?q=鸡肉',
    '鸡腿': 'https://s.meituan.com/v1/mss_126c814fe3f743a29d82aa9e962d2fc2/search/1?q=鸡腿',
    '鸡翅': 'https://s.meituan.com/v1/mss_126c814fe3f743a29d82aa9e962d2fc2/search/1?q=鸡翅',
    '鸡胸肉': 'https://s.meituan.com/v1/mss_126c814fe3f743a29d82aa9e962d2fc2/search/1?q=鸡胸肉',
    '排骨': 'https://s.meituan.com/v1/mss_126c814fe3f743a29d82aa9e962d2fc2/search/1?q=排骨',
    '大排': 'https://s.meituan.com/v1/mss_126c814fe3f743a29d82aa9e962d2fc2/search/1?q=猪大排',
    '肉片': 'https://s.meituan.com/v1/mss_126c814fe3f743a29d82aa9e962d2fc2/search/1?q=猪肉片',
    '肉丝': 'https://s.meituan.com/v1/mss_126c814fe3f743a29d82aa9e962d2fc2/search/1?q=肉丝',
    '虾': 'https://s.meituan.com/v1/mss_126c814fe3f743a29d82aa9e962d2fc2/search/1?q=虾',
    '虾仁': 'https://s.meituan.com/v1/mss_126c814fe3f743a29d82aa9e962d2fc2/search/1?q=虾仁',
    '河虾': 'https://s.meituan.com/v1/mss_126c814fe3f743a29d82aa9e962d2fc2/search/1?q=河虾',
    '鱼': 'https://s.meituan.com/v1/mss_126c814fe3f743a29d82aa9e962d2fc2/search/1?q=鱼',
    '鱼块': 'https://s.meituan.com/v1/mss_126c814fe3f743a29d82aa9e962d2fc2/search/1?q=鱼块',
    
    # 蔬菜
    '西兰花': 'https://s.meituan.com/v1/mss_126c814fe3f743a29d82aa9e962d2fc2/search/1?q=西兰花',
    '青菜': 'https://s.meituan.com/v1/mss_126c814fe3f743a29d82aa9e962d2fc2/search/1?q=青菜',
    '白菜': 'https://s.meituan.com/v1/mss_126c814fe3f743a29d82aa9e962d2fc2/search/1?q=白菜',
    '大白菜': 'https://s.meituan.com/v1/mss_126c814fe3f743a29d82aa9e962d2fc2/search/1?q=大白菜',
    '菠菜': 'https://s.meituan.com/v1/mss_126c814fe3f743a29d82aa9e962d2fc2/search/1?q=菠菜',
    '莴笋': 'https://s.meituan.com/v1/mss_126c814fe3f743a29d82aa9e962d2fc2/search/1?q=莴笋',
    '胡萝卜': 'https://s.meituan.com/v1/mss_126c814fe3f743a29d82aa9e962d2fc2/search/1?q=胡萝卜',
    '土豆': 'https://s.meituan.com/v1/mss_126c814fe3f743a29d82aa9e962d2fc2/search/1?q=土豆',
    '茄子': 'https://s.meituan.com/v1/mss_126c814fe3f743a29d82aa9e962d2fc2/search/1?q=茄子',
    '豆芽': 'https://s.meituan.com/v1/mss_126c814fe3f743a29d82aa9e962d2fc2/search/1?q=豆芽',
    '花菜': 'https://s.meituan.com/v1/mss_126c814fe3f743a29d82aa9e962d2fc2/search/1?q=花菜',
    '娃娃菜': 'https://s.meituan.com/v1/mss_126c814fe3f743a29d82aa9e962d2fc2/search/1?q=娃娃菜',
    '菜心': 'https://s.meituan.com/v1/mss_126c814fe3f743a29d82aa9e962d2fc2/search/1?q=菜心',
    '油麦菜': 'https://s.meituan.com/v1/mss_126c814fe3f743a29d82aa9e962d2fc2/search/1?q=油麦菜',
    '上海青': 'https://s.meituan.com/v1/mss_126c814fe3f743a29d82aa9e962d2fc2/search/1?q=上海青',
    '春菜': 'https://s.meituan.com/v1/mss_126c814fe3f743a29d82aa9e962d2fc2/search/1?q=春菜',
    '芹菜': 'https://s.meituan.com/v1/mss_126c814fe3f743a29d82aa9e962d2fc2/search/1?q=芹菜',
    '青椒': 'https://s.meituan.com/v1/mss_126c814fe3f743a29d82aa9e962d2fc2/search/1?q=青椒',
    '西红柿': 'https://s.meituan.com/v1/mss_126c814fe3f743a29d82aa9e962d2fc2/search/1?q=西红柿',
    '番茄': 'https://s.meituan.com/v1/mss_126c814fe3f743a29d82aa9e962d2fc2/search/1?q=番茄',
    '笋': 'https://s.meituan.com/v1/mss_126c814fe3f743a29d82aa9e962d2fc2/search/1?q=笋',
    '竹笋': 'https://s.meituan.com/v1/mss_126c814fe3f743a29d82aa9e962d2fc2/search/1?q=竹笋',
    '木耳': 'https://s.meituan.com/v1/mss_126c814fe3f743a29d82aa9e962d2fc2/search/1?q=木耳',
    '香菇': 'https://s.meituan.com/v1/mss_126c814fe3f743a29d82aa9e962d2fc2/search/1?q=香菇',
    '海带': 'https://s.meituan.com/v1/mss_126c814fe3f743a29d82aa9e962d2fc2/search/1?q=海带',
    
    # 豆制品
    '豆腐': 'https://s.meituan.com/v1/mss_126c814fe3f743a29d82aa9e962d2fc2/search/1?q=豆腐',
    '豆干': 'https://s.meituan.com/v1/mss_126c814fe3f743a29d82aa9e962d2fc2/search/1?q=豆干',
    '香干': 'https://s.meituan.com/v1/mss_126c814fe3f743a29d82aa9e962d2fc2/search/1?q=香干',
    '白干': 'https://s.meituan.com/v1/mss_126c814fe3f743a29d82aa9e962d2fc2/search/1?q=白干',
    '方干': 'https://s.meituan.com/v1/mss_126c814fe3f743a29d82aa9e962d2fc2/search/1?q=豆腐干',
    '鸡蛋干': 'https://s.meituan.com/v1/mss_126c814fe3f743a29d82aa9e962d2fc2/search/1?q=鸡蛋干',
    '腐竹': 'https://s.meituan.com/v1/mss_126c814fe3f743a29d82aa9e962d2fc2/search/1?q=腐竹',
    
    # 蛋类
    '鸡蛋': 'https://s.meituan.com/v1/mss_126c814fe3f743a29d82aa9e962d2fc2/search/1?q=鸡蛋',
    
    # 调料（常用）
    '大豆油': 'https://s.meituan.com/v1/mss_126c814fe3f743a29d82aa9e962d2fc2/search/1?q=大豆油',
    '食用油': 'https://s.meituan.com/v1/mss_126c814fe3f743a29d82aa9e962d2fc2/search/1?q=食用油',
    '盐': 'https://s.meituan.com/v1/mss_126c814fe3f743a29d82aa9e962d2fc2/search/1?q=盐',
    '生抽': 'https://s.meituan.com/v1/mss_126c814fe3f743a29d82aa9e962d2fc2/search/1?q=生抽',
    '老抽': 'https://s.meituan.com/v1/mss_126c814fe3f743a29d82aa9e962d2fc2/search/1?q=老抽',
    '蒜': 'https://s.meituan.com/v1/mss_126c814fe3f743a29d82aa9e962d2fc2/search/1?q=大蒜',
    '蒜子': 'https://s.meituan.com/v1/mss_126c814fe3f743a29d82aa9e962d2fc2/search/1?q=大蒜',
    '葱': 'https://s.meituan.com/v1/mss_126c814fe3f743a29d82aa9e962d2fc2/search/1?q=葱',
    '姜': 'https://s.meituan.com/v1/mss_126c814fe3f743a29d82aa9e962d2fc2/search/1?q=姜',
}

def get_ingredient_link(ingredient_name):
    """获取食材的购买链接"""
    # 先尝试精确匹配
    if ingredient_name in INGREDIENT_LINKS:
        return INGREDIENT_LINKS[ingredient_name]
    
    # 模糊匹配
    for key in INGREDIENT_LINKS:
        if key in ingredient_name or ingredient_name in key:
            return INGREDIENT_LINKS[key]
    
    # 如果都没匹配到，返回通用搜索链接
    return f'https://s.meituan.com/v1/mss_126c814fe3f743a29d82aa9e962d2fc2/search/1?q={ingredient_name}'

def extract_ingredients(content):
    """从菜品内容中提取食材"""
    import re
    
    ingredients = []
    
    # 查找配料/原料部分
    if '## 配料' in content or '## 原料' in content:
        # 提取配料列表
        pattern = r'##\s*(?:配料|原料)[：:]\s*\n(.*?)(?=\n##|\Z)'
        match = re.search(pattern, content, re.DOTALL)
        
        if match:
            ingredients_text = match.group(1)
            # 提取每一行的食材（去掉markdown的列表符号）
            lines = ingredients_text.strip().split('\n')
            for line in lines:
                line = line.strip()
                if line and line.startswith('-'):
                    ingredient = line[1:].strip()
                    # 去掉数量信息
                    ingredient = re.sub(r'\d+g?\s*', '', ingredient)
                    ingredient = re.sub(r'\d+ml?\s*', '', ingredient)
                    if ingredient:
                        ingredients.append(ingredient)
    
    return ingredients

