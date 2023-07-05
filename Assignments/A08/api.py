
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import csv



description = """🚀
## 4883 Software Tools
### Where awesomeness happens
"""


app = FastAPI(

    description=description,

)

db = []

# Open the CSV file
# populates the `db` list with all the csv data
with open('data.csv', 'r') as file:
    # Create a CSV reader object
    reader = csv.reader(file)

    i = 0
    # Read each row in the CSV file
    for row in reader:
        if i == 0:
            i += 1
            continue
        db.append(row)


def getUniqueCountries():
    global db
    countries = {}

    for row in db:
        print(row)
        if not row[2] in countries:
            countries[row[2]] = 0

    return list(countries.keys())

def getUniqueWhos():
    global db
    whos = {}

    for row in db:
        print(row)
        if not row[3] in whos:
            whos[row[3]] = 0
   
    return list(whos.keys())

@app.get("/")
async def docs_redirect():
    """Api's base route that displays the information created above in the ApiInfo section."""
    return RedirectResponse(url="/docs")

@app.get("/countries/")
async def countries():

    return {"countries":getUniqueCountries()}


@app.get("/whos/")
async def whos():

    return {"whos":getUniqueWhos()}

@app.get("/casesByRegion/")
async def casesByRegion(year:int = None):
    """
    Returns the number of cases by region

    """

    # create a dictionary as a container for our results
    # that will hold unique regions. Why, because there 
    # cannot be duplicate keys in a dictionary.
    cases = {}

    # return {'success':False,'message':'no database exists'}

    # loop through our db list
    for row in db:
        
        # If there is a year passed in and that year is not equal to this row
        # then skip the rest of code
        if year != None and year != int(row[0][:4]):
            continue
            
        # this line guarantees that the dictionary has the region as a key
        if not row[3] in cases:
            cases[row[3]] = 0
        
        # this line adds the case count to whatever is at that key location
        cases[row[3]] += int(row[4])    

    # return cases

    return {"data":cases,"success":True,"message":"Cases by Region","size":len(cases),"year":year}



my_list = ['apple', 'banana', 'cherry', 'date', 'elderberry']

@app.get("/get_values1/")
def get_values1(index1: int=None, index2: int=None):
    try:
        value1 = my_list[index1]
        value2 = my_list[index2]
        return [value1, value2]
    except IndexError:
        return {"error": "Invalid index provided."}


@app.get("/get_values2/{index1}/{index2}")
def get_values2(index1: int, index2: int):
    try:
        value1 = my_list[index1]
        value2 = my_list[index2]
        return [value1, value2]
    except IndexError:
        return {"error": "Invalid index provided."}
    


if __name__ == "__main__":
    uvicorn.run("api:app", host="127.0.0.1", port=5000, log_level="debug", reload=True) #host="127.0.0.1"
