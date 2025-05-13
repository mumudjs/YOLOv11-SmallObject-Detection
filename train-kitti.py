from ultralytics import YOLO
import glob

if __name__ == '__main__':
    model = YOLO('yolo11n-MLCA.yaml')
    model.train(data='./ultralytics/cfg/datasets/kitti.yaml', workers=8, batch=32, epochs=200)

