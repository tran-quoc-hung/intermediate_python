"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json

from models import NearEarthObject, CloseApproach

def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    neos = []
    with open(neo_csv_path, 'r') as neo_csv:
        neo_csv_reader = csv.reader(neo_csv)
        next(neo_csv_reader) # next header

        # create list NEO
        for row in neo_csv_reader:
            neo = NearEarthObject(row[3], row[4], row[15], True if row[7] == 'Y' else False)
            neos.append(neo)
    return neos

def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param cad_json_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    approaches = []
    with open(cad_json_path) as cad_json:
        cad = json.load(cad_json)

        # create list approache
        for cad_data in cad['data']:
            approache = CloseApproach(cad_data[0], cad_data[3], cad_data[4], cad_data[7])
            approaches.append(approache)

    return approaches
