def rtnFls(ftype, pths):
    """
    Returns a list of the fls with the specified ending
    :param ftype:
    :type ftype: str
    :param pths: list of paths, e.g. ["data.csv", "data.sav"]
    :type pths: str
    """
    return [l for l in pths if l.endswith(ftype)]
