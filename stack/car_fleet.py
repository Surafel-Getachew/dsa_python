from cmath import log


def car_fleet(target, position, speed):
    fleetMap = {}
    for i in range(len(position)):
        add = position[i] + speed[i]
        fleetMap[add] = 1 + fleetMap.get(add, 0)
    return len(fleetMap)


target = 12
position = [10, 8, 0, 5, 3]
speed = [2, 4, 1, 1, 3]

print(car_fleet(target, position, speed))
