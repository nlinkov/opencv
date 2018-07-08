from curses import wrapper
import curses

import cv2
capture = cv2.VideoCapture(0)
frame_width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
print('Frame width:', frame_width)
print('Frame height:', frame_height)

video = cv2.VideoWriter('data/captured_video.avi', cv2.VideoWriter_fourcc(*
                                                                          'X264'), 25, (frame_width, frame_height))


def main(stdscr):
    stdscr.clear()
    while True:
        has_frame, frame = capture.read()
        if not has_frame:
            print('Can\'t get frame')
            break
        video.write(frame)
        cv2.imshow('frame', frame)
        key = stdscr.getch()
        if key == ord('q'):
            print('Pressed q')
            capture.release()
            video.release()
            cv2.destroyAllWindows()
            break


capture.release()
video.release()
cv2.destroyAllWindows()
