"""Write a stream of close approaches to CSV or to JSON.

This module exports two functions: `write_to_csv` and `write_to_json`, each of
which accept an `results` stream of close approaches and a path to which to
write the data.

These functions are invoked by the main module with the output of the `limit`
function and the filename supplied by the user at the command line. The file's
extension determines which of these functions is used.

You'll edit this file in Part 4.
"""
import csv
import json
import helpers

def write_to_csv(results, filename):
    """Write an iterable of `CloseApproach` objects to a CSV file.

    The precise output specification is in `README.md`. Roughly, each output row
    corresponds to the information in a single close approach from the `results`
    stream and its associated near-Earth object.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should be saved.
    """
    fieldnames = (
        'datetime_utc', 'distance_au', 'velocity_km_s',
        'designation', 'name', 'diameter_km', 'potentially_hazardous'
    )
    # TODO: Write the results to a CSV file, following the specification in the instructions.
    datas = []
    for rs in results:
        item = {}
        item['datetime_utc'] = rs.time
        item['distance_au'] = rs.distance
        item['velocity_km_s'] = rs.velocity
        item['designation'] = rs._designation
        item['name'] = None if rs.neo.name == '' or rs.neo.name is None else rs.neo.name
        item['diameter_km'] = 'nan' if rs.neo.diameter == '' or rs.neo.diameter is None else rs.neo.diameter
        item['potentially_hazardous'] = 'True' if rs.neo.hazardous else 'False'
        datas.append(item)

    with open(filename, 'w') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(datas)


def write_to_json(results, filename):
    """Write an iterable of `CloseApproach` objects to a JSON file.

    The precise output specification is in `README.md`. Roughly, the output is a
    list containing dictionaries, each mapping `CloseApproach` attributes to
    their values and the 'neo' key mapping to a dictionary of the associated
    NEO's attributes.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should be saved.
    """
    # TODO: Write the results to a JSON file, following the specification in the instructions.
    datas = []
    for rs in results:
        item = {}
        neo = {}
        item['datetime_utc'] = helpers.datetime_to_str(rs.time)
        item['distance_au'] = float(rs.distance)
        item['velocity_km_s'] = float(rs.velocity)
        neo['designation'] = rs._designation
        neo['name'] = '' if rs.neo.name == '' or rs.neo.name is None else rs.neo.name
        neo['diameter_km'] = float('nan') if rs.neo.diameter is None else rs.neo.diameter
        neo['potentially_hazardous'] = rs.neo.hazardous
        item['neo'] = neo
        datas.append(item)

    with open(filename, 'w') as file:
        json.dump(datas, file)

