"""
1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и
метод running (запуск). Атрибут реализовать как приватный.
В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов,
и при его нарушении выводить соответствующее сообщение и завершать скрипт.
"""

import time


class TrafficLight:
    __color = ['\033[31m', '\033[33m', '\033[32m']

    def running(self):
        while True:
            print(self.__color[0], "Stop")
            time.sleep(7)
            print(self.__color[1], "Wait")
            time.sleep(2)
            print(self.__color[2], "Go\n")
            time.sleep(7)


a = TrafficLight()
a.running()
