#!/usr/bin/python3
"""
Defines a base class for all other classes in the project.
"""

import json
import os
import csv


class Base:
    """
    Base class to manage the id attribute for all future classes
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a new Base instance

        Args:
            id (int): The id of the instance. If None, the id is set to
            the next available id.
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Return the JSON str representation of a list of dicts

        Args:
            list_dictionaries (list): list of dicts

        Returns:
            str: the JSON str representation of list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"

        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """
        Return the list represented by a JSON str

        Args:
            json_string (str): a str representing a list of dicts

        Returns:
            list: the list represented by json_string
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Write the JSON str representation of list_objs to a file

        Args:
            list_objs (list): list of instances that inherit from Base
        """
        filename = "{}.json".format(cls.__name__)

        with open(filename, 'w') as file:
            if list_objs is None:
                file.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                file.write(cls.to_json_string(list_dicts))

    @classmethod
    def create(cls, **dictionary):
        """
        Return an instance will all attributes already set

        Args:
            **dictionary: a dict of attributes to set

        Returns;
            An instance of the class with attributes set
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)  # create a dummy rectangle instance
        elif cls.__name__ == "Square":
            dummy = cls(1)  # create a dummy square instance

        # update the dummy instance with real values
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Return a list of instances from a JSON file

        Returns:
            list: a list of instances of the class
        """
        filename = "{}.json".format(cls.__name__)
        if not os.path.exists(filename):
            return []

        with open(filename, 'r') as file:
            json_string = file.read()
            list_dicts = cls.from_json_string(json_string)
            return [cls.create(**d) for d in list_dicts]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Write the CSV str representation of list_objs to a file
        """
        filename = "{}.csv".format(cls.__name__)

        with open(filename, 'w', newline="") as csvfile:
            if list_objs is None or len(list_objs) == 0:
                csvfile.write("")
            else:
                writer = csv.writer(csvfile)

                if cls.__name__ == "Rectangle":
                    for obj in list_objs:
                        writer.writerow([
                            obj.id, obj.width, obj.height, obj.x, obj.y
                            ]
                        )
                elif cls.__name__ == "Square":
                    for obj in list_objs:
                        writer.writerow([
                            obj.id, obj.size, obj.x, obj.y
                            ]
                        )

    @classmethod
    def load_from_file_csv(cls):
        """
        Return a list of instances from a CSV file
        """
        filename = "{}.csv".format(cls.__name__)

        if not os.path.exists(filename):
            return []

        with open(filename, 'r') as csvfile:
            reader = csv.reader(csvfile)
            list_dicts = []
            if cls.__name__ == "Rectangle":
                for row in reader:
                    list_dicts.append({
                        'id': int(row[0]),
                        'width': int(row[1]),
                        'height': int(row[2]),
                        'x': int(row[3]),
                        'y': int(row[4])
                    })
            elif cls.__name__ == 'Square':
                for row in reader:
                    list_dicts.append({
                        'id': int(row[0]),
                        'size': int(row[1]),
                        'x': int(row[2]),
                        'y': int(row[3])
                    })

            return [cls.create(**d) for d in list_dicts]
