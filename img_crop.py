import argparse
import os
from glob import glob

from PIL import Image
import dir_create

# import img_resize
from img_resize import check_1000x


def heigh_width_resize(value, scaleFactor):
    '''Accept the image size and scaleFactor
       return the Percentage value for image size to crop
    '''
    return int(value * scaleFactor)


def crop_to_size(resize_file_name, path, by_width=0, by_height=0):
    '''Accept the bulk images and crop it by width and height and save to new location provided
     path - BulkImage folder
     by_width - by width to crop
     by_height - by height to crop
     resize_file_name - new folder where cropped images to save
     '''
    # os.mkdir(path)
    dirName = dir_create.create_dir(resize_file_name, path)
    for file in glob(os.path.join(path, '*.*')):
        img = Image.open(file)
        image_path_and_name = os.path.split(file)
        save_path = os.path.join(dirName, image_path_and_name[1])
        width, height = img.size
        # scaleFactor = by_percentage / 100
        if width > by_width and height > by_height:
            # width, height = heigh_width_resize(width, scaleFactor), heigh_width_resize(height, scaleFactor)
            # imResize = crop_center(file,width,height by_width, by_height)
            imCrop = img.crop(((width - by_width) // 2,
                               (height - by_height) // 2,
                               (width + by_width) // 2,
                               (height + by_height) // 2))
            imCrop.save(save_path, 'JPEG')
        else:
            raise Exception(f'Please check for the heigh and width for image {file}')


def crop_to_percentage(resize_file_name, path, by_percentage=100):
    # def crop_to_percentage(path, by_percentage=100):
    # os.mkdir(path)
    dirName = dir_create.create_dir(resize_file_name, path)
    for file in glob(os.path.join(path, '*.*')):
        img = Image.open(file)
        image_path_and_name = os.path.split(file)
        save_path = os.path.join(dirName, image_path_and_name[1])
        width, height = img.size
        scaleFactor = by_percentage / 100
        by_width, by_height = heigh_width_resize(width, scaleFactor), heigh_width_resize(height, scaleFactor)
        check_1000x(width, height)
        if width > by_width and height > by_height:
            # width, height = heigh_width_resize(width, scaleFactor), heigh_width_resize(height, scaleFactor)
            # imResize = crop_center(file,width,height by_width, by_height)
            imCrop = img.crop(((width - by_width) // 2,
                               (height - by_height) // 2,
                               (width + by_width) // 2,
                               (height + by_height) // 2))
            imCrop.save(save_path, 'JPEG')
        else:
            raise Exception(f'Please check for the heigh and width for image {file}')


# crop_to('gajuEx3','C:/Users/gajanana_ganjigatti/Desktop/Images/',by_percentage=10, by_width=0,by_height=0)

# crop_to_percentage('gajuEx4','C:/Users/gajanana_ganjigatti/Desktop/Images/',by_percentage=10)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    subparsers = parser.add_subparsers(help='Choose a Crop by method.', dest='definition')

    parser_crp_pixel = subparsers.add_parser('crp_px', help='center crop images dimensions (width, height)')
    parser_crp_pixel.add_argument('-file', '--image_path', type=str, required=True,
                                  help='Select the folder where images present')
    parser_crp_pixel.add_argument('-loc', '--new_path', type=str, required=True,
                                  help='Save new folder for cropped images')
    parser_crp_pixel.add_argument('-wt', '--width', type=int, required=True, help='Image width to crop')
    parser_crp_pixel.add_argument('-ht', '--height', type=int, required=True, help='Image height to crop')

    parser_crp_percentage = subparsers.add_parser('crp_p', help='center crop images for percentage')
    parser_crp_percentage.add_argument('-file', '--image_path', type=str, required=True,
                                       help='Select the folder where images present')
    parser_crp_percentage.add_argument('-loc', '--new_path', type=str, required=True,
                                       help='Save new folder for cropped images')
    parser_crp_percentage.add_argument('-per', '--percentage', type=int, required=True,
                                       help='mention the percentage to crop image')

    args = parser.parse_args()
    if args.definition == 'crp_px':
        crop_to_size(args.new_path, args.image_path, args.width, args.height)
    elif args.definition == 'crp_p':
        crop_to_percentage(args.new_path, args.image_path, args.percentage)

# python img_crop.py crp_p -file C:\Users\gajanana_ganjigatti\Desktop\Images\ -loc backup1 -p 50
