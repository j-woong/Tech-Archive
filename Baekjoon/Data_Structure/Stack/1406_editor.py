import sys

# 현재 폴더에 있는 input.txt를 표준 입력(stdin)으로 연결합니다.
# sys.stdin = open("input.txt", "r")

# 초기 문자열 읽기
Left = list(sys.stdin.readline().strip())
Right = []
# 입력값 읽기
n = int(sys.stdin.readline())

for _ in range(n):
    command = sys.stdin.readline().split()
    
    if command[0] == "L":
        if Left:
            char = Left.pop()
            Right.append(char)
        else:
            continue

    elif command[0] == "D":
        if Right:        
            char = Right.pop()
            Left.append(char)
        else:
            continue
    elif command[0] == "B":
        if Left:
            Left.pop()

    else:
        Left.append(command[1])

sys.stdout.write("".join(Left) + "".join(reversed(Right)) + "\n")