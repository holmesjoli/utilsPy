# About

The utilsPy package contains general utility functions.

## Col Types

Tests pandas series for column types.

* `test_ser_str`: Tests if the series is a string
* `test_ser_num`: Tests if the series is number
* `test_ser_int`: Tests if the series is an integer
* `test_ser_flt`: Tests if the series is a float
* `test_ser_cmplx`: Tests if the series is complex
* `test_ser_bool`: Tests if the series is boolean

## Config

Contains functions related to reading in and updating configuration files.

* `read_yaml`: Reads in a yaml file
* `read_json`: Reads in a json file
* `update_yaml`: Writes out the updated config file to a new yaml file

## Folder Structure

The folder structure module contains functions:

* `create_dirs`: Creates a file structure
* `remove_files`: Removes files from the current working directory
* `remove_dirs`:

## Logging

The logging module contains several functions as part of the logging class:

* `open_log`: Opens the log file
* `close_log`: Closes the log file

`open_log` takes an argument fl, the name of the log file. The log functions also initiate time, so that it's easy to know how long a script file takes to run and logs the output all in one place. 
