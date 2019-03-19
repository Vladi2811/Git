# Class that merge two images in one
import cv2
import numpy as np


class merge:

    @staticmethod
    def mergeImages(frontImage, backImage, position="left-top"):

        # Read front image
        imgFront = cv2.imread(frontImage, cv2.IMREAD_UNCHANGED)
        # Read background image and getting the shape
        imgBack = cv2.imread(backImage, cv2.IMREAD_UNCHANGED)
        heightBack, widthBack, componentsBack = imgBack.shape
        # Resizing the front image and getting the shape
        imgFront = cv2.resize(imgFront, (int(widthBack/4), int(heightBack/8)))
        heightFront, widthFront, componentsFront = imgFront.shape

        # Getting the max shape
        height = max(heightFront, heightBack)
        width = max(widthFront, widthBack)

        # Depending of the position, it merges the images

        if(position.lower() == "right-bottom" or position.lower() == "bottom-right"):
            startX = 0
            startY = 0

            while(startX + (widthBack-widthFront) < width):
                startY = 0
                while(startY + (heightBack-heightFront) < height):
                   # We create the alpha variable
                    alpha = imgFront[startY, startX, 3]/255

                    imgBack[startY + (heightBack-heightFront), startX + (widthBack-widthFront)] = [alpha*imgFront[startY, startX, 0] + (1-alpha)*imgBack[startY + (heightBack-heightFront), startX + (widthBack-widthFront), 0],
                                               alpha *imgFront[startY, startX, 1] +(1-alpha) *imgBack[startY + (heightBack-heightFront), startX + (widthBack-widthFront), 1],
                                               alpha*imgFront[startY, startX, 2] + (1-alpha)*imgBack[startY + (heightBack-heightFront), startX + (widthBack-widthFront), 2]]
                    startY = startY + 1

                startX = startX + 1
        elif(position.lower() == "left-top" or position.lower() == "top-left"):
            startX = 0
            startY = 0

            while(startX < widthFront):
                startY = 0
                while(startY < heightFront):
                    # We create the alpha variable
                    alpha = imgFront[startY, startX, 3]/255

                    imgBack[startY, startX] = [alpha*imgFront[startY, startX, 0] + (1-alpha)*imgBack[startY, startX, 0],
                                               alpha *imgFront[startY, startX, 1] +(1-alpha) *imgBack[startY, startX, 1],
                                               alpha*imgFront[startY, startX, 2] + (1-alpha)*imgBack[startY, startX, 2]]
                    startY = startY + 1

                startX = startX + 1
        elif(position.lower() == "left-bottom" or position.lower() == "bottom-left"):
            startX = 0
            startY = 0

            while(startX < widthFront):
                startY = 0
                while(startY + (heightBack-heightFront)< height):
                    # We create the alpha variable
                    alpha = imgFront[startY, startX, 3]/255

                    imgBack[startY + (heightBack-heightFront), startX] = [alpha*imgFront[startY, startX, 0] + (1-alpha)*imgBack[startY + (heightBack-heightFront), startX, 0],
                                               alpha *imgFront[startY, startX, 1] +(1-alpha) *imgBack[startY + (heightBack-heightFront), startX, 1],
                                               alpha*imgFront[startY, startX, 2] + (1-alpha)*imgBack[startY + (heightBack-heightFront), startX, 2]]
                    startY = startY + 1

                startX = startX + 1
        elif(position.lower() == "right-top" or position.lower() == "top-right"):
            startX = 0
            startY = 0

            while(startX + (widthBack-widthFront) < width):
                startY = 0
                while(startY < heightFront):
                    # We create the alpha variable
                    alpha = imgFront[startY, startX, 3]/255

                    imgBack[startY, startX + (widthBack-widthFront)] = [alpha*imgFront[startY, startX, 0] + (1-alpha)*imgBack[startY, startX + (widthBack-widthFront), 0],
                                               alpha *imgFront[startY, startX, 1] +(1-alpha) *imgBack[startY, startX + (widthBack-widthFront), 1],
                                               alpha*imgFront[startY, startX, 2] + (1-alpha)*imgBack[startY, startX + (widthBack-widthFront), 2]]
                    startY = startY + 1

                startX = startX + 1
        """cv2.imshow('image', imgBack)
        cv2.waitKey(0)
        cv2.destroyAllWindows()"""
        cv2.imwrite("OutFiles/img2.jpg",imgBack)
