from ultralytics import YOLO

model = YOLO("yolov8n.pt")

# CHANGE THIS LINE:
source = "2026-03-09 12-41-05.mp4"

if source.lower().endswith((".jpg", ".jpeg", ".png", ".bmp")):
    model.predict(source=source, conf=0.35, show=True, save=True)
else:
    model.track(source=source, tracker="bytetrack.yaml", conf=0.35, show=True, save=True)

print("Done. Check runs/ folder.")