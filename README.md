# Improved YOLO11 network for small target detection

This code is based on the YOLO11 network, and integrates the MLCA attention mechanism and the improved model of the WIoUv3 loss function, aiming to improve the detection of small targets in road images. The training data uses the open source Kitti dataset from Kaggle.


## How to Use

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/mumudjs/YOLO11-SmallObject-Detection.git
    cd YOLO11-SmallObject-Detection
    ```

2. **Set Up Dependencies**:
   - Ensure that you have all the required dependencies installed. You can install them by creating an environment with Conda to ensure they are available for use.

3. **Obtain Kitti for YOLO Dataset**:
   - Download the [kitti-yolo-images](https://www.kaggle.com/code/shreydan/kitti-object-detection-yolov8n/input?scriptVersionId=141221275) project.
   - Download the [kitti-yolo-labels](https://www.kaggle.com/datasets/shreydan/kitti-dataset-yolo-format?select=labels) project.
   - According to the data storage format of YOLO place it in the dateset directory.

4. **Check and Update Paths**:
   - Please modify the data storage path in './ultralytics/sfg/datasets/kitti.yaml' according to where you store the Kitti dataset.

5. **Run the train-kitti.py**:
   - Open the 'train-kitti.py', adjust the parameters and run to start training.


## Notes

- If you use a different dataset, be sure to modify the dataset path and configuration settings as necessary.

## Dataset

- This project only uses part of the Kitti dataset. You can replace the dataset with your own dataset according to the YOLO dataset storage method.


## Acknowledgements

- [Ultralytics](https://github.com/ultralytics/ultralytics) for providing the YOLO11 model.
- [Kaggle](https://www.kaggle.com/datasets/shreydan/kitti-dataset-yolo-format?select=labels) for the data.
- [MLCA](https://www.sciencedirect.com/science/article/abs/pii/S0952197623006267) [WIoUv3](https://arxiv.org/abs/2301.10051)for the improvement ideas.

## Contact

If you have any questions or suggestions, feel free to reach out through the repository's issues or contact me directly.
