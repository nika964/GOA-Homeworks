data = [42, "hello", 3.14, True, "world", False, "python", 100]


for item in data:
    if isinstance(item, str):
        upper_str = item.upper()
        print(upper_str[-3:])
