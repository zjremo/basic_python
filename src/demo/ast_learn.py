import ast

list_str = "[1, 2, 3, 4]"
"""
    Evaluate an expression node or a string containing only a Python
    expression.  The string or node provided may only consist of the following
    Python literal structures: strings, bytes, numbers, tuples, lists, dicts,
    sets, booleans, and None.
"""
l = ast.literal_eval(list_str)
print(type(l))
print(f"l: {l}")

d = '{"a": 1, "b": 2}'
d = ast.literal_eval(d)
print(type(d))
print(f"d: {d}")
