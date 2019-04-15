import unittest
import os
from utilsPy.config import read_json, read_yaml

class config_TestClass(unittest.TestCase):
 
    def __init__(self, *args, **kwargs):

        super(config_TestClass, self).__init__(*args, **kwargs)
        self.yaml_pth = "./utils/tests/test.yml"
        self.json_pth = "./utils/tests/test.json"

    def test_read_yaml(self):
        cu_yaml = read_yaml(self.yaml_pth)
       
        self.assertTrue(set(cu_yaml.keys()).issubset(set(["test1", "test2"])))
        self.assertTrue(set(cu_yaml["test1"].keys()).issubset(set(["test_var1", "test_var2"])))
        
    def test_read_config(self):
        cu_json = read_json(self.json_pth)

        self.assertTrue(set(cu_json.keys()).issubset(set(["test1", "test2"])))
        self.assertTrue(set(cu_json["test1"].keys()).issubset(set(["test_var1", "test_var2"])))

        
