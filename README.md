
# Python Modules

# Module Introduction
# Import Variants

## Modules Introduction:
__1.__ what are modules in python?
		
  Mainly a file containing python code and Objects of type ModuleType, a file with .py extentions are called modules in python.
		__example.py__ as Module
		
	def print_hello():
		'''This block prints Hello School of AI'''
		print('Hello School of AI')
	
__2.__ How Doest python loads Module?
		
  An import statement is made up of the import keyword along with the name of the module.
	
__3.__ How to __import hello__ without import statement?
  
  *The first thing Python will do is look up the name hello in __sys.modules__. This is a cache of all modules that have been previously imported.*
  
  *If the name isn’t found in the module cache, Python will proceed to search through a list of built-in modules. These are modules that come pre-installed with Python and can be     found in the Python Standard Library. If the name still isn’t found in the built-in modules, Python then searches for it in a list of directories defined by __sys.path__. This   list usually includes the current directory, which is searched first.*
  
  *When Python finds the module, it binds it to a name in the local scope. This means that abc is now defined and can be used in the current file without throwing a __NameError__.*

## Below Changes to be implemented
### Create these modules:
  1. jpg/jpeg to png conversion (use PIL library) __[j2p](https://github.com/Gaju27/session11/blob/main/j2p.py)__
  2. png to jpg conversion (use PIL library) __[p2j](https://github.com/Gaju27/session11/blob/main/j2p.py)__
### Image resizer that can resize bulk images with these features:
  1. resize by user determined percentage (say 50% for height and width) (proportional) __[res_p](https://github.com/Gaju27/session11/blob/main/img_resize.py#L22)__
  2. resize by user determined width (proportional) __[res_w](https://github.com/Gaju27/session11/blob/main/img_resize.py#L48)__
  3. resize by user determined height (proportional) __[res_h](https://github.com/Gaju27/session11/blob/main/img_resize.py#L71)__
### Image cropper that can crop bulk images with these features:
  1. center square/rectangle crop by user-determined pixels __[crp_px](https://github.com/Gaju27/session11/blob/main/img_crop.py)__
  2. centre square/rectangle crop by user-determined percentage (crop to 50%/70%) __crp_p__
  3. it let's user know which all images were not cropped due to size mismatches
### A ____main____ module that exposes all these features (using argparse)
  1. Finally create an [zipped app](https://github.com/Gaju27/session11/blob/main/image_converter), that exposes all of these features

# Function used
  * crp_px
  * crp_p
  * res_p
  * res_w
  * res_h
  * p2j
  * j2p
