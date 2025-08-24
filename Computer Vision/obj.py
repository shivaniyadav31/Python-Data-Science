from ultralytics import YOLO

#pre-trained YOLOv8 Nano model(fast aur lightweighted)
model = YOLO("yolov8n.pt")

#webcam se live object detection (source=0 matlab default camera)
model.predict(
    source=0,  #webcam
    show=True,  #shows live window
    conf=0.5,  #confidence threshold (50%)-for managing brightness
)

