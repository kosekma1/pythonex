#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Martin
#
# Created:     14/05/2018
# Copyright:   (c) Martin 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import json

def json_dir():
    print(dir(json))

def json_test():

    #json.load(f):   Load JSON data from file (or file-like object)
    #json.loads(s):   Load JSON data from a string (usually sent over internet)
    #json.dump(j, f):   Load JSON object to file (or file-like object)
    #json.dumps(j):     Output JSON object as string

    # load JSON from a file
    json_file = open("C:\Programy\PythonProjects\movie_1.txt", "r", encoding="utf-8")
    movie = json.load(json_file)  # covnert to dict and false, true, null convert to False, True and None python values
    json_file.close()

    print(movie)
    print(type(movie))
    print(movie["title"])
    print(movie["actors"])
    print(movie["release_year"])


    # load JSON as a string (over the net)
    value = """
    {   "title" : "Tron: Legacy",
        "composer" : "Daft Punk",
        "release_date" : 2010,
        "budget" : 170000000,
        "actors" : null,
        "won_oscar" : false
    }
    """

    tron = json.loads(value) #all characters are ASCII, no need encoding
    print(tron)

    # Convert dict to JSON (convert False, True, None to false, true, null etc. proper JSON format)
    print(json.dumps(movie))
    print(json.dumps(movie, ensure_ascii=False))  # Preserve non ASCII characters


def json_test2():
    """Dumpo JSON to file"""

    movie2 = {}
    movie2["title"] = "Minority Report"
    movie2["director"] = "Steven Spielberg"
    movie2["composer"] = "John Williams"
    movie2["actors"] = ["Tom Cruise", "Colin Farrell", "Samantha Morton", "Max von Sydow"]
    movie2["is_awesome"] = True
    movie2["budget"] = 102000000
    movie2["cinematographer"] = "Janusz Kami\u0144ski"

    file2 = open("C:\Programy\PythonProjects\movie_2.txt", "w", encoding="utf-8")
    json.dump(movie2, file2, ensure_ascii=False)  # our data contains non ASCII characters
    file2.close()


def main():
    #json_dir()
    #json_test()
    json_test2()
    pass

if __name__ == '__main__':
    main()
