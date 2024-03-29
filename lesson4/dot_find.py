#!/usr/bin/env python
"""
Your task is to write a query that will return all cars with width dimension
greater than 2.5. Please modify only the 'dot_query' function, as only that
will be taken into account.

Your code will be run against a MongoDB instance that we have provided.
If you want to run this code locally on your machine, you will need to install
MongoDB, download and insert the dataset. For instructions related to MongoDB
setup and datasets, please see the Course Materials.
"""


def dot_query():
    # Edit the line below with your query - try to use dot notation.
    # You can check out example_auto.txt for an example of the document
    # structure in the collection.
    query = {"dimensions.width": {"$gt": 2.5}}
    return query


# Do not edit code below this line in the online code editor.
# Code here is for local use on your own computer.
def get_db():
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client.examples
    return db


if __name__ == "__main__":
    db = get_db()
    query = dot_query()
    cars = db.cars.find(query)

    print("Printing first 3 results\n")
    import pprint
    for car in cars[:3]:
        pprint.pprint(car)

#OUTPUT:-Found autos: 34
# Printing first 3 results

# {u'dimensions': {u'length': 39.9288, u'weight': 2721000.0, u'width': 34.7472},
#  u'name': u'Crawler-transporter'}
# {u'dimensions': {u'length': 16.5, u'width': 3.7}, u'name': u'Thrust SSC'}
# {u'dimensions': {u'height': 7.4,
#                  u'length': 14.5,
#                  u'wheelbase': 6.4008,
#                  u'width': 8.7},
#  u'name': u'Liebherr T 282B'}