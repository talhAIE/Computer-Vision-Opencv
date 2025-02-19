import cv2
import matplotlib.pyplot as plt
from IPython.display import Image

mypic=cv2.imread('images/mypic.jpg')
#convert picture to RGB to show original color via matplotlib
# mypic=cv2.cvtColor(mypic,cv2.COLOR_BGR2RGB)

# plt.imshow(mypic)
# plt.title('My Picture')
# plt.show()

#show image via cv2 imshow
# w1=cv2.namedWindow('w1')
# cv2.imshow(w1,mypic)
# cv2.waitKey(0)
# cv2.destroyWindow(w1)
flag=True
while flag:
    cv2.imshow('My Picture' ,mypic)
    keypress=cv2.waitKey(1)
    if keypress== ord('q'):
        flag=False
cv2.destroyAllWindows()