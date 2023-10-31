import os
import cv2
import numpy as np


class PngToTxtConverterML:
    '''
    The name PngToTxtConverterML is for: Png To Txt Converter for Multi Labels (multiple image files representing the classes).\n
    This class is for the creation of the polygones from PNG images (we can replace them with jpg alos), the idea of this class is to to have multiple classes in the mask BUT the structure is like this:\n
    input_folder\n
    |__ mask_class_1_folder\n
        |__ image_0.png
        |__ image_1.png
        |__ ...

    |__ mask_class_2_folder\n
        |__ image_0.png
        |__ image_1.png
        |__ ...

    |__ ...\n

    Having a structure different than this, will lead to not working properly.\n

    `Params`:\n
    - epsilon_coeff: the percentage that will be used to create the polygon points, a smaller value will lead to more accurate results (but it can create complex shape so be careful).\n
    - input_folder: the path to the mask images (.png), if you want .jpg for example, then make sure to change that in the code.\n
    - output_folder: the path to save the generated txt files.

    '''
    def __init__(self, input_folder, output_folder, epsilon_coeff=0.01):
        self.input_folder = input_folder
        self.output_folder = output_folder
        self.epsilon_coeff = epsilon_coeff
        os.makedirs(self.output_folder, exist_ok=True)

    def binary_mask_to_yolo_polygon(self, binary_mask, class_index):
        contours, _ = cv2.findContours(binary_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        polygons = []

        for contour in contours:
            if len(contour) >= 5:
                epsilon = self.epsilon_coeff * cv2.arcLength(contour, True)
                approx_contour = cv2.approxPolyDP(contour, epsilon, True)

                x_coords_normalized = approx_contour[:, 0, 0] / binary_mask.shape[1]
                y_coords_normalized = approx_contour[:, 0, 1] / binary_mask.shape[0]
                polygon = np.vstack((x_coords_normalized, y_coords_normalized)).T

                polygons.append(f"{class_index} " + ' '.join([f"{x:.6f} {y:.6f}" for x, y in polygon]))

        return polygons

    def run(self):
        subfolders = [f.path for f in os.scandir(self.input_folder) if f.is_dir()]
        
        for subfolder in subfolders:
            input_files = sorted([f for f in os.listdir(subfolder) if f.endswith('.png')])
            print(input_files)
            if len(input_files) == 2:    
                class_0_file = input_files[0]
                class_1_file = input_files[1]

                class_0_path = os.path.join(subfolder, class_0_file)
                class_1_path = os.path.join(subfolder, class_1_file)

                class_0_mask = cv2.imread(class_0_path, cv2.IMREAD_GRAYSCALE)
                class_1_mask = cv2.imread(class_1_path, cv2.IMREAD_GRAYSCALE)

                polygons_class_0 = self.binary_mask_to_yolo_polygon(class_0_mask, 0)
                polygons_class_1 = self.binary_mask_to_yolo_polygon(class_1_mask, 1)

                output_filename = f"{os.path.basename(subfolder)}.txt"
                output_path = os.path.join(self.output_folder, output_filename)

                with open(output_path, 'w') as f:
                    for polygon_line in polygons_class_0:
                        f.write(polygon_line + '\n')
                    for polygon_line in polygons_class_1:
                        f.write(polygon_line + '\n')
            elif len(input_files) == 1:    
                class_0_file = input_files[0]

                class_0_path = os.path.join(subfolder, class_0_file)

                class_0_mask = cv2.imread(class_0_path, cv2.IMREAD_GRAYSCALE)

                polygons_class_0 = self.binary_mask_to_yolo_polygon(class_0_mask, 0)

                output_filename = f"{os.path.basename(subfolder)}.txt"
                output_path = os.path.join(self.output_folder, output_filename)

                with open(output_path, 'w') as f:
                    for polygon_line in polygons_class_0:
                        f.write(polygon_line + '\n')

            else:
                print(subfolder)