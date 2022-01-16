import os
import logging

# DEBUG
# INFO
# WARNING
# ERROR
# CRITICAL
# Log formatters reference https://docs.python.org/3/library/logging.html#logrecord-attributes
def find_in_path(path, to_find):
    logging.info(f"Started looking in {path}")
    for tup in os.walk(path):
        for a_file in tup[2]:
            logging.log(logging.DEBUG, f"Looking in {a_file}")
            if os.path.splitext(a_file)[1] == ".txt":
                logging.info(f"Found a txt file in {path}")
                logging.log(logging.WARNING, f"Looking in {a_file}")
                with open(tup[0]+os.sep+a_file, "r") as txt_file:
                    if to_find in txt_file.read():
                        return tup[0]+os.sep+a_file

    return ""


def logging_example():
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler('search_files.log', 'w', 'utf-8')
    handler.setFormatter(logging.Formatter('[%(asctime)-15s]: %(message)s'))
    root_logger.addHandler(handler)

    print(find_in_path(r"C:\Users\ovatm\Dropbox\eventHorizon\Ar-Ge", "Tolga"))