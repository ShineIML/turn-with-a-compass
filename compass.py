def direction(facing: str, turn: int):

    min_v = -1080
    max_v = 1080

    compass = ["W", "NW", "N", "NE", "E", "SE", "S", "SW"]

    if turn < min_v or turn > max_v or facing not in compass or turn % 45 != 0:
        raise ValueError
    
    dir_counter = turn // 45
    
    for side in compass:
        if side == facing:
            idx = compass.index(side)
            return compass[(idx+dir_counter) % (len(compass))]

def run_tests():
    print(direction("S", 180))
    print(direction("SE", -45))
    print(direction("W", 495))
    print(direction("W",  18000))
    print(direction("WSAD",  18000))

run_tests()