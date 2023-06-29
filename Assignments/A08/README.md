## Assignment 8 - Fast Api with Covid Data

#### Due: 07-05-2023 (Wednesday @ 10:10 a.m.)

### Overview:

Create a RESTful API using FastAPI that provides access to COVID-19 data. The API will fetch the data from a publicly available data source and expose endpoints to retrieve various statistics related to COVID-19 cases.

### Addendum

I made a mistake yesterday when I stated that I prefer `RPC` (Remote Procedure Calls) type API's over RESTful api's. Previous reading had me believe that `RPC` was less structured than a `RESTful API`, but really `REST` = `stateless` or "call and forget" where `RPC` = `maintain state` meaning stay connected.

I would explain more with examples here, but that would take too long.

### RESTful

I'm putting a description of what restful is here not as part of the program requirements, but just as a little learning nugget.

- REST (Representational State Transfer) is an architectural style used for designing networked applications.
- RESTful APIs are based on the principles of REST and are widely used for web services.
- RESTful APIs utilize standard HTTP methods (GET, POST, PUT, DELETE) to perform CRUD (Create, Read, Update, Delete) operations on resources.
- RESTful APIs are stateless, meaning each request contains all the necessary information for the server to process it.
- RESTful APIs typically use JSON or XML as the data interchange format.
- RESTful APIs are often more scalable and easier to consume by a wide range of clients.
- They are suitable for web-based applications, mobile apps, and other distributed systems that require interoperability.

### Data File

The data is provided here: [data.csv](data.csv)

Column Descriptions:

|  #  | Column            | Description                       |
| :-: | :---------------- | :-------------------------------- |
|  0  | Date_reported     | date in `yyyy-mm-dd` format       |
|  1  | Country_code      | A unique 2 digit country code     |
|  2  | Country           | Name of the country               |
|  3  | WHO_region        | World Health Organization region  |
|  4  | New_cases         | Number of new cases on this date  |
|  5  | Cumulative_cases  | Cumulative cases up to this date  |
|  6  | New_deaths        | Number of new deaths on this date |
|  7  | Cumulative_deaths | Cumulative deaths up to this date |

## Fast Api Examples

Examples 1 and 2 show you two different ways to pass in parameters to a route.

### Example 1

Here is one way to create a GET function that uses two parameters:

```python
from fastapi import FastAPI

app = FastAPI()

# Fictitious list of data
my_list = ['apple', 'banana', 'cherry', 'date', 'elderberry']

@app.get("/get_values1/")
def get_values1(index1: int, index2: int):
    try:
        value1 = my_list[index1]
        value2 = my_list[index2]
        return [value1, value2]
    except IndexError:
        return {"error": "Invalid index provided."}
```

To invoke this via the address bar in your browser:

- `http://localhost:5000/get_values/?index1=0&index2=2`

providing the values for `index1` and `index2` as query parameters. The response will be a JSON object containing the list of values if the indices are valid, or an error message if the indices are out of range.

### Example 2

This is the same, but different way provide two params

```python
from fastapi import FastAPI

app = FastAPI()

# Fictitious list of data
my_list = ['apple', 'banana', 'cherry', 'date', 'elderberry']

@app.get("/get_values2/{index1}/{index2}")
def get_values2(index1: int, index2: int):
    try:
        value1 = my_list[index1]
        value2 = my_list[index2]
        return [value1, value2]
    except IndexError:
        return {"error": "Invalid index provided."}
```

To invoke this via the address bar in your browser:

- `http://localhost:5000/get_values/3/4/`

providing the values for `index1` and `index2` as part of the url. The response will be the same as Example 1.

Remember that any params you define in the `route` like `@app.get("/get_values2/{index1}/{index2}")` are required no matter what. Fast api calls those `path` parameters. The other style where you place them after a `q` (question mark) are called `query` parameters. Those you can make default (optional).

For more examples on how to pass in parameters (along with optional params) go here: https://fastapi.tiangolo.com/tutorial/query-params/

## Requirements

