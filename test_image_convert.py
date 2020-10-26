import inspect
import os
import re
from glob import glob

from PIL import Image

import img_crop
import img_resize
import j2p
import p2j
import pytest

all_modules = [j2p, p2j, img_resize, img_crop]

README_CONTENT_CHECK_FOR = [
    'crp_px',
    'crp_p',
    'res_p',
    'res_w',
    'res_h',
    'p2j',
    'j2p',

]

path = 'image_store/'



def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"


def test_readme_contents():
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 100, "Make your README.md file interesting! Add atleast 100 words"


def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"


def test_readme_file_for_formatting():
    f = open("README.md", "r")
    content = f.read()
    f.close()
    assert content.count("#") >= 5


def test_indentations():
    for each_module in all_modules:
        lines = inspect.getsource(each_module)
        spaces = re.findall('/n +.', lines)
        for space in spaces:
            assert len(space) % 4 == 2, f"Your script {each_module} contains misplaced indentations"
            assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"


def test_function_name_had_cap_letter():
    for each_module in all_modules:
        functions = inspect.getmembers(each_module, inspect.isfunction)
        for function in functions:
            assert len(
                re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"


def test_for_20_images():
    assert len(os.listdir(path)) >= 20, "Must have more the 20 images in image store"


def test_for_20_jpeg_images():
    for file in glob(os.path.join(path, '*.*')):
        img = Image.open(file)
        assert img.format == 'JPEG', "20 Images must be JPEG"


def test_for_backup_file_absent():
    new_path = path + 'backup_store'
    isdir = os.path.isdir(new_path)
    assert bool(isdir) is False, "Lets check for the back folder to store the cropped/resized images"


# @pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+4", 6), ("6*9", 42)])
# def test_eval(test_input, expected):
#     assert eval(test_input) == expected
def test_images_for_1000X1000_true():
    with pytest.raises(ValueError):
        im = Image.open(r'C:/Users/gajanana_ganjigatti/Documents/Gaju_data/github/image_converter/png_4.png')
        wt, ht = im.size
        img_resize.check_1000x(wt, ht)


def test_zip_convert_png():
    command = f'python image_con j2p -loc "resize_store_png" -file {path}'
    command_run = os.system(command)
    assert command_run == 1, "Image Converts from jpeg to png"


def test_folder_resize_store_png():
    new_path = path + 'resize_store_png'
    isdir = os.path.isdir(new_path)
    assert bool(isdir) is True, "This test confirms whether test_folder_resize_store_png ran successful "


def test_zip_resize_percentage_80():
    command = f'python image_con res_p -file {path} -loc "resize_store_per" -per 80'
    command_run = os.system(command)
    assert command_run == 0, "resize image by 80%"


def test_folder_resize_store_percentage():
    new_path = path + 'resize_store_per'
    isdir = os.path.isdir(new_path)
    assert bool(isdir) is True, "This test confirms whether test_folder_resize_store_png ran successful "


def test_zip_convert_jpg():
    command = f'python image_con p2j -loc "resize_store_jpg" -file {path}/resize_store_png/'
    command_run = os.system(command)
    assert command_run == 1, "Image Converts from png to jpg"


def test_folder_resize_store_jpg():
    new_path = path + 'resize_store_png' + '/resize_store_jpg'
    isdir = os.path.isdir(new_path)
    assert bool(isdir) is True, "This test confirms whether test_folder_resize_store_jpg ran successful "


def test_zip_resize_to_500_width():
    command = f'python image_con res_w -file {path} -loc "resize_store_width" -wt 500'
    command_run = os.system(command)
    assert command_run == 0, "Image Resize by Width Success"


def test_folder_resize_store_for_resize_to_500_width():
    new_path = path + 'resize_store_width'
    isdir = os.path.isdir(new_path)
    assert bool(isdir) is True, "This test confirms whether test_folder_resize_store_for_resize_to_500_width ran successful "


def test_zip_resize_to_500_height():
    command = f'python image_con res_h -file {path} -loc "resize_store_height" -ht 500'
    command_run = os.system(command)
    assert command_run == 0, "Image Resize by height Success"


def test_folder_resize_store_for_resize_to_500_height():
    new_path = path + 'resize_store_height'
    isdir = os.path.isdir(new_path)
    assert bool(isdir) is True, "This test confirms whether test_folder_resize_store_for_resize_to_500_height ran successful "

def test_zip_center_crop_224x224():
    command = f'python image_con crp_px -file {path} -loc "center_crop_224x224" -wt 224 -ht 224'
    command_run = os.system(command)
    assert command_run == 1, "center crop to 224x224"


def test_folder_center_crop_224x224():
    new_path = path + 'center_crop_224x224'
    isdir = os.path.isdir(new_path)
    assert bool(isdir) is True, "This test confirms whether test_folder_resize_store_png ran successful "
