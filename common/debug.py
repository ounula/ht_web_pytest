# -*- coding: UTF-8 –*-
# author: zhh
# time: 2020/7/2 14:19


def function_practise():
    win_count = 0
    count = 0
    while True:
        try:
            user = input("输入：")  # 石头（0）／剪刀（1）／布（2）／退出（3）
            user = int(user)
            assert user in [0, 1, 2, 3]
            import random
            cpu = random.randint(0, 2)
            if user == 0:
                print('你赢了') if cpu == 2 else print("你输了")
                win_count += 1 if cpu == 2 else win_count
            elif user == 1:
                win_count += 1 if cpu == 0 else win_count
            elif user == 2:
                win_count += 1 if cpu == 1 else win_count
            count += 1
            if user == 3:
                print("胜率：%.2f%%" % (win_count/count))
                break
        except AssertionError:
            print("输入错误")


if __name__ == '__main__':
    function_practise()
