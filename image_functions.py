from PIL import Image, ImageFilter
import math
import numpy

class ImageFunctions:
    blurRadius = 0.0
    greyScale = False

    def __init__(self, blurRadius, greyScale):
        self.blurRadius = blurRadius
        self.greyScale = greyScale

    def applyGreyScale(self, image):
        grey = Image.new(image.mode, image.size)
        width, height = image.size

        # greyscale val is just the average of rgb colours
        for x in range(0, width):
            for y in range(0, height):
                pixel = image.getpixel((x,y))
                avg = int((pixel[0]+pixel[1]+pixel[2])/3)
                grey.putpixel((x,y), (avg, avg, avg))

        return grey

    def gaussianBlur(self, img, blurRadius):
        return img.filter(ImageFilter.GaussianBlur(blurRadius))

    def detectEdges(self, img):

        if (self.greyScale):
            img = self.applyGreyScale(self.gaussianBlur(img, self.blurRadius))
        else:
            img = self.gaussianBlur(img, self.blurRadius)
        
        sobel_x = [[-1,0,1],
                   [-2,0,2],
                   [-1,0,1]]

        sobel_y = [[-1,-2,-1],
                    [0, 0, 0],
                    [1, 2, 1]]

        newImg = Image.new(img.mode, img.size)

        for x in range(len(sobel_x)-1, img.size[0]):  
            for y in range(len(sobel_y)-1, img.size[1]): 

                # initialise Gx to 0 and Gy to 0 for every pixel
                Gx = 0
                Gy = 0

                for xPixel in range( - ( len(sobel_x) -1 ), 1):
                    for yPixel in range( - ( len(sobel_y) -1), 1):

                        p = img.getpixel((x + xPixel, y + yPixel))

                        # Sum of rgb channels (greyscale pixels have same channel values)
                        intensity = p[0]+p[1]+p[2]

                        Gx += sobel_x[yPixel + 2][xPixel + 2] * intensity
                        Gy += sobel_y[yPixel + 2][xPixel + 2] * intensity
                

                # Length of gradient (Pythagorean theorem)
                val = math.sqrt((Gx * Gx) + (Gy * Gy))

                # Normalize in the range of 0 - 255 (rgb range)
                val = math.floor(val / 4328 * 255)

                newImg.putpixel((x,y),(val,val,val))

        return newImg

