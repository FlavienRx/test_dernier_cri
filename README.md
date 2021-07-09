# Instalation

## Requirements

To install project, you need to have [Pipenv](https://pipenv.pypa.io/en/latest/install/) and [Yarn](https://classic.yarnpkg.com/en/docs/install/#debian-stable) installed on your computer.

## Backend

To install backend, go to root directory and install python dependencies:
```
pipenv install
```

Pipenv will create a virtual env.

Next, go to backend directory and run the backend server:

```
cd pokemon && python manage.py migrate && python manage.py runserver --settings=pokemon.dev
```

## Frontend

In `frontend` directory, install frontend dependencies:
```
yarn install
```

Run the server to compiles and hot-reloads:
```
yarn serve
```

To compiles and minifies for production
```
yarn build
```

Find the application here [http://localhost:8000](http://localhost:8000) 

# API

To get the pokemon list, make a GET request at `/api/pokemon`

The response have to be like this:

```json
[
    {
        "poke_api_id": 1,
        "name": "bulbasaur",
        "small_image_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/1.png"
    },
    {
        "poke_api_id": 2,
        "name": "ivysaur",
        "small_image_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/2.png"
    },
    ...
    {
        "poke_api_id": 20,
        "name": "raticate",
        "small_image_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/20.png"
    }
]
```

To get the pokemon detail, make a GET request at `/api/pokemon/id` where `id` is an integer in range to 1 to X.

The response have to be like this:

```json
{
    "poke_api_id": 1,
    "name": "bulbasaur",
    "height": 7,
    "weight": 69,
    "types": [
        {
            "poke_api_id": 4,
            "name": "poison"
        },
        {
            "poke_api_id": 12,
            "name": "grass"
        }
    ],
    "moves": [
        {
            "poke_api_id": 13,
            "name": "razor-wind"
        },
        {
            "poke_api_id": 14,
            "name": "swords-dance"
        },
        ...
        {
            "poke_api_id": 590,
            "name": "confide"
        }
    ],
    "large_image_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/1.png"
}
```

# TODO

- [x] Wrap poke API
- [x] Fill database
- [x] Make an API endpoint
- [x] Make tests
- [x] Consume API endpoint by front
- [ ] Deploy in roduction
- [ ] Manage dev url to remove that -> `http://localhost:8000/http://127.0.0.1:8080/`
- [ ] Move API call from components to a JS file
- [ ] Add more pokemon informations
- [ ] Add database integrity tests
