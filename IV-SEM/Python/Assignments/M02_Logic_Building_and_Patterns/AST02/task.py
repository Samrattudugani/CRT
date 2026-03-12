def reverse_number(n: int) -> int:
    sign = -1 if n < 0 else 1
    n = abs(n)
    reversed_num = int(str(n)[::-1])
    return sign * reversed_num

if __name__ == "__main__":
    n = int(input())
    print(reverse_number(n))