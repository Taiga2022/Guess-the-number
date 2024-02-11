import math
import random

class Level:
    def __init__(self):
        self.level=None

    def select(self):
        while True:
            self.level=input("難易度を選択してください\n1:簡単 2:難しい")
            if self.level=="1":
                break
            if self.level=="2":
                break
            print("1または2を入力してください")

class Range:
    def __init__(self):
        self.min=None
        self.max=None

    def input(self):
        while True:
            self.min=int(input("最小値を入力してください"))
            self.max=int(input("最大値を入力してください"))
            if self.min>self.max:
                print("最小値は最大値よりも大きい値にしてください")
                continue
            break

class EasyAnswer:
    def __init__(self, min_val, max_val):
        self.answer = random.randint(min_val, max_val)

    def check(self):
        while True:
            guess_number = input("予想値を入力してください")
            if int(guess_number) == self.answer:
                print("正解")
                break
            if int(guess_number) < self.answer:
                print("もっと大きい")
            else:
                print("もっと小さい")

class HardAnswer:
    def __init__(self, min_val, max_val):
        self.answer = random.randint(min_val, max_val)
        self.min=int(min_val)
        self.limit=math.ceil(math.sqrt(int(max_val)))

    def check(self):
        for i in range(self.min,self.limit):
            guess_number = input("予想値を入力してください")
            if int(guess_number)==self.answer:
                print("正解")
                break
            if int(guess_number)<self.answer:
                print("もっと大きい")
            else:
                print("もっと小さい")

class Quiz:
    def __init__(self):
        self.level=Level()
        self.range=Range()

    def start(self):
        self.level.select()
        self.range.input()
        if self.level.level=="1":
            EasyAnswer(self.range.min,self.range.max).check()
        elif self.level.level=="2":
            HardAnswer(self.range.min,self.range.max).check()


if __name__ == '__main__':
    quiz=Quiz()
    quiz.start()