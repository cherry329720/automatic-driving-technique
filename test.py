def fibonacci(n):
    """生成斐波那契数列的前n项"""
    a, b = 0, 1
    sequence = []
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

print("斐波那契数列前20项:", fibonacci(20))