from ultralytics import YOLO
import cv2
import torch
import numpy as np
import os

model = YOLO(r'c:\Users\amine\Documents\Personal\PYCAD\code-templates\utils\mandible_model_weight\best.pt')
img_path = '../../assets/panoramic.png'
output_dir = os.path.join('./dataset/yolo_predictions', os.path.basename(img_path).split('.')[0])
os.makedirs('./dataset/yolo_predictions', exist_ok=True)

results = model.predict(source=img_path, conf=0.5, save=False, save_txt=False)
masks = results[0].masks
boxes = results[0].boxes

# Read the input image
input_img = cv2.imread(img_path)
input_img = cv2.cvtColor(input_img, cv2.COLOR_BGR2RGB)

# Define the color for the mask (BGR format)
mask_color = (250, 200, 0)  # Green color

for idx, mask in enumerate(masks):
    m = torch.squeeze(mask.data)

    # Convert the tensor to numpy array
    mask_np = m.cpu().numpy().astype(np.uint8)

    # Create a colored mask
    colored_mask = np.zeros((mask_np.shape[0], mask_np.shape[1], 3), dtype=np.uint8)
    colored_mask[mask_np == 1] = mask_color

    # Resize mask to match input image size
    colored_mask = cv2.resize(colored_mask, (input_img.shape[1], input_img.shape[0]))

    # Blend the colored mask with the input image
    alpha = 0.5  # Transparency factor. You can change it as needed.
    overlayed_img = cv2.addWeighted(input_img, 1, colored_mask, alpha, 0)

    # Save the image with overlayed mask
    cv2.imwrite(os.path.join(output_dir, f'mask_overlay_{idx}.png'), cv2.cvtColor(overlayed_img, cv2.COLOR_RGB2BGR))

    # Display the image with overlayed mask
    cv2.imshow(f'Segmentation Mask Overlay {idx}', cv2.cvtColor(overlayed_img, cv2.COLOR_RGB2BGR))
    cv2.waitKey(0)
    cv2.destroyAllWindows()
