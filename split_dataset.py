import os
import random
import shutil

# Define paths
dataset_path = "data/dataset"  # Both images & labels are directly in this folder
label_path = dataset_path  # Labels are also in this folder

# Define target train/val paths
image_train_path = os.path.join(dataset_path, "images/train")
image_val_path = os.path.join(dataset_path, "images/val")
label_train_path = os.path.join(dataset_path, "labels/train")
label_val_path = os.path.join(dataset_path, "labels/val")

# Create the necessary folders
for folder in [image_train_path, image_val_path, label_train_path, label_val_path]:
    os.makedirs(folder, exist_ok=True)

# Debug: List initial files
all_files = os.listdir(dataset_path)
print("📂 All files in dataset directory before splitting:", all_files)

# Get all images from dataset (Filter only valid image formats)
image_files = [f for f in all_files if os.path.isfile(os.path.join(dataset_path, f)) and f.lower().endswith(('.png', '.jpg', '.jpeg'))]

if not image_files:
    print("⚠️ No image files found in", dataset_path)
    exit()

# Shuffle images for randomness
random.shuffle(image_files)

# Split: 80% train, 20% val
split_idx = int(0.8 * len(image_files))
train_files, val_files = image_files[:split_idx], image_files[split_idx:]

# Function to move images and labels correctly
def move_files(files, src_img, src_lbl, dest_img, dest_lbl):
    for file in files:
        # Move image
        src_image_file = os.path.join(src_img, file)
        dest_image_file = os.path.join(dest_img, file)

        if os.path.exists(src_image_file):
            print(f"📦 Moving Image: {src_image_file} -> {dest_image_file}")
            shutil.move(src_image_file, dest_image_file)
        else:
            print(f"⚠️ Image file {file} not found!")

        # Move corresponding label file (Assuming .txt format)
        label_file = file.rsplit(".", 1)[0] + ".txt"  # Convert image filename to label filename
        src_label_file = os.path.join(src_lbl, label_file)
        dest_label_file = os.path.join(dest_lbl, label_file)

        if os.path.exists(src_label_file):
            print(f"📦 Moving Label: {src_label_file} -> {dest_label_file}")
            shutil.move(src_label_file, dest_label_file)
        else:
            print(f"⚠️ Label file {label_file} not found!")

# Move images and labels to their respective train/val folders
move_files(train_files, dataset_path, label_path, image_train_path, label_train_path)
move_files(val_files, dataset_path, label_path, image_val_path, label_val_path)

# Debugging output
print("✅ After splitting, train images:", os.listdir(image_train_path))
print("✅ After splitting, val images:", os.listdir(image_val_path))
print("✅ After splitting, train labels:", os.listdir(label_train_path))
print("✅ After splitting, val labels:", os.listdir(label_val_path))

print("✅ Dataset successfully split into train/ and val/!")
