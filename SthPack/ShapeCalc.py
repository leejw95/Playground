from shapely.geometry import Polygon, box, MultiPolygon
import matplotlib.pyplot as plt
import shapely.ops as so


def _Boundary2Polygon(Boundary):
    PolygonList = []
    for XYs in Boundary['_XYCoordinates']:
        PolygonList.append(
            box(XYs[0] - Boundary['_XWidth'] / 2,     # minX
                XYs[1] - Boundary['_YWidth'] / 2,     # minY
                XYs[0] + Boundary['_XWidth'] / 2,     # maxX
                XYs[1] + Boundary['_YWidth'] / 2)     # maxY
        )
    return MultiPolygon(PolygonList)


def _Polygon2BoundaryElement(MultiPolygon):

    if len(MinMaxXYList) == 0:
        return None
    else:
        BoundaryElement = dict(_XWidth=(MinMaxXYList[0][2] - MinMaxXYList[0][0]),
                               _YWidth=(MinMaxXYList[0][3] - MinMaxXYList[0][1]),
                               _XYCoordinates=[])
        for Obj in MinMaxXYList:
            assert (Obj[2] - Obj[0]) == BoundaryElement['_XWidth']
            assert (Obj[3] - Obj[1]) == BoundaryElement['_YWidth']
            BoundaryElement['_XYCoordinates'].append(
                [(Obj[2] + Obj[0]) / 2.,
                 (Obj[3] + Obj[1]) / 2.])
        return BoundaryElement


if __name__ == '__main__':
    plt.rcParams["figure.figsize"] = [7.00, 3.50]
    plt.rcParams["figure.autolayout"] = True


    b1 = dict()
    b1['_XWidth'] = 1000
    b1['_YWidth'] = 60
    b1['_XYCoordinates'] = [[0,0]]

    b2 = dict()
    b2['_XWidth'] = 20
    b2['_YWidth'] = 80
    b2['_XYCoordinates'] = [[0,0], [100,0], [200,0], [300,0]]

    p1 = _Boundary2Polygon(b1)
    p2 = _Boundary2Polygon(b2)

    p3 = p1.difference(p2)


    multipolygon1 = p3

    print(multipolygon1)
    for Polygon in multipolygon1.geoms:
        print(Polygon)


    ''' plot '''
    fig, axs = plt.subplots()
    axs.set_aspect('equal', 'datalim')

    for geom in multipolygon1.geoms:
        xs, ys = geom.exterior.xy
        axs.fill(xs, ys, alpha=0.5, fc='r', ec='none')

    plt.show()