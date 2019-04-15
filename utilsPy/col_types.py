import numpy as np
import pandas as pd
from datetime import datetime

class col_types(object):
    """Pandas series type testing functions"""

    def __init__(self):

        self.types = {"char_string": np.object_,
                      "string": np.object_,
                      "str": np.object_,
                      "number": np.number,
                      "numeric": np.number,
                      "integer": np.int64,
                      "int": np.int64,
                      "float": np.float64,
                      "flt": np.float64,
                      "double": np.float64,
                      "complex": np.complex128,
                      "boolean": np.bool_,
                      "bool": np.bool_,
                      "datetime": datetime,
                      "date": datetime}

    def get_type(self, key):

        try:
            return self.types[key.lower()]

        except KeyError:

            raise ValueError("Expects type to be one of the following values in upper or lowercase: \n{}".format("\n".join(self.types.keys())))

    @staticmethod
    def test_ser_str(ser):
        """

        Tests to see if the series is a string
        :param ser: the series to test
        :type ser: pandas series
        :returns: True or False
        :rtype: boolean
        """

        if ser.dtype == "object":
            return True
        else: 
            return False

    @staticmethod
    def test_ser_num(ser):
        """

        Tests to see if the series is number
        :param ser: the series to test
        :type ser: pandas series
        :returns: True or False
        :rtype: boolean
        """
        if np.issubdtype(ser.dtype, np.number):
            return True
        else:
            return False

    @staticmethod
    def test_ser_int(ser):
        """

        Tests to see if the series is a string
        :param ser: the series to test
        :type ser: a pandas series
        :returns: True or False
        :rtype: boolean
        """

        if ser.dtype == np.int64:
            return True
        else: 
            return False

    @staticmethod
    def test_ser_flt(ser):
        """

        Tests to see if the series is a float
        :param ser: the series to test
        :type ser: a pandas series
        :returns: True or False
        :rtype: boolean
        """

        if ser.dtype == np.float64:
            return True
        else:
            return False

    @staticmethod
    def test_ser_cmplx(ser):
        """

        Tests to see if the series is complex
        :param ser: the series to test
        :type ser: a pandas series
        :returns: True or False
        :rtype: boolean
        """

        if ser.dtype == np.complex128:
            return True
        else:
            return False

    @staticmethod
    def test_ser_date(ser):
        """

        Tests to see if the series is a date
        :param ser: the series to test
        :type ser: a pandas series
        :returns: True or False
        :rtype: boolean
        """

    @staticmethod
    def test_ser_datetime(ser):
        """

        Tests to see if the series is a datetime
        :param ser: the series to test
        :type ser: a pandas series
        :returns: True or False
        :rtype: boolean
        """

    @staticmethod
    def test_ser_spatial(ser):
        """

        Tests to see if the series is spatial
        :param ser: the series to test
        :type ser: a pandas series
        :returns: True or False
        :rtype: boolean
        """

    @staticmethod
    def test_ser_bool(ser):
        """

        Tests to see if the series is boolean
        :param ser: the series to test
        :type ser: a pandas series
        :returns: True or False
        :rtype: boolean
        """

        if ser.dtype == bool:
            return True
        else:
            return False

