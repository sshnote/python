# 3.8 입력 받은 세 자리 정수를 역순으로 출력하는 프로그램

num = int(input("세 자리 정수를 입력하시오 : ")) # 세 자리 정수 입력 받기

num_100 = num // 100 # 백의 자리
num_10 = (num - num_100 * 100) // 10 # 십의 자리
num_1 = (num - num_100 * 100) % 10 # 일의 자리

print(f'{num_1}') # 일의 자리 출력
print(f'{num_10}') # 십의 자리 출력
print(f'{num_100}') # 백의 자리 출력
