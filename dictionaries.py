#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Martin
#
# Created:     10/05/2018
# Copyright:   (c) Martin 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def dictionaries():

    #dictionary is associative array or map in python it is called dictionary

    # FriendFace post
    # user_id = 209
    # message = "D5 E5 C5 C4 G4"
    # language = "English"
    # datetime = "20230215T124231Z"
    # location = (44.590533,-104,715556)

    # key : value
    # one way of creating dictionary
    post = {"user_id" : 209, "message" : "D5 E5 C5 C4 G4", "language" : "English",
    "datetime" : "20230215T124231Z", "location": (44.590533,-104,715556)}

    print(type(post))
    print(post)

    # the second way creating dictionary using dict keyword
    post2 = dict(message="SS Cotopaxi", language="English")
    print(post2)

    # adding key and values
    post2["user_id"] = 209
    post2["datetime"] = "19771116T093001Z"

    print(post2)

    # accessing data in dictionaries
    print(post2['message'])
    #print(post2['location']) #does not exist in list -> error
    #solving error
    #1. method testing
    if 'location' in post2:
        print(post2['location'])
    else:
        print("The post does not contain a location value")

    #2. method try
    try:
        print(post2['location'])
    except KeyError:
        print("The post does not contain a location value")


    #dir(post2)
    #help(post2.get)
    #3. method get
    loc = post2.get('location', None)
    print(loc)

    #1. method - iteration over all items
    for key in post.keys():
        value = post[key]
        print(key, "=", value)

    # dictionaries are not ordered data

    #2. method - iteration over all items
    for key, value in post.items():
        print(key, "=", value)

    # removing items
    print(post.pop("message"))
    print(post)

    print(post.popitem())  # random remove items - return tuple (key, value)
    print(post)

    post.clear() # remove all data
    print(post)



def main():
    dictionaries()
    pass

if __name__ == '__main__':
    main()
