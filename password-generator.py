"""
🔥 随机密码生成工具 by GitHub-Copilot
功能：
1. 生成指定长度的密码
2. 可自定义包含大写字母/数字/特殊符号
3. 避免相似字符（如1,l,I）
"""

import random
import argparse

def generate_password(length=12, use_upper=True, use_digits=True, use_symbols=True):
    # 基础字符集
    lower = 'abcdefghjkmnpqrstuvwxyz'  # 排除 l, i 等易混淆字符
    upper = 'ABCDEFGHJKMNPQRSTUVWXYZ'  # 排除 I
    digits = '23456789'                # 排除 0,1
    symbols = '!@#$%^&*()_+-='
    
    # 组合可用字符
    chars = lower
    if use_upper: chars += upper
    if use_digits: chars += digits
    if use_symbols: chars += symbols
    
    # 至少包含一个每个选定的字符类型
    password = []
    if use_upper: password.append(random.choice(upper))
    if use_digits: password.append(random.choice(digits))
    if use_symbols: password.append(random.choice(symbols))
    
    # 填充剩余长度
    remaining = length - len(password)
    password += random.choices(chars, k=remaining)
    
    # 打乱顺序
    random.shuffle(password)
    return ''.join(password)

if __name__ == "__main__":
    # 命令行参数解析
    parser = argparse.ArgumentParser(description='生成高强度随机密码')
    parser.add_argument('-l', '--length', type=int, default=12, help='密码长度')
    parser.add_argument('--no-upper', action='store_false', dest='use_upper', help='禁用大写字母')
    parser.add_argument('--no-digits', action='store_false', dest='use_digits', help='禁用数字')
    parser.add_argument('--no-symbols', action='store_false', dest='use_symbols', help='禁用符号')
    args = parser.parse_args()
    
    # 生成并输出密码
    password = generate_password(
        length=args.length,
        use_upper=args.use_upper,
        use_digits=args.use_digits,
        use_symbols=args.use_symbols
    )
    print(f"🔒 生成的密码：{password}")