# coding: utf8
import random


def figureGen():  # Эти генераторы для файла. Тут не важно как склоняются слова, программа и так читает только 1 букву
    color_list = ['синий', 'зеленый', 'красный']
    gradient_list = ['полосатый', 'пустой', 'заполненный']
    form_list = ['ромб', 'овал', 'фасоль']
    return str(random.randint(1, 3)) + ' ' + random.choice(color_list) + ' ' + random.choice(
        gradient_list) + ' ' + random.choice(form_list)


def fileGen():
    f = open('set.txt', 'w')
    for i in range(12):
        f.write(figureGen() + '\n')
    f.close()
