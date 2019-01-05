import cv2 
import motiongraph
import time 

def motionDetection():
    video = cv2.VideoCapture(0)
    prevFrame = None
     
    timeSeconds = 0
    motionDetectionList=[] # keeps track of seconds in which motion has occurred
    detected=False
    prevTime = time.time()
    print "Press Q to exit"
    while True:
        newTime = time.time()
        _,frame = video.read()
        grayFrame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	#Reduce the filter if you indent to increase the sensitivity
        grayFrame = cv2.GaussianBlur(grayFrame,(21,21),0) 

        if prevFrame is None:
            prevFrame = grayFrame
            continue
	#Calculating Difference b/w previous and new frame
        frameDiff = cv2.absdiff(prevFrame,grayFrame)
	#Applying thresholding
        threshFrame = cv2.threshold(frameDiff,30,255,cv2.THRESH_BINARY)[1]
	#Checking the presence of white value <if presence motion has occurred>
        if((threshFrame==255).any()):
            detected=True
        
        if newTime-prevTime>=1:
            prevTime = newTime
            timeSeconds+=1 
            if detected==True:
                motionDetectionList.append(timeSeconds)
                detected=False

        cv2.imshow("Difference",threshFrame)


        prevFrame = grayFrame
        key = cv2.waitKey(1)
        if key == ord('q'):
	    print 'Exiting..'
            break
    video.release()
    cv2.destroyAllWindows
    return motionDetectionList

motiongraph.plotter(motionDetection())
