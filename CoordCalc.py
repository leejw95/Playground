# CoordCalc.py

def Add(Coordinate1, Coordinate2):

    __isCoordinate([Coordinate1, Coordinate2])

    x = Coordinate1[0] + Coordinate2[0]
    y = Coordinate1[1] + Coordinate2[1]

    return [x, y]
    # end of def Add():


def Subtract(Coordinate1, Coordinate2):     # another def named distance and exactly same functionality?

    __isCoordinate([Coordinate1, Coordinate2])

    x = Coordinate1[0] - Coordinate2[0]
    y = Coordinate1[1] - Coordinate2[1]

    return [x, y]
    # end of def Subtract():


def FlipX(Coordinate):
    __isCoordinate(Coordinate)
    return [-Coordinate[0], Coordinate[1]]


def FlipY(Coordinate):
    __isCoordinate(Coordinate)
    return [Coordinate[0], -Coordinate[1]]


def FlipXY(Coordinate):
    __isCoordinate(Coordinate)
    return [-Coordinate[0], -Coordinate[1]]


def __isCoordinate(ListOfCoordinates):

    for element in ListOfCoordinates:
        assert isinstance(element, list), 'Expected list.'
        assert len(element) == 2, 'Expected two element. But {}.'.format(len(element))
        for xy in element:
            assert isinstance(xy, (int, long, float)), 'Expected number. But {}.'.format(xy)

    # end of def isCoordinate(x):


# testbench
if __name__ == '__main__':

    value1 = [1, 3]
    value2 = [2, 5]

    results = Add(value1, value2)
    print(results)
