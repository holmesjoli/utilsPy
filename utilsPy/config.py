import yaml
import json

def read_yaml(pth):
    """

    Reads in a yaml file
    :param pth: the path to the yaml config file
    :type pth: str
    :returns: the config file
    :rtype: dct
    """
    with open(pth, "r", encoding = "utf-8") as cf:
        return yaml.load(cf)

def read_json(pth):
    """

    Reads in a json file
    :param pth: the path to the yaml config file
    :type pth: str
    :returns: the config file
    :rtype: dct
    """
    with open(pth, "r", encoding = "utf-8") as cf:
        return json.load(cf)

def update_yaml(pth, config):
    """

    Writes out the updated config file to a new yaml file
    :param pth: the path to the yaml config file
    :type pth: str
    :param config: the configuration file to write out
    :type config: dct
    """
    with open(pth, "w") as cf:
            yaml.dump(config, cf, default_flow_style = True, default_style = '"')
