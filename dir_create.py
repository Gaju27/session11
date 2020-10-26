import os


def create_dir(new_file_name,path):
    dirName = os.path.join(path, new_file_name)
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
    return dirName