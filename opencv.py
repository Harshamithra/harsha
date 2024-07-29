import cv2

def main():
    imgpath = r"C:\Users\harshamithra\Downloads\happy.tif"
    img = cv2.imread(imgpath)
    cv2.namedWindow('fig1', cv2.WINDOW_AUTOSIZE)
    cv2.imshow('fig1',img)
    cv2.waitKey(0)
    cv2.destroyALLWindows()
    
if __name__ == "__main__":
   main()    