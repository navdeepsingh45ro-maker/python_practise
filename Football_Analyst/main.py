import cv2 
import numpy as np 
import mss
from ultralytics import YOLO

model = YOLO("yolov8n.pt")
sct = mss.mss()

monitor = {
    "top": 200,
    "left": 600,
    "width": 1100,
    "height": 500
}

cv2.namedWindow("Overlay", cv2.WINDOW_NORMAL)
cv2.setWindowProperty("Overlay", cv2.WND_PROP_TOPMOST, 1)

while True:
    screenshot = sct.grab(monitor)
    frame = np.array(screenshot)

    frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)
    
    results = model(frame)
    
    cv2.imshow("Overlay", frame)
    for r in results:
        for boxes in r.boxes:
            cls = int(boxes.cls[0])

            if cls == 0 :
                x1, y1, x2, y2 = map(int , boxes.xyxy[0])

                cv2.rectangle(frame,(x1, y1), (x2, y2), (0,255,0), 2)


    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()