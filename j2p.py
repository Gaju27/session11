import argparse
import os
from glob import glob

from PIL import Image


def j2p(resize_file_name, path):
    '''get all the jpeg/jpg images and convert it to PNG
               format to the new location requested
    '''
    dirName = os.path.join(path, resize_file_name)
    '''
           here it check for the directory / folder name for resized images 
           if exists does nothing if not it creates one and stores the resized images into it.
    '''
    try:
        # Create target Directory
        os.mkdir(dirName)
        print("Directory ", dirName, " Created ")
    except FileExistsError:
        print("Directory ", dirName, " already exists")
    for file in glob(os.path.join(path, '*.*')):
        img = Image.open(file).convert('RGB')
        image_name = os.path.split(file)[-1].split('.')[0]
        # print(image_name)
        save_path = os.path.join(dirName, image_name)
        img.save(save_path + '.png', 'PNG')


# j2p('latest_path', 'C:/Users/gajanana_ganjigatti/Desktop/Images/gajuEx2')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Image conversion from jpg or jpeg ==> png' )
    parser.add_argument('-file', '--image_path', type=str, required=True, help='Select the folder where images present')
    parser.add_argument('-loc', '--new_path', type=str, required=True, help='Save new folder for cropped images')

    args = parser.parse_args()
    j2p(args.new_path, args.image_path)

# python j2p.py -file C:\Users\gajanana_ganjigatti\Desktop\Images\gajuEx2\latest_path -loc back_loc