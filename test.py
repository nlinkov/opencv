#!/Users/nikolay/Documents/opencv/venv-opencv/bin/python

import cv2


def main():
    while True:
        try:
            print('printing...')
        except (KeyboardInterrupt, SystemExit):
            print('breaking...')
            break


if __name__ == '__main__':
    main()

cv2.destroyAllWindows()
cv2.waitKey(1)
