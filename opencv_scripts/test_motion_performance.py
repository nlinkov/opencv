import cv2
import timeit

#Capture three frames from camera
#cam = cv2.VideoCapture(0)
#_, frame1 = cam.read()
#_, frame2 = cam.read()
#_, frame3 = cam.read()


def motion_detect(frame1, frame2, frame3):
    def diffImg(t0, t1, t2):
      d1 = cv2.absdiff(t2, t1)
      d2 = cv2.absdiff(t1, t0)
      return cv2.bitwise_and(d1, d2)
    t_minus = cv2.cvtColor(frame1, cv2.COLOR_RGB2GRAY)
    t = cv2.cvtColor(frame2, cv2.COLOR_RGB2GRAY)
    t_plus = cv2.cvtColor(frame3, cv2.COLOR_RGB2GRAY)
    return diffImg(t_minus, t, t_plus)

def motion_detect_BS_MOG(frame1, frame2, frame3):
    fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()
    for frame in (frame1, frame2, frame3):
        fgmask = fgbg.apply(frame)
        return fgmask

def motion_detect_BS_MOG2(frame1, frame2, frame3):
    fgbg = cv2.createBackgroundSubtractorMOG2()
    for frame in (frame1, frame2, frame3):
        fgmask = fgbg.apply(frame)
        return fgmask

def motion_detect_BS_GMG(frame1, frame2, frame3):
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
    fgbg = cv2.bgsegm.createBackgroundSubtractorGMG()
    for frame in (frame1, frame2, frame3):
        fgmask = fgbg.apply(frame)
        fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)
        return fgmask


timeit.timeit(setup='gc.disable(); from __main__ import motion_detect, frame1, frame2, frame3', stmt='motion_detect(frame1, frame2, frame3)', number=1)

#Results:
#>>> timeit.timeit(setup='gc.disable(); from __main__ import motion_detect, frame1, frame2, frame3', stmt='motion_detect(frame1, frame2, frame3)', number=100)
#0.4090280420000454

>>> timeit.timeit(setup='gc.disable(); from __main__ import motion_detect_BS_MOG, frame1, frame2, frame3', stmt='motion_detect_BS_MOG(frame1, frame2, frame3)', number=100)
15.081822761999774

>>> timeit.timeit(setup='gc.disable(); from __main__ import motion_detect_BS_MOG2, frame1, frame2, frame3', stmt='motion_detect_BS_MOG2(frame1, frame2, frame3)', number=100)
3.3101735970003574

>>> timeit.timeit(setup='gc.disable(); from __main__ import motion_detect_BS_GMG, frame1, frame2, frame3', stmt='motion_detect_BS_GMG(frame1, frame2, frame3)', number=100)
23.442041975999928
