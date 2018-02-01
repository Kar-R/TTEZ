import numpy as np
import matplotlib.pyplot as plt
import shapefile

sf = shapefile.Reader('toronto_shape/CENTRELINE_WGS84.shp')
shapes = sf.shapes()
plt.figure()
for shape in sf.shapeRecords():
    x = [i[0] for i in shape.shape.points[:]]
    y = [i[1] for i in shape.shape.points[:]]
    plt.plot(x,y)
plt.show()
