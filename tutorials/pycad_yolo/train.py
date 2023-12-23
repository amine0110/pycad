import os
from ultralytics import YOLO

if __name__ == '__main__':
    model = YOLO('yolov8s-seg.yaml').load('yolov8s.pt')   # load a pretrained model (recommended for training)

    # Train the model
    dataset_path = "./datasets/xray_panoramic_mandible/yolo/dataset.yaml"
    results = model.train(data=dataset_path, epochs=100, imgsz=640, batch=8, patience=30,
                        lr0=.01, lrf=.002, momentum=.937, weight_decay=.0005, warmup_epochs=3.0,
                        warmup_momentum=0.8, warmup_bias_lr=.1, box=7.5, cls=.5, dfl=1.5, pose= 12.0,
                        kobj=1.0, label_smoothing=0.0, nbs=64, hsv_h=.015, hsv_s=.7, hsv_v=.4, degrees=.0,
                        translate=.1, scale=.0, shear=.0, perspective=.0, flipud=.5, fliplr=.5, mosaic=.0,
                        mixup=.0, copy_paste=.3
                        )