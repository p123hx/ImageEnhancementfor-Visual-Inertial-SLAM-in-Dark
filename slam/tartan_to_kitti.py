import sys
import os
import shutil
import re

if __name__ == '__main__':
    print("\n\n------------------------------------------------")
    print(">> TartanAir Tools v0p1")
    print(">> Convert TartanAir Format to KITTI format")
    print(">> Developed by: Islam A. Ali")
    print("------------------------------------------------\n")

    if (len(sys.argv)) <2:
        # command line argument is not provided
        print("[Error] Dataset path is not provided !")
        sys.exit()
    else:
        # get the dataset path from the command line argument
        dataset_path = sys.argv[1]
        print("[INFO] TartanAir Dataset folder path is: "+dataset_path)
        left_img_path = dataset_path+"/image_left"
        right_img_path = dataset_path+"/image_right"

        # check if left images directory exists
        if os.path.exists(left_img_path):
            print("[INFO] Left camera images folder found")
        else:
            print("[Error] Left camera images folder not found")
            sys.exit()

        # check if right images directory exists
        if os.path.exists(right_img_path):
            print("[INFO] Right camera images folder found")
        else:
            print("[Error] Right camera images folder not found")
            sys.exit()

        # create the directory structure of the kitti conversion
        kitti_path = dataset_path+"/kitti"
        kitti_left = kitti_path+"/image_0"
        kitti_right = kitti_path+"/image_1"

        if os.path.exists(kitti_path):
            print("[WARNING] kitti directory folder found, deleting it !")
            shutil.rmtree(kitti_path)

        os.mkdir(kitti_path)
        os.mkdir(kitti_left)
        os.mkdir(kitti_right)

        # copy the images in left folder to image_0
        src_files = os.listdir(left_img_path)
        for file_name in src_files:
            full_file_name = os.path.join(left_img_path, file_name)
            if os.path.isfile(full_file_name):
                shutil.copy(full_file_name, kitti_left)
                new_name = re.sub('\_left', '', file_name)
                os.rename(kitti_left+"/"+file_name, kitti_left+"/"+new_name)

        # copy the images in right folder to image_1
        images_count = 0
        src_files = os.listdir(right_img_path)
        for file_name in src_files:
            full_file_name = os.path.join(right_img_path, file_name)
            if os.path.isfile(full_file_name):
                shutil.copy(full_file_name, kitti_right)
                new_name = re.sub('\_right', '', file_name)
                os.rename(kitti_right+"/"+file_name, kitti_right+"/"+new_name)
                images_count += 1

        # create the timestamp file for the dataset
        timestamp_file = open(kitti_path+"/times.txt", 'w')
        timestamp_val = 0
        for i in range(images_count):
            timestamp_val += 0.1
            timestamp_file.write(str(timestamp_val)+"\n")
        print("[INFO] Timestamp file created successfully.")

        # copy the yaml file beside the images folders
        if os.path.isfile('tartanair.yaml'):
            shutil.copyfile('tartanair.yaml', kitti_path+"/tartanair.yaml")
            print("[INFO] YAML file copied successfully.")
        else:
            print("[Error] YAML file not found.")





