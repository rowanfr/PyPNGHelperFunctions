import numpy
import png

a = numpy.array([[[255,0,0,0],[0,255,0,255]],[[255,0,0,0],[0,0,255,0]]], dtype=numpy.uint8)
#RGBA
print(str(a.shape))
f = open('swatch.png', 'wb')
w = png.Writer(2, 2, greyscale=False, alpha=True)
#png.Writer(First Row Size, Number of Rows)
print(numpy.copy(a).reshape(a.shape[0],(a.shape[1]*a.shape[2])))
w.write(f, numpy.copy(a).reshape(a.shape[0],(a.shape[1]*a.shape[2])))
#This partially flattens the array to abide by the format desired by PyPng.
#In essence we reshape to # of rows, RGBA in those rows CONTINUOUSLY
#The reason why we don't define our array originally in this manner is that it's easier for me to think about in 3Dimensions (but their shouldn't be any substantial effect from this)
f.close()