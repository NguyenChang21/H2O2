from PIL import Image
import os

def crop_images_in_folder(folder_path, crop_coords, output_folder):
    """
    Cắt tất cả các ảnh trong thư mục theo tọa độ cho trước.
    
    Args:
    folder_path (str): Đường dẫn đến thư mục chứa ảnh.
    crop_coords (tuple): Tuple 4 giá trị (left, upper, right, lower) để cắt ảnh.
    output_folder (str): Đường dẫn đến thư mục lưu ảnh đã cắt.
    # """
    # # Tạo thư mục output nếu nó không tồn tại
    # if not os.path.exists(output_folder):
    #     os.makedirs(output_folder)

    # Duyệt qua tất cả các file trong thư mục
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            img_path = os.path.join(folder_path, filename)
            img = Image.open(img_path)
            cropped_img = img.crop(crop_coords)
            cropped_img.save(os.path.join(output_folder, filename))
            print(f"Đã cắt và lưu: {filename}")

# Thay đổi các đường dẫn và tọa độ theo nhu cầu của bạn
folder_path = 'C:/vs code/H2O2/h202/raw data/data cut/60uM fn'
output_folder = 'C:/vs code/H2O2/h202/raw data/data cut/60uM new'
crop_coords = (19,108,64,220)  # Thay đổi tọa độ này theo yêu cầu

crop_images_in_folder(folder_path, crop_coords, output_folder)
