import torch

model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

print(model)
# imgs = ['photo.jpg']

# results = model(imgs)

# results.print()
# results.show()
