import os
import time
import cv2

camera = None
fileName = ""

def takePicture():
    global fileName
    global camera
    
    if len(fileName) != 0:
        os.unlink(fileName) # 파일 삭제
        if camera == None:
            camera = cv2.VideoCapture(0, cv2.CAP_V4L)
            camera.set(cv2.CAP_PROP_FRAME_WIDTH, 160) # 너무 크면 느려짐
            camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 120) # 너무 크면 느려짐
            takeTime = time.time()
            fileName = "./static/%d.jpg" % (takeTime * 10) # 촬영한 파일 이름 만들기
        ret, frame = camera.read()
        cv2.imwrite(fileName, frame)
        return fileName # 촬영한 파일 이름 리턴

def stopPicture():
    camera.release()
    camera = None
    fileName = ""


if __name__ == '__main__' :
        takePicture()

if __name__ == 'myCamera' :
        pass