1. Use FastAPI to build the API (code mostly provided)
2. The API should have the endpoints listed in the sections below
3. Try to handle errors gracefully. For example, if a parameter that is passed in causes an error, simply return `{'success':False}` or return the parameters passed in as well `{'success':False,'param1':value1,'param(n):value(n)}`. This helps for debugging.
4. Implement proper API documentation using FastAPI's built-in support for OpenAPI (Swagger UI). This means comment your functions using markdown syntax for readability. I'll provide an example below the routes.

### Generic Routes

- **Route:** `/`
  - Retrieves the documentation provided by swagger.
- **Route:** `/countries`
  - Retrieves a list of unique countries from the "db"
- **Route:** `/regions`
  - Retrieves a list of available WHO regions from the "db"

### Death Routes

You can use the same route and pass in specific parameters to tailor your result. The 5 routes below would only be one function that calculated the answer based on the params actually passed in.

- **Route:** `/deaths`
  - Retrieves total deaths for all countries
- **Route:** `/deaths?country=France`
  - Retrieves the total deaths for the given country.
- **Route:** `/deaths?region=AFRO`
  - Retrieves the total deaths for the given region.
- **Route:** `/deaths?country=France&year=2020`
  - Retrieves the total deaths for the given country in a specified year.
- **Route:** `/deaths?region=AFRO&year=2020`
  - Retrieves the total deaths for the given region in a specified year.

OR you can create different routes for each specific query type. There would be 5 seperate routes using the style below.

- **Route:** `/deaths`
  - Retrieves total deaths for all countries
- **Route:** `/deaths_by_country/{country}`
  - Retrieves the total deaths for the given country.
- **Route:** `/deaths_by_region/{region}`
  - Retrieves the total deaths for the given region.
- **Route:** `/deaths_by_country_year/{country}/{year}`
  - Retrieves the total deaths for the given country in a given year.
- **Route:** `/deaths_by_region_year/{region}/{year}`
  - Retrieves the total deaths for the given region in a given year.

I'm you can see the merits of both styles. I like the first style, although the logic and get a little ugly within the function.

### Case Routes

- Same as above!

### Aggregate Routes

- **Route:** `/max_deaths`
  - Find the country with the most deaths
- **Route:** `/max_deaths?min_date=2021-06-01&max_date=2021-12-31`
  - Find the country with the most deaths between a range of dates
- **Route:** `/min_deaths`
  - Find the country with the least deaths
- **Route:** `/min_deaths?min_date=2021-06-01&max_date=2021-12-31`
  - Find the country with the least deaths between a range of dates
- **Route:** `/avg_deaths`

  - Find the average number of deaths between all countries

### Example Comment Block

```python
@app.get("/deaths/")
async def deaths(country:str = None,year:int = None):
    """
    This method will return a total death count or can be filtered by country and year.
    - **Params:**
      - country (str) : A country name
      - year (int) : A 4 digit year
    - **Returns:**
      - (int) : The total sum based on filters (if any)

    #### Example 1:

    [http://localhost:8080/deaths/](http://localhost:8080/deaths/)

    #### Response 1:

        {
            "total": 1000000,
            "params": {
                "country": null,
                "year": null
            }
            "success": true,
        }

    #### Example 2:

    [http://localhost:8080/deaths/?country=Brazil&year=2023](http://localhost:8080/deaths/?country=Brazil&year=2023)

    #### Response 2:

        {
            "total": 42,
            "params": {
                "country": "Brazil",
                "year": 2023
            }
            "success": true,
        }

    """

    pass
```

## Deliverables:

- Create a folder called `A08` to place all of your assignment files in.
- Include your Python code for the FastAPI application and any additional files.
- A README.md Document explaining the API endpoints and their usage.
  - If you comment your functions well, then you could almost cut and past to your readme.
- A brief report summarizing the implementation process, challenges faced, and any additional functionalities you may have added.
- Any instructions should be included in your readme (how to run your code)

> Note: Ensure proper code organization, documentation, and adherence to best practices in software development.
