import argparse
import os
from glob import glob

from PIL import Image


def p2j(resize_file_name, path):
    '''get all the PNG images and convert it to jpg
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
    for file in glob(os.path.join(path, '*.png')):
        img = Image.open(file)
        image_name = os.path.split(file)[-1].split('.')[0]
        # print(image_name)
        save_path = os.path.join(dirName, image_name)
        img.save(save_path + '.jpg', 'JPEG')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Image conversion from png ==> jpeg')
    parser.add_argument('-file', '--image_path', type=str, required=True, help='Select the folder where images present')
    parser.add_argument('-loc', '--new_path', type=str, required=True, help='Save new folder for converted images')

    args = parser.parse_args()
    p2j(args.new_path, args.image_path)
