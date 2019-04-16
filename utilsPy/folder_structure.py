import os
import shutil

def create_files(fls):
    """
    Creates files
    :param fls: the files to create
    :type fls: list
    """

    [open(d, 'w') for d in fls if not os.path.exists(d)]

def create_dirs(dirs):
    """
    Creates a file structure
    :param dirs: the directories to create
    :type dirs: list
    """
    
    [os.mkdir(d) for d in dirs if not os.path.isdir(d)]

def remove_files(fls):
    """
    Removes files from the current working directory
    :param fls: the files to remove
    :type fls: list
    """

    [os.remove(d) for d in fls if os.path.exists(d)]

def remove_dirs(dirs):
    """
    Removes directories from the current working directory
    :param dirs: the directories to remove
    :type dirs: list
    """

    [shutil.rmtree(d) for d in dirs if os.path.exists(d)]
