import random


class ItemBox():
    class Color():
        RED = 'RED'
        GREEN = 'GREEN'
        BLUE = 'BLUE'

    red_count = 22
    green_count = 26
    blue_count = 52

    def __init__(self):
        self.box = [0] * 100
        self.shuflebox()

    def shuflebox(self):
        red_items = [self.Color.RED] * self.red_count
        green_items = [self.Color.GREEN] * self.green_count
        blue_items = [self.Color.BLUE] * self.blue_count
        index = 0
        while index < 100:
            choice = random.randint(0, 2)
            if choice == 0 and red_items != []:
                self.box[index] = red_items.pop()
                index += 1

            if choice == 1 and green_items != []:
                self.box[index] = green_items.pop()
                index += 1

            if choice == 2 and blue_items != []:
                self.box[index] = blue_items.pop()
                index += 1


if __name__ == "__main__":
    result = ItemBox()
    result.shuflebox()
    print(result.box)

# Есть группа из 100 предметов.
# Предметы могут быть синего, зелёного и красного цвета.
# Известно, что предметов синего цвета сильно больше,
# чем предметов зелёного цвета, а предметов зелёного цвета
# немного больше, чем предметов красного цвета.
# Напишите сервис, который будет принимать номер
# предмета и пытаться угадать его цвет.
# Логику работы сервиса определите самостоятельно.

# all = 100
# blue > green    blue = 2 * green
# green > red     green = 1.2 * red
# blue + green + red = all
# red = 22
# green = 26
# blue = 52
