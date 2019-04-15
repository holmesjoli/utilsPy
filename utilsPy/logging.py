import sys
from datetime import datetime

class logging(object):

    @classmethod
    def open_log(cls, fl):
        """
        Opens the log file
        :param fl: the name of the file 
        :type fl: str
        """

        cls.start_tm = datetime.now()
        cls.old_stdout = sys.stdout
        cls.log_file = open(fl, "w")
        cls.hash = "#"*80
        sys.stdout = cls.log_file
        print("Log file initiated on {}".format(cls.start_tm))
        print(cls.hash)

    @classmethod
    def close_log(cls):
        """
        Closes the log file
        """
        cls.end_tm = datetime.now()
        print(cls.hash)
        print("Log file close on {}".format(cls.end_tm))
        print("Took {} time to run".format(cls.end_tm - cls.start_tm))
        sys.stdout = cls.old_stdout
        cls.log_file.close()