import argparse
import os
from glob import glob

from PIL import Image

from dir_create import create_dir


# def heigh_width_resize(value, scaleFactor):
#     return int(value * scaleFactor)
import img_crop


def check_1000x(width, height):
    if width > 1000 and height > 1000:
        pass
    else:
        raise ValueError("Image resolution greater than 1000 X 1000. ")


def resize_by_percentage(resize_file_name, path, by_percentage=100, by_width=0, by_height=0):
    # os.mkdir(path)
    ''' this funciton help to resize images based on any of the inputs
    res_p: by percentage
    res_w by width
    res_h by height
    you need to provide image folder location and new folder name where you expect the
    new resize images to stored'''
    dirName = create_dir(resize_file_name, path)
    for file in glob(os.path.join(path, '*.*')):
        img = Image.open(file)
        image_path_and_name = os.path.split(file)
        save_path = os.path.join(dirName, image_path_and_name[1])
        width, height = img.size
        if by_percentage != 100:
            scaleFactor = by_percentage / 100
            check_1000x(width, height)
            width, height = img_crop.heigh_width_resize(width, scaleFactor), img_crop.heigh_width_resize(height, scaleFactor)
            imResize = img.resize((width, height), Image.ANTIALIAS)
            imResize.save(save_path, 'png')
        else:
            raise Exception("100 % has no impact and no changes to the images")




def resize_by_width(resize_file_name, path, by_width=0):
    # os.mkdir(path)
    ''' this funciton help to resize images based on any of the inputs
    res_p: by percentage
    res_w by width
    res_h by height
    you need to provide image folder location and new folder name where you expect the
    new resize images to stored'''
    dirName = create_dir(resize_file_name, path)
    for file in glob(os.path.join(path, '*.*')):
        img = Image.open(file)
        image_path_and_name = os.path.split(file)
        save_path = os.path.join(dirName, image_path_and_name[1])
        width, height = img.size
        check_1000x(width, height)
        if width > by_width:

            imResize = img.resize((by_width, height), Image.ANTIALIAS)
            imResize.save(save_path, 'png')
        else:
            raise Exception(f'Please check for the heigh and width for image {file}')


def resize_by_height(resize_file_name, path, by_height=0):
    # os.mkdir(path)
    ''' this funciton help to resize images based on any of the inputs
    res_p: by percentage
    res_w by width
    res_h by height
    you need to provide image folder location and new folder name where you expect the
    new resize images to stored'''
    dirName = create_dir(resize_file_name, path)
    for file in glob(os.path.join(path, '*.*')):
        img = Image.open(file)
        image_path_and_name = os.path.split(file)
        save_path = os.path.join(dirName, image_path_and_name[1])
        width, height = img.size
        check_1000x(width, height)
        if height > by_height:
            imResize = img.resize((width, by_height), Image.ANTIALIAS)
            imResize.save(save_path, 'png')
        else:
            raise Exception(f'Please check for the heigh and width for image {file}')


# resize_to('gaju1right','C:/Users/gajanana_ganjigatti/Desktop/Images/', by_height=1)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    subparsers = parser.add_subparsers(help='Choose a resize option by method to resize bulk images.',
                                       dest='resize_function')

    parser_res_per = subparsers.add_parser('res_p', help='resize by user determined percentage')
    parser_res_per.add_argument('-file', '--image_path', type=str, required=True,
                                help='Select the folder where images present')
    parser_res_per.add_argument('-loc', '--new_path', type=str, required=True,
                                help='Save new folder for resized images')
    parser_res_per.add_argument('-per', '--percentage', type=int, required=True,
                                help='Image width to resize by percentage between 0 too 100')

    parser_res_w = subparsers.add_parser('res_w', help='Resize by user defined width value')
    parser_res_w.add_argument('-file', '--image_path', type=str, required=True,
                              help='Select the folder where images present')
    parser_res_w.add_argument('-loc', '--new_path', type=str, required=True,
                              help='Save new folder for resized images')
    parser_res_w.add_argument('-wt', '--width', type=int, required=True, help='Image width to resize')

    parser_res_w = subparsers.add_parser('res_h', help='Resize by user defined height value')
    parser_res_w.add_argument('-file', '--image_path', type=str, required=True,
                              help='Select the folder where images present')
    parser_res_w.add_argument('-loc', '--new_path', type=str, required=True,
                              help='Save new folder for resized images')
    parser_res_w.add_argument('-ht', '--height', type=int, required=True, help='Image height to resize')

    args = parser.parse_args()
    if args.resize_function == 'res_p':
        resize_by_percentage(args.new_path, args.image_path, args.percentage)
    elif args.resize_function == 'res_w':
        resize_by_width(args.new_path, args.image_path, args.width)
    elif args.resize_function == 'res_h':
        resize_by_height(args.new_path, args.image_path, args.height)
