﻿# Project Raven Backend

 [project_raven_frontend](https://github.com/mohammadlebzo/project_raven_frontend)

## Tech-stack
- Python - FastAPI
- MySQL Database
- Docker

## How to run
- Run the following command:
    - generate environment `python3 -m venv venv`
    - activate environment:
        - Windows: `venv\Scripts\activate`
        - Linux: `source venv/bin/activate`
    - install requirements: `pip install -r requirements.txt`
    - generate `SECRET_KEY` by using `openssl rand -hex 32`

        **Note**: if you are using windows and don't have `wsl` available on your machine use the provided linux based docker image to generate it by following these steps:
        
        - run `docker compose up -d` to build a container of the provided image
        - run `docker exec -it project_r bash` to enter the docker container
        - run `openssl rand -hex 32`
        - copy the provided key for later
        - run `exit` to leave the docker container

    - copy the content of `.env.sample` to `.env` (Make One)
    - copy the key from the second step and use it for `SECRET_KEY` environment var
    - Run the project (OS based):
        - Windows -> `./run.bat`
        - Linux/macOS -> `./run.sh`

**Notes**: 
- If you don't prefer using the **run command files** just use the commands within.
- In case you want to test JWT expiration change `ACCESS_TOKEN_EXPIRE_MINUTES` .env variable to desired amount.
- Was not sure if the JWT token should be registered as no registration was mentioned (the login was the only thing mentioned) so I made a mocked user for use + testing:

        {
            "username": "Raven",
            "password": "raven621",
        }

## Database used
I decided to use **MySQL** database for simplicity sake as the scope of the project is quit small as there is no need for advanced database features like materialized views or stored procedures.

At first I wanted to use **MongoDB** but was not sure if it's an allowed option. The reason behind going for **MongoDB** at first is that there is no need for relations in such project scope as this project, so it would be the simplest option + lately I have been working a lot with **Mongos** so it just felt right.

## Endpoints
- **Authentication**:
    - ***[POST]*** `/api/v1/token`
        - curl ex:
            
                curl -X 'POST' \
                'http://localhost:8000/api/v1/token/' \
                -H 'accept: application/json' \
                -H 'Content-Type: application/x-www-form-urlencoded' \
                -d 'grant_type=password&username=Raven&password=raven621&scope=&client_id=string&client_secret=string'

        - response 200 ex:

                {
                    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJSYXZlbiIsImV4cCI6MTc0MjU2MjE3N30.vosDB99oSDxZxAKoCIg712nwltYO52uxtoYkliHBabI",
                    "token_type": "bearer"
                }

        - response 401 ex (incase of wrong username or password):

                {
                    "detail": "Incorrect username or password"
                }

- **Products Listing (Auth Needed)**:
    - ***[GET]*** `/api/v1/item`

        - curl ex:
            
                curl -X 'GET' \
                'http://localhost:8000/api/v1/item/?page_number=3&page_size=2' \
                -H 'accept: application/json' \
                -H 'Authorization: Bearer <token>'

        - response 200 ex:

                [
                    
                    "items": [
                        {
                        "id": 5,
                        "title": "Ring of Invisibility",
                        "description": "Grants temporary invisibility",
                        "price": 75,
                        "location": "JO"
                        },
                        {
                            "id": 6,
                            "title": "Helmet of Courage",
                            "description": "Boosts defense and confidence in battle",
                            "price": 95,
                            "location": "SA"
                        }
                    ],
                     "full_total": 100
                ]

        - curl with location (JO). ex:

                curl -X 'GET' \
                'http://localhost:8000/api/v1/item/?page_number=0&page_size=2&location=jo' \
                -H 'accept: application/json' \
                -H 'Authorization: Bearer <token>'

        - response 200 with location (JO). ex:

               {
                    "items": [
                        {
                            "id": 1,
                            "title": "Sword of Valor",
                            "description": "A legendary sword with magical powers",
                            "price": 150,
                            "location": "JO"
                        },
                        {
                            "id": 3,
                            "title": "Potion of Healing",
                            "description": "Restores health completely over 5 seconds",
                            "price": 20,
                            "location": "JO"
                        }
                    ],
                    "full_total": 50
                } 

- **Product Details (Auth Needed)**:
   - ***[GET]*** `/api/v1/item/{id}`

       - curl ex:
            
                curl -X 'GET' \
                'http://localhost:8000/api/v1/item/70/' \
                -H 'accept: application/json' \
                -H 'Authorization: Bearer <token>'


        - response 200 ex:

                {
                    "id": 70,
                    "title": "Cape of Shadows",
                    "description": "Allows the wearer to blend into the darkness",
                    "price": 110,
                    "location": "SA"
                }

- **Purchase Flow (Auth Needed)**:
    - ***[POST]*** `/api/v1/order/{purchase_id}`

        - curl ex:
            
                curl -X 'POST' \
                'http://localhost:8000/api/v1/order/70' \
                -H 'accept: application/json' \
                -H 'Authorization: Bearer <token>' \
                -d ''

        - response ex:

                {
                    "id": 70,
                    "title": "Cape of Shadows",
                    "description": "Allows the wearer to blend into the darkness",
                    "price": 110,
                    "location": "SA"
                }

- **Response 403 (for all auth protected end-points)**
    - Not Authenticated. ex:

            {
                "detail": "Not authenticated"
            }

     - Expired. ex:

            {
                "detail": "Invalid token or expired token."
            }
