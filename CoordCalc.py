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


def getXYCoords_MinY(Coordinates):

    XYList = []
    referenceMinY = None

    for XY in Coordinates:
        if referenceMinY is None:         # initial
            referenceMinY = XY[1]
            XYList.append(XY)
        else:
            if XY[1] < referenceMinY:     # New MinimumY
                referenceMinY = XY[1]
                XYList = [XY]
            elif XY[1] == referenceMinY:  # Same with MinimumY
                XYList.append(XY)
            else:                         # bigger than MinimumY
                pass
    return XYList


def getXYCoords_MinX(Coordinates):

    XYList = []
    referenceMinX = None

    for XY in Coordinates:
        if referenceMinX is None:         # initial
            referenceMinX = XY[0]
            XYList.append(XY)
        else:
            if XY[0] < referenceMinX:     # New MinimumX
                referenceMinX = XY[0]
                XYList = [XY]
            elif XY[0] == referenceMinX:  # Same with MinimumX
                XYList.append(XY)
            else:                         # bigger than MinimumX
                pass
    return XYList


def getXYCoords_MaxX(Coordinates):

    XYList = []
    referenceMaxX = None

    for XY in Coordinates:
        if referenceMaxX is None:         # initial
            referenceMaxX = XY[0]
            XYList.append(XY)
        else:
            if XY[0] > referenceMaxX:     # New MaximumX
                referenceMaxX = XY[0]
                XYList = [XY]
            elif XY[0] == referenceMaxX:  # Same with MaximumX
                XYList.append(XY)
            else:                         # smaller than MaximumX
                pass
    return XYList


def getXYCoords_MaxY(Coordinates):

    XYList = []
    referenceMaxY = None

    for XY in Coordinates:
        if referenceMaxY is None:         # initial
            referenceMaxY = XY[1]
            XYList.append(XY)
        else:
            if XY[1] > referenceMaxY:     # New MaximumY
                referenceMaxY = XY[1]
                XYList = [XY]
            elif XY[1] == referenceMaxY:  # Same with MaximumY
                XYList.append(XY)
            else:                         # smaller than MaximumY
                pass
    return XYList


# testbench
if __name__ == '__main__':

    # value1 = [1, 3]
    # value2 = [2, 5]
    #
    # results = Add(value1, value2)

    XYCoordinates = [[3,5], [1,5], [-1,5], [4,5], [0,-1], [0,-1], [-3,-1]]
    results = getXYCoords_MinY(XYCoordinates)

    print(results)
