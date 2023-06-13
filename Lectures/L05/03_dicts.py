from rich import print
import random


"""
Simple overview of dictionaries
Dictionaries are mutable and unordered since we access them by key.
"""
if __name__ == '__main__':
    # example of a dictionary
    person =  {
        "id": "0",
        "generation": "0",
        "fname": "Gustavus",
        "lname": "Banfill",
        "gender": "M",
        "birthDate": "7/21/1701",
        "deathDate": "2/9/1767",
        "age": 66,
        "marriedYear": "1719",
        "marriedAge": "18",
        "personality": "ESTP",
        "clanName": "Blacksteel",
        "spouseId": "",
        "fatherId": "",
        "motherId": "",
        "parentNodeId": "-1"
    }
    
    # print the dictionary
    print(person) 
    
    # access a value by key
    print(person["fname"])
    
    # add a new key-value pair
    person["height"] = 180
    
    # change a value
    person["parentNodeId"] = 5 # changes -1 to 5
    
    # remove a key-value pair
    del person["height"]
    # if we print person now, we see that height is gone
    
    # iterate over a dictionary (loop through all key-value pairs)
    # remember .items() returns a list of tuples that we can unpack
    for key, value in person.items():
        print(f"{key}: {value}")