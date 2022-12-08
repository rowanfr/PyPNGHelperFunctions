import numpy
import png
import PyPNGHelperFunctions as PNGHelper

image_3d = PNGHelper.importPNGto3DNumpy('png.png')

PNGHelper.export3DNumpytoPNG(image_3d, 'numpyTestOut.png')