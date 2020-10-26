# Main
import argparse

from img_crop import crop_to_size, crop_to_percentage
# from img_resize import *
from img_resize import resize_by_percentage, resize_by_width, resize_by_height
from j2p import j2p
from p2j import p2j




print(f'Main running __name__ = {__name__}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    subparsers = parser.add_subparsers(help='Please select image resize/cropping methods.', dest='definition')

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

    parser_p2j = subparsers.add_parser('p2j', help='Image conversion from png ==> jpeg')
    parser_p2j.add_argument('-file', '--image_path', type=str, required=True,
                            help='Select the folder where images present')
    parser_p2j.add_argument('-loc', '--new_path', type=str, required=True, help='Save new folder for converted images')

    parser_j2p = subparsers.add_parser('j2p', help='Image conversion from jpeg ==> png')
    parser_j2p.add_argument('-file', '--image_path', type=str, required=True,
                            help='Select the folder where images present')
    parser_j2p.add_argument('-loc', '--new_path', type=str, required=True, help='Save new folder for converted images')

    args = parser.parse_args()
    if args.definition == 'crp_px':
        crop_to_size(args.new_path, args.image_path, args.width, args.height)
    elif args.definition == 'crp_p':
        crop_to_percentage(args.new_path, args.image_path, args.percentage)
    elif args.definition == 'res_p':
        resize_by_percentage(args.new_path, args.image_path, args.percentage)
    elif args.definition == 'res_w':
        resize_by_width(args.new_path, args.image_path, args.width)
    elif args.definition == 'res_h':
        resize_by_height(args.new_path, args.image_path, args.height)
    elif args.definition == 'p2j':
        p2j(args.new_path, args.image_path)
    elif args.definition == 'j2p':
        j2p(args.new_path, args.image_path)
