#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
In this problem set you work with cities infobox data, audit it, come up with a
cleaning idea and then clean it up.

In the previous quiz you recognized that the "name" value can be an array (or
list in Python terms). It would make it easier to process and query the data
later if all values for the name are in a Python list, instead of being
just a string separated with special characters, like now.

Finish the function fix_name(). It will recieve a string as an input, and it
will return a list of all the names. If there is only one name, the list will
have only one item in it; if the name is "NULL", the list should be empty.
The rest of the code is just an example on how this function can be used.
"""
import codecs
import csv
import pprint

CITIES = '/Users/xiaonili/Problem_set3/Quiz5/cities.csv'


def fix_name(name):

    if name.startswith('{'):
        name = name.replace('{', '').replace('}', '').split('|')
    elif name == 'NULL':
        name = []
    else:
        name = [name]

    # YOUR CODE HERE

    return name


def process_file(filename):
    data = []
    with open(filename, "r") as f:
        reader = csv.DictReader(f)
        #skipping the extra metadata
        for _ in range(3):
            reader.__next__()
        # processing file
        for line in reader:
            # calling your function to fix the area value
            if "name" in line:
                line["name"] = fix_name(line["name"])
            data.append(line)
    return data


def test():
    data = process_file(CITIES)

    print("Printing 20 results:")
    for n in range(20):
        pprint.pprint(data[n]["name"])
        
        # print(data[14]["name"])
        # print(data[9]["name"])
        # print(data[3]["name"])

    assert(data[14]["name"] != ['Negtemiut', 'Nightmute'])
    assert(data[9]["name"] != ['Pell City Alabama'])
    assert(data[3]["name"] == ['Kumhari'])

if __name__ == "__main__":
    test()

#OUTPUT
# Printing 20 results:
# ['Kud']
# ['Kuju']
# ['Kumbhraj']
# ['Kumhari']
# ['Kunigal']
# ['Kurgunta']
# ['Athens']
# ['Demopolis']
# ['Chelsea Alabama']
# ['Pell City Alabama']
# ['City of Northport']
# ['Sand Point']
# ['Unalaska Alaska']
# ['City of Menlo Park']
# ['Negtemiut', 'Nightmute']
# ['Fairbanks Alaska']
# ['Homer']
# ['Ketchikan Alaska']
# ['Nuniaq', 'Old Harbor']
# ['Rainier Washington']