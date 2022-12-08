import png
p = [(255,0,0, 0,255,0, 0,0,255),
     (128,0,0, 0,128,0, 0,0,128)]
f = open('swatch.png', 'wb')
w = png.Writer(3, 2, greyscale=False)
w.write(f, p)
f.close()