import cv2 
import motiongraph

def motionDetection():
    video = cv2.VideoCapture(0)
    prevFrame = None
     
    timeSeconds = 0
    motionDetectionList=[]
    detected=False
    fps = video.get(cv2.CAP_PROP_FPS)
    frameNo=0
    while True:

        _,frame = video.read()
        grayFrame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        grayFrame = cv2.GaussianBlur(grayFrame,(21,21),0)

        if prevFrame is None:
            prevFrame = grayFrame
            continue

        frameDiff = cv2.absdiff(prevFrame,grayFrame)
        threshFrame = cv2.threshold(frameDiff,30,255,cv2.THRESH_BINARY)[1]
        if((threshFrame==255).any()):
            detected=True
        
        if frameNo % fps == 0:
            timeSeconds+=1 
            if detected==True:
                motionDetectionList.append(timeSeconds)
                detected=False
            print timeSeconds
        cv2.imshow("Diff",threshFrame)
        frameNo+=1
        prevFrame = grayFrame
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
    video.release()
    cv2.destroyAllWindows
    return motionDetectionList

motiongraph.plotter(motionDetection())
