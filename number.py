import random
import math

while True:
    selectNumber=input("難易度を選択してください\n1:簡単 2:難しい")
    if selectNumber=="1":
        break
    elif selectNumber=="2":
        break
    else:
        print("1または2を入力してください")

while True:
    min=input("最小値を入力してください")
    max=input("最大値を入力してください")

    if min>max:
        print("最小値は最大値よりも大きい値にしてください")
        continue
    break


randomNumber=random.randint(int(min),int(max))

if selectNumber=="1":
    print("簡単")
    while True:
        guessNumber=input("予想値を入力してください")
        if int(guessNumber)==randomNumber:
            print("正解")
            break
        elif int(guessNumber)<randomNumber:
            print("もっと大きい")
        else:
            print("もっと小さい")
elif selectNumber=="2":
    print("難しい")
    limitNum=math.floor(math.sqrt(int(max)))
    for i in range(int(min),limitNum):
        guessNumber=input("予想値を入力してください")
        if int(guessNumber)==randomNumber:
            print("正解")
            break
        elif int(guessNumber)<randomNumber:
            print("もっと大きい")
        else:
            print("もっと小さい")