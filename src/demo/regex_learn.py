"""
re 基本用法：match / search / 分组获取

- match  : 只从字符串开头匹配
- search : 在整个字符串里找第一次匹配
- group  : 取整段或某个捕获组
"""

import re


def demo_match_vs_search() -> None:
    text = "hello world 2024"

    # match：必须从开头开始；开头对不上就失败
    m1 = re.match(r"world", text)
    m2 = re.match(r"hello", text)
    print("match 'world':", m1)          # None
    print("match 'hello':", m2.group())  # hello

    # search：全文找第一次出现
    s1 = re.search(r"world", text)
    print("search 'world':", s1.group())  # world
    print("span:", s1.span())             # (6, 11) 起止下标


def demo_groups() -> None:
    text = "Alice is 20 years old"

    # () 是捕获组，从 1 开始编号；group(0) 是整段匹配
    pattern = r"(\w+) is (\d+) years old"
    m = re.search(pattern, text)
    assert m is not None

    print("group(0) 整段:", m.group(0))   # Alice is 20 years old
    print("group(1) 姓名:", m.group(1))   # Alice
    print("group(2) 年龄:", m.group(2))   # 20
    print("groups() 元组:", m.groups())   # ('Alice', '20')
    print("group(1, 2):", m.group(1, 2))  # ('Alice', '20')


def demo_named_groups() -> None:
    text = "email: zjremo@example.com"

    # (?P<name>...) 命名分组，可读性更好
    pattern = r"email:\s*(?P<user>\w+)@(?P<domain>[\w.]+)"
    m = re.search(pattern, text)
    assert m is not None

    print("user:", m.group("user"))       # zjremo
    print("domain:", m.group("domain"))   # example.com
    print("groupdict:", m.groupdict())    # {'user': 'zjremo', 'domain': 'example.com'}


def demo_findall_finditer() -> None:
    text = "a1 b22 c333"

    # findall：有分组时返回各组；多个组则返回元组列表
    print("findall 无分组:", re.findall(r"\d+", text))           # ['1', '22', '333']
    print("findall 有分组:", re.findall(r"([a-z]+)(\d+)", text))  # [('a','1'), ...]

    # finditer：返回 Match 对象迭代器，适合既要内容和位置
    for m in re.finditer(r"([a-z]+)(\d+)", text):
        print(f"  {m.group(1)} -> {m.group(2)}, span={m.span()}")


def demo_compile_flags() -> None:
    text = "Hello\nWORLD"

    # 预编译：同一模式多次用时更清晰
    pat = re.compile(r"hello", re.IGNORECASE)
    print("IGNORECASE:", pat.search(text).group())  # Hello

    # re.DOTALL: . 也能匹配换行
    pat2 = re.compile(r"Hello.*WORLD", re.DOTALL)
    print("DOTALL:", pat2.search(text).group())


def demo_sub_split() -> None:
    text = "tel: 138-0000-1111, 139-2222-3333"

    # sub：替换
    masked = re.sub(r"(\d{3})-(\d{4})-(\d{4})", r"\1-****-\3", text)
    print("sub:", masked)

    # split：按模式切开
    print("split:", re.split(r"[,:\s]+", "a, b: c  d"))


if __name__ == "__main__":
    print("=== match vs search ===")
    demo_match_vs_search()

    print("\n=== groups ===")
    demo_groups()

    print("\n=== named groups ===")
    demo_named_groups()

    print("\n=== findall / finditer ===")
    demo_findall_finditer()

    print("\n=== compile / flags ===")
    demo_compile_flags()

    print("\n=== sub / split ===")
    demo_sub_split()
