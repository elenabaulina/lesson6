from time import sleep
class TrafficLight:
    __color = ["Red", "Yellow", "Green"]
    def running(self):
        s = 0
        while s != 3:
            print(TrafficLight.__color[s])
            if s == 0:
                sleep(7)
            elif s == 1:
                sleep(2)
            elif s == 2:
                sleep(15)
            s += 1
t = TrafficLight()
t.running()


class Road:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width
    def sum_road(self):
        sum_road = self.__length * self.__width * 25 * 5 // 1000
        print(sum_road)
r = Road(20,5000)
r.sum_road()
