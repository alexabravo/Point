import struct 

def char(c):
    return struct.pack('=c', c.encode('ascii'))

def word(c):
    return struct.pack('=h', c)

def dword(c):
    return struct.pack('=l', c)

def color(r, g, b):
    return bytes([b, g, r])

class Render(object):

    def glInit(self, witdh, height):
        self.width = witdh
        self.height = height
        self.color = color(255, 255, 255)
        self.framebuffer = []
        self.glclear
       

    def glClear(self):
        self.framebuffer = [
            [color(0, 0, 0) for x in range(self.width)]
            for y in range(self.height)
        ]
        
    def glCreateWindow(self, width, height):
        self.width = width
        self.height = height        
      

    def glViewPort(self, x, y, width, height):
        self.xVP = x
        self.yVP = y
        self.wVP = width
        self.hVP = height
        

    def glClearColor(self, r=0, g=0, b=0):
        self.framebuffer = [
        [color(r, b, g) for x in range(self.width)]
        for y in range(self.height)
            ]

    def point(self, x, y):
        self.framebuffer[x][y] = color(255, 0, 0)

    def glVertex(self, x, y):
        x_Ver = int(round(self.wVP/2)*(x+1))
        y_Ver = int(round(self.yVP/2)*(x+1))
        x_pnt = self.xVP + x_Ver
        y_pnt = self.yVP + y_Ver
        self.point((x_pnt),(y_pnt))
    
    def glColor(self, r, g, b):
        self.color = color (r, g, b)

    def glFinish(self, filename):
        f = open(filename, 'bw')

        f.write(char('B'))
        f.write(char('M'))
        f.write(dword(14 + 40 + self.width + self.height * 3))
        f.write(dword(0))
        f.write(dword(14 + 40))

        f.write(dword(40))
        f.write(dword(self.width))
        f.write(dword(self.height))
        f.write(word(1))
        f.write(word(24))
        f.write(dword(0))
        f.write(dword(self.width * self.height * 3))
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))


        for x in range(self.height):
            for y in range(self.width):
                f.write(self.framebuffer[x][y])
        f.close()

bitmap = Render()
bitmap.glCreateWindow(100,100)
bitmap.glViewPort(20, 40, 50, 20)
bitmap.glClear()
bitmap.glVertex(0,0)
bitmap.glFinish('punto.bmp')

