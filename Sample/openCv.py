import cv2



# ここからスタート
if __name__ == '__main__':
    
    for i1 in range(0, 2): 
        cap1 = cv2.VideoCapture( i1, cv2.CAP_DSHOW )
        if cap1.isOpened(): 
            print("VideoCapture(", i1, ") : Found")
        else:
            print("VideoCapture(", i1, ") : None")
        cap1.release()


    cap2 = cv2.VideoCapture(1)
    if cap2.isOpened(): 
        ret, frame = cap2.read()
        if ( ret == True ):
            cv2.imwrite("image.png", frame)
        else:
            print("Read Error")
    cap2.release()


