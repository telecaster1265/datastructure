print("세 정수의 최댓값을 구합니다.")
a = int(input("정수 a의 값을 입력하세요: "))
b = int(input("정수 b의 값을 입력하세요: "))
c = int(input("정수 c의 값을 입력하세요: "))

max_value = a
if b > max_value:
    max_value = b
if c > max_value:
    max_value = c

print(f"최댓값은 {max_value}입니다.")
