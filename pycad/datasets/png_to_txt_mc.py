import os
import cv2
import numpy as np


class PngToTxtConverterMC:
    '''
    The name PngToTxtConverterML is for: Png To Txt Converter for Multi Class (one image mask containing all the classes).\n
    This class is for the creation of the polygones from PNG images (we can replace them with jpg alos), the idea of this class is to to have multiple classes in one image mask and extract all the classes to createthe txt file. The structure of the folder
    is as follows:\n

    input_folder\n
    |__ image_0.png
    |__ image_1.png
    |__ ...

    `Params`:
    - input_folder: the path to all the mask images.
    - output_folder: the path to save the generated txt files.
    - epsilon_coeff: the percentage that will be used to create the polygon points, a smaller value will lead to more accurate results (but it can create complex shape so be careful).\n

    ### Example of usage:
    ```
    from pycad.preprocess import converters

    input_folder = 'path to the mask images'
    output_folder = 'path to save the generated txt files'
    converter = converters.PngToTxtConverterMC(input_folder, output_folder, 0.001) # lets use a coeff of .1%

    converter.run()

    ```

    '''
    def __init__(self, input_folder, output_folder, epsilon_coeff=0.001):
        self.input_folder = input_folder
        self.output_folder = output_folder
        self.epsilon_coeff = epsilon_coeff
        os.makedirs(self.output_folder, exist_ok=True)

    def multi_class_mask_to_yolo_polygons(self, mask, classes=[0, 1, 2]):
        all_polygons = []
        for class_index in classes:
            binary_mask = (mask == class_index).astype(np.uint8) * 255
            contours, _ = cv2.findContours(binary_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            for contour in contours:
                if len(contour) >= 5:
                    epsilon = self.epsilon_coeff * cv2.arcLength(contour, True)
                    approx_contour = cv2.approxPolyDP(contour, epsilon, True)
                    x_coords_normalized = approx_contour[:, 0, 0] / mask.shape[1]
                    y_coords_normalized = approx_contour[:, 0, 1] / mask.shape[0]
                    polygon = np.vstack((x_coords_normalized, y_coords_normalized)).T
                    polygon_line = f"{class_index - 1} " + ' '.join([f"{x:.6f} {y:.6f}" for x, y in polygon])
                    all_polygons.append(polygon_line)
        return all_polygons

    def run(self):
        image_files = [f.path for f in os.scandir(self.input_folder) if f.is_file() and f.name.endswith('.png')]
        for image_file in image_files:
            mask = cv2.imread(image_file, cv2.IMREAD_GRAYSCALE)
            polygons = self.multi_class_mask_to_yolo_polygons(mask)
            
            output_filename = f"{os.path.splitext(os.path.basename(image_file))[0]}.txt"
            output_path = os.path.join(self.output_folder, output_filename)

            with open(output_path, 'w') as f:
                for polygon_line in polygons:
                    f.write(polygon_line + '\n')