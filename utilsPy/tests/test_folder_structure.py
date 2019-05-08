import os
import unittest
from utilsPy.folder_structure import create_files, create_dirs, remove_files, remove_dirs

class folderStructureTestClass(unittest.TestCase):
    def __init__(self, *args, **kwargs):

        super(folderStructureTestClass, self).__init__(*args, **kwargs)

        self.dirs = ["test_folder1", "test_folder2"]
        self.fls = ["test_folder1/test_fl1.txt", "test_folder1/test_fl2.txt"]

    def test_create_dirs(self):
        create_dirs(self.dirs)
        self.assertTrue(all([os.path.exists(d) for d in self.dirs]))

    def test_create_fls(self):
        create_files(self.fls)
        self.assertTrue(all([os.path.exists(d) for d in self.fls]))

    def test_remove_fls(self):
        remove_files(self.fls)
        self.assertFalse(all([os.path.exists(d) for d in self.fls]))

    def test_remove_dirs(self):
        remove_dirs(self.dirs)
        self.assertFalse(all([os.path.exists(d) for d in self.dirs]))
