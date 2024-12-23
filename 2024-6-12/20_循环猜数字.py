# 你任意输入一个100以内的整数，如果比目标小了，就说猜小了，比目标大了就是猜大了，如果正好就说猜对了，并且输出您猜了多少次
import random

target_number = random.randint(1, 100)
guess = 0
tries = 0

while guess != target_number:
    guess = int(input("猜一个1到100之间的数字: "))
    tries += 1

    if guess < target_number:
        print("猜小了")
    elif guess > target_number:
        print("猜大了")
    else:
        print("恭喜，猜对了！")
        print("您猜了", tries, "次")
