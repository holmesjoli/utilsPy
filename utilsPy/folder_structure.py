import os

def remove_files(fls, pth = None):
    """
    Removes files from the current working directory
    :param fls: the files to remove
    :type fls: list
    """

    [os.remove(d) for d in fls if d in os.listdir(os.getcwd())]

def remove_dirs(dirs, pth = None):
    """
    Removes directories from the current working directory
    :param dirs: the directories to remove
    :type dirs: list
    """

    [os.rmdir(d) for d in dirs if d in os.listdir(os.getcwd())]

def create_dirs(dirs, pth = None):
    """
    Creates a file structure
    :param dirs: the directories to remove
    :type dirs: list
    """
    
    [os.mkdir(d) for d in dirs if not os.path.isdir(os.getcwd())]

