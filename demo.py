import os
import shutil


def folder_image_processing():
    path = 'final_processed_images'

    count = 0
    folder_deleted = 'processed_images'
    imgFolder = 'processed_images'
    
    shutil.rmtree(folder_deleted)
    os.mkdir(imgFolder)
    for dirname, dirs, files in os.walk(path):
        for filename in files:
            filename_without_extension, extension = os.path.splitext(filename)

            if extension == '.jpg' or extension == '.png':
                print("Found img")
                print(filename)
                old_name = os.path.join(dirname, filename)
                # construct full file path
                new_name = os.path.join(imgFolder, filename)
                # Renaming the file
                os.rename(old_name, new_name)
                count = count+1

    print(count)

    print('....All Files Copied from yolo to Processed Image....')




if __name__ == "__main__":
    # folder_image_processing()
    for i in range(35, 39):
         print(i)