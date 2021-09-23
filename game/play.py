def rsp(x):
    import random
    computer = random.randint(0, 2)

    if computer == 0:
        computer_rsp = "가위"
    elif computer == 1:
        computer_rsp = "바위"
    else:
        computer_rsp = "보"
    print("컴퓨터 :", computer_rsp)

    if x == "가위":
        if computer_rsp == "바위":
            print("컴퓨터 승리")
        elif computer_rsp == "가위":
            print("무승부")
        else:
            print("나 승리")
    elif x == "바위":
        if computer_rsp == "바위":
            print("무승부")
        elif computer_rsp == "가위":
            print("나 승리")
        else:
            print("컴퓨터 승리")
    else:
        if computer_rsp == "바위":
            print("나 승리")
        elif computer_rsp == "가위":
            print("컴퓨터 승리")
        else:
            print("무승부")


my = input("가위 바위 보 :")
print("나 :", my)

rsp(my)
