import cv2

cam = cv2.VideoCapture(0)

while True:
    ret,frame = cam.read()

    if not ret:
        print('unsuccessful')
        break

cv2.imshow('test',frame)

cv2.write('test.png',frame)
print(successful)

cam.release()
cam.destroyAllWindows