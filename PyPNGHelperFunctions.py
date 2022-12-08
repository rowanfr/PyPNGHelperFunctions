#Requisites for these helper functions are Numpy and PyPNG
#Source for many function ideas: https://ciechanow.ski/alpha-compositing/
#
import png
import numpy

def importPNGtoNumpy(filename):
    imageData = png.Reader(filename=filename).asDirect()
    return imageData

def ThreeDimensionImageFromBytearray(bytearrayList, channelQuantity):
    if channelQuantity < 1 or channelQuantity > 4:
        raise ValueError("PyPNG only offers L (Greyscale), LA (Greyscale with alpha), RGB (Red, Green, and Blue), and RGBA channels. The function ThreeDimensionImageFromBytearray was given the input of " + str(channelQuantity) + " channels to use which falls outside of the range of channels that PyPNG can offer.")
    image_2d = TwoDimensionImageFromBytearray(bytearrayList)
    image_3d = image_2d.reshape(numpy.size(image_2d,0),(numpy.size(image_2d,1)//channelQuantity),channelQuantity)
    return image_3d


def TwoDimensionImageFromBytearray(bytearrayList):
    image_2d = numpy.vstack(bytearrayList)
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

            
        
