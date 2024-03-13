import os
import shutil
from PIL import Image

TARGET = "organized"

os.mkdir(TARGET)

for directory in os.listdir("."):
    if os.path.isdir(directory):
        for image in os.listdir(directory):
            file = os.path.join(directory,image)
            
            image = Image.open(file)
            datetime = image._getexif()[36867]
            datetime = datetime.split(" ")
            date = datetime[0].split(":")
            time = datetime[1].split(":")
            new_filename = f"{date[0]}_{date[1]}_{date[2]}__{time[0]}_{time[1]}_{time[2]}.jpg"
            target_dir = os.path.join(TARGET,date[0])
            
            if not os.path.exists(target_dir):
                os.mkdir(os.path.join(target_dir))
            shutil.copy(file, os.path.join(target_dir,new_filename))