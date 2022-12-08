import numpy
import png
import PyPNGHelperFunctions as PNGHelper
iData = PNGHelper.importPNGtoNumpy('PyPNGTest.png')
#For some fucking reason one uses filename to indicate physical file's name and file tag to use a seperate library to get something online
#iData is image data, not the reader

#image data is held as a tuple of (Row, Column, Generator for bytearray of data, PNG metadata dictionary)
#Generator generates multiple bytearrays that represent each row stacked on top of each other starting at the top and then going dows
print(iData)

for value in iData:
    print(value)
print(iData[3].get('planes'))
#for value in iData[2]:
#    print(value)
#!!!Generators can only generate their variables once so doing this before list yields an empty list
host = numpy.arange(iData[0]*iData[1]).reshape(iData[1],iData[0])#Reshape works by column then row
dataMap = list(iData[2])
print(dataMap)
image_3d = PNGHelper.ThreeDimensionImageFromBytearray(dataMap, iData[3].get('planes'))#// are integer divisions
print(image_3d)
print(image_3d.dtype)


f = open('numpyTestOut.png', 'wb')
w = png.Writer(numpy.size(image_3d,1), numpy.size(image_3d,0), greyscale=False, alpha=True)

print(numpy.copy(image_3d).reshape(image_3d.shape[0],(image_3d.shape[1]*image_3d.shape[2])))
w.write(f, numpy.copy(image_3d).reshape(image_3d.shape[0],(image_3d.shape[1]*image_3d.shape[2])))

f.close()