# CoordCalc.py

def Add(Coordinate1, Coordinate2):

    x = Coordinate1[0] + Coordinate2[0]
    y = Coordinate1[1] + Coordinate2[1]

    return [x, y]


def Subtract(Coordinate1, Coordinate2):     # another def named distance and exactly same functionality?

    x = Coordinate1[0] - Coordinate2[0]
    y = Coordinate1[1] - Coordinate2[1]

    return [x, y]


def FlipX(Coordinate):
    return [-Coordinate[0], Coordinate[1]]


def FlipY(Coordinate):
    return [Coordinate[0], -Coordinate[1]]


def FlipXY(Coordinate):
    return [-Coordinate[0], -Coordinate[1]]


def __isCoordinate(ListOfCoordinates):

    for element in ListOfCoordinates:
        assert isinstance(element, list), 'Expected list. But {}'.format(type(element))
        assert len(element) == 2, 'Expected two element. But {}.'.format(len(element))
        for xy in element:
            assert isinstance(xy, (int, long, float)), 'Expected number. But {}.'.format(xy)

    # end of def isCoordinate(x):


def FlipXs(Coordinates):

    tmpXYs = []
    for XY in Coordinates:
        print XY
        tmpXYs.append([-XY[0], XY[1]])
    return tmpXYs


def FlipYs(Coordinates):

    tmpXYs = []
    for XY in Coordinates:
        print XY
        tmpXYs.append([XY[0], -XY[1]])
    return tmpXYs


def FlipXYs(Coordinates):

    tmpXYs = []
    for XY in Coordinates:
        print XY
        tmpXYs.append([-XY[0], -XY[1]])
    return tmpXYs


def MinMaxXY(Coordinates):
    x_list, y_list = [], []
    for XY in Coordinates:
        x_list.append(XY[0])
        y_list.append(XY[1])

    return min(x_list), min(y_list), max(x_list), max(y_list)


# testbench
if __name__ == '__main__':

    # value1 = [1, 3]
    # value2 = [2, 5]
    #
    # results = Add(value1, value2)

    XYCoordinates = [[3,5], [1,5], [-1,5], [4,5]]
    results = FlipXs(XYCoordinates)

    print(results)
