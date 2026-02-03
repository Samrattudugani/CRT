def Student_Grade_System(name: str, n1: int, n2: int, n3: int) -> str:
    avg = (n1 + n2 + n3) / 3
    avg = int(avg * 100) / 100   # truncate to 2 decimals

    if avg >= 40:
        status = "Pass"
    else:
        status = "fail"

    return f"Average grade: {avg}, Status: {status}"

if __name__ == '__main__':
    data = input().split()
    name = data[0]
    n1, n2, n3 = map(int, data[1:])
    print(Student_Grade_System(name, n1, n2, n3))    