import png
s = ['110010010011',
     '101011010100',
     '110010110101',
     '100010010011']
s = [[int(c) for c in row] for row in s]
palette=[(0x55,0x55,0x55), (0xff,0x99,0x99)]
w = png.Writer(len(s[0]), len(s), palette=palette, bitdepth=1)
f = open('png.png', 'wb')#python function, w indicates write meaning that it writes over or creates file, b is binary mode
w.write(f, s)#F is file that's open and s is array
f.close()