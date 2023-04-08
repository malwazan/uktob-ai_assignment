# Assignment 1 & 2 - Flask API


### Project Desctrption
The project is an assignment for uktob.ai job. It is web api project build in Python's Flask framework. Project is following MVC pattern. Let's go throught some of the important files:
- `/config.py`: This file contains the application config for multiple environments.
- `/server.py`: This file is responsible for running the flask server.
- `/app/__init__.py`: This file is the main brain of whole flask application. 
  - It initialize Flask, and other dependencies.
  - It initialize Blueprints
  - __init__.py also contains `@before_request` and `@after_request` lifecycle methods which are loading the database `db.json` in to flask request context `g`.
- `/app/routes`: This folder contains all the flask blueprint initializations
- `/app/controller`: It is responsible for ubpacking request and returning response to the client
- `/app/services`: Service files contains the business logic
- `/app/utilities`: Utilities files contains common functions and configurations
- `/app/utilities/errors.py`: This module is responsible for handling all the user exceptions and unhandled exceptions.


### Running the application
- Create virtual environment
  `python -m venv .venv`
- Activate the virtual environment
  [Windows] `.venv\scripts\activate` | [Linux] `source .venv/bin/activate`
- Install `requirements.txt`
  `pip install -r requirements.txt`
- Run the application with following command
  `python server.py`


## Base Endpoint

- `http://localhost:5000`


## Routes

- **[GET] `/`:** Status/Health_check route
  

- **[POST] `/home/sum`:** API for sum of list of numbers
  - Headers
    ```
    - Content-Type: application/json
    ```
  - JSON Body:
    ```
    {
      "numbers: [
        1,2,3
      ]
    }
    ```

- **[POST] `/home/concat`:** API to concat 2 strings
  - Headers
    ```
    - Content-Type: application/json
    ```
  - JSON Body:
    ```
    {
      "string1: "VALUE",
      "string2": "VALUE"
    }
    ```


- **[POST] `/auth/register`:** API to register new user
  - Headers
    ```
    - Content-Type: application/json
    ```
  - JSON Body:
    ```
    {
      "username: "",
      "password": ""
    }
    ```


- **[POST] `/auth/login`:** API to login registered users
  - Headers
    ```
    - Content-Type: application/json
    ```
  - JSON Body:
    ```
    {
      "username: "",
      "password": ""
    }
    ```