import csv
import re

# Open specified csv file and read data from file.
# Warning: when files are updated and their names get changed, you
#   must update the hard coded file name in DataBuilder.py
def dict_builder(path=""):
    location = path
    data_dictionary = dict()

    with open(path, "r") as fin:
        reader = csv.DictReader(fin)

        for frow in reader:
            tempdict = dict()
            for cn, values in frow.items():
                if values != "":
                    tempdict[cn] = values
            row_id = frow[[*frow.keys()][0]]
            if re.match(r".*Root Table.*", location, re.IGNORECASE):
                data_dictionary[row_id] = tempdict
            else:
                data_dictionary[row_id.lower()] = tempdict

    return data_dictionary