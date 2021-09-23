import random


def com_action(start_num):
    if start_num >= 30:
        return -1

    if start_num + 3 >= 31:
        return 30

    random_num = random.randint(1, 3)
    end_num = start_num + random_num

    return end_num


def my_action(start_num):
    if start_num >= 30:
        return -1

    count = 0

    while True:
        count = count + 1

        if count > 1:
            print("숫자를 잘못 입력했습니다. 다시 입력해주세요.")

        my = input("My turn - 숫자를 입력하세요 :")
        my_split_list = my.split(" ")
        end_num = int(my_split_list[-1])

        if len(my_split_list) > 3 or len(my_split_list) < 1:
            continue

        flag = True

        for i in range(len(my_split_list)):
            if (start_num + i + 1) != int(my_split_list[i]):
                flag = False
                break

        if not flag:
            continue
        else:
            break

    return end_num


def br31():
    print("베스킨라빈스 31 게임 시작!")

    number = 0

    while True:
        number = com_action(number)

        if number == -1:
            print("게임종료")
            print("나 승리!")
            break
        else:
            print("컴퓨터 :", number)

        number = my_action(number)

        if number == -1:
            print("게임종료")
            print("컴퓨터 승리!")
            break
        else:
            print("나 :", number)


br31()
