#Requisites for these helper functions are Numpy and PyPNG
#Source for many function ideas: https://ciechanow.ski/alpha-compositing/
#
import png
import numpy

#This is used to convert the input image into an easier to understand format
def importPNGto3DNumpy(filename):
    imageData = png.Reader(filename=filename).asDirect()
    image_3d = ThreeDimensionImageFromBytearray(imageData[2], imageData[3].get('planes'), imageData[3].get('bitdepth'))
    return image_3d

def export3DNumpytoPNG(image_3d, filename):
    f = open(filename, 'wb')  

    match numpy.size(image_3d,2):
        case 1:
            w = png.Writer(numpy.size(image_3d,1), numpy.size(image_3d,0), greyscale=True, alpha=False)
        case 2:
            w = png.Writer(numpy.size(image_3d,1), numpy.size(image_3d,0), greyscale=True, alpha=True)
        case 3:
            w = png.Writer(numpy.size(image_3d,1), numpy.size(image_3d,0), greyscale=False, alpha=False)
        case 4:
            w = png.Writer(numpy.size(image_3d,1), numpy.size(image_3d,0), greyscale=False, alpha=True)
        case _:
            raise ValueError("The value provided from the channel dimension is " + numpy.size(image_3d,2) + " which is outside the range of acceptable values")
    
    
    image_2d = semiFlatten3DNumpyArray(image_3d)
    w.write(f, image_2d)

    f.close()

#This is used to convert the numpy array to it's final output for PyPNG
def semiFlatten3DNumpyArray(numpyArray):
    image_2d = numpyArray.reshape(numpy.size(numpyArray,0),(numpy.size(numpyArray,1)*numpy.size(numpyArray,2)))
    return image_2d

def ThreeDimensionImageFromBytearray(bytearrayList, channelQuantity, bitdepth):
    if channelQuantity < 1 or channelQuantity > 4:
        raise ValueError("PyPNG only offers L (Greyscale), LA (Greyscale with alpha), RGB (Red, Green, and Blue), and RGBA channels. The function ThreeDimensionImageFromBytearray was given the input of " + str(channelQuantity) + " channels to use which falls outside of the range of channels that PyPNG can offer.")
    image_2d = TwoDimensionImageFromBytearray(bytearrayList, bitdepth)
    image_3d = image_2d.reshape(numpy.size(image_2d,0),(numpy.size(image_2d,1)//channelQuantity),channelQuantity)
    return image_3d

#bitdepth here is per channel, not per pixel, hence it only include 2^x, x from 0 to 4
def TwoDimensionImageFromBytearray(bytearrayList, bitdepth):
    firstPass = True
    datatypeDictionary = {1 : numpy.bool, 8 : numpy.uint8, 16 :numpy.uint16}
    #Bit depths of 2 and 4 can be supported later
    for row in bytearrayList:
        if firstPass:
            image_2d = numpy.frombuffer(row, dtype = datatypeDictionary.get(bitdepth))
            firstPass = False
        else:
            byteRow = numpy.frombuffer(row, dtype = datatypeDictionary.get(bitdepth))
            image_2d = numpy.vstack((image_2d, byteRow))
    return image_2d

def OutputImage(filename,):
    f = open(filename, 'wb')

#This class is meant to help combine multiple different images together into a larger image. It can be combined with itself
#Defaults to RGB
class magicImage:
    
    def checkColorSize(numpyArray, channelNum):
        channels = ['L','LA','RGB','RGBA']
        if numpy.size(numpyArray) != channelNum:
            raise ValueError("Background color has " + str(numpy.size(numpyArray)) + " values despite being for " + channels[channelNum - 1])

    def __init__(self,greyscale = False, alpha = False, backColor = numpy.array([0,0,0]),outline = False,outlineColor = numpy.array([0,0,0]), boarder = 5, datatype = numpy.uint8,startingImage = None):
        if startingImage == None:
            if greyscale == True:
                if alpha == True:
                    checkColorSize(backColor,2)
                else:
                    checkColorSize(backColor,1)
                
            else:
                if alpha == True:
                    checkColorSize(backColor,4)
                else:
                    checkColorSize(backColor,3)

            
        
