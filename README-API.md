## API Reference

### Getting Started
- Cloud URL: https://thecastingagency.herokuapp.com/
- Localhost URL: http://127.0.0.1:5000/


### Error Handling
Errors are returned as JSON objects in the following format:

```
{
  "error": 401,
  "message": "unauthorized",
  "success": false
}
```

The API will return the following error types when requests fail:
- 400: Bad Request
- 401: Unauthorized
- 404: Resource Not Found
- 405: Method Not Allowed
- 422: Not Processable
- 500: Internal Server Error (This is very rare)

### Initialize environmental variables to use with curl
```bash
export URL='https://thecastingagency.herokuapp.com'
or
export URL='http://127.0.0.1:5000'
```

From the landing page, click on the `Login` button and generate the access token.
```bash
export TOKEN='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c'
```
>This is a dummy token. Actual token generated after login may differ from this.
>No space before and after equal (=) symble.
> Use `echo $URL` or echo `echo $TOKEN` to read.

### Endpoints

#### POST /movies
---
- General:
  - Create a movie
  - Required permission `post:movies`
  - Takes
    - Authentication bearer token
    - title (String)
    - release_date (Date)
  - Returns
    - Success value (bool)
    - A list containing one movie in dictionary of title and release_date

- Request
```bash
curl $URL/movies -X POST -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" -d '{"title":"Action Movie", "release_date":"2020-12-30"}'
```

- Response
```
{"movie":[{"release_date":"2020-12-30","title":"Action Movie"}],"success":true}
```

#### GET /movies
---
- General:
  - Returns the list of all movies
  - Required permission `get:movies`
  - Takes
    - Authentication bearer token
  - Returns
    - Success value (bool)
    - A list of movies (list)

- Request
```bash
curl -H "Authorization: Bearer $TOKEN" $URL/movies
```

- Response
```
{
    "movies": [
        {
            "id": 1,
            "release_date": "2022-01-01",
            "title": "Action Movie"
        },
        {
            "id": 2,
            "release_date": "2022-01-01",
            "title": "Action Movie"
        },
        {
            "id": 3,
            "release_date": "2020-10-20",
            "title": "Action Movie"
        },
        {
            "id": 4,
            "release_date": "2024-02-20",
            "title": "Thriller Movie"
        }
    ],
    "success": true
}
```

#### PATCH /movies/movie_id
---
- General:
  - Update a movie
  - Required permission `patch:movies`
  - Takes
    - Authentication bearer token
    - movie_id as part of the URL
    - title (String) to update
    - release_date (Date) to update
  - Returns
    - Success value (bool)
    - A list containing one movie in dictionary of title and release_date

- Request
```bash
curl $URL/movies/1 -X PATCH -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" -d '{"title":"Action Movie", "release_date":"2022-01-01"}'
```

- Response
```
{"movie":[{"release_date":"2022-01-01","title":"Action Movie"}],"success":true}
```

#### DELETE /movies/movie_id
---
- General:
  - Delete a movie
  - Required permission `delete:movies`
  - Takes
    - Authentication bearer token
    - movie_id (int) as part of the URL
  - Returns
    - Success value (bool)
    - Deleted movie_id (int)

- Request
```bash
curl $URL/movies/4 -X DELETE -H "Authorization: Bearer $TOKEN"
```

- Response
```
{"id":4,"success":true}
```

#### POST /actors
---
- General:
  - Create an actor
  - Required permission `post:actors`
  - Takes
    - Authentication bearer token
    - name (String)
    - age (String)
    - gender (String)
  - Returns
    - Success value (bool)
    - A list containing one actor in dictionary of name, age, and gender

- Request
```bash
curl $URL/actors -X POST -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" -d '{"name":"Beautiful Actress", "age": 25, "gender": "female"}'
```

- Response
```
{"actor":[{"age":25,"gender":"Female","name":"Beautiful Actress"}],"success":true}
```

#### GET /actors
---
- General:
  - Returns the list of all actors
  - Required permission `get:actors`
  - Takes
    - Authentication bearer token
  - Returns
    - Success value (bool)
    - A list of actors (list)

- Request
```bash
curl -H "Authorization: Bearer $TOKEN" $URL/actors
```

- Response
```
{
    "actors": [
        {
            "age": 25,
            "gender": "Female",
            "id": 1,
            "name": "Beautiful Actress"
        },
        {
            "age": 32,
            "gender": "Male",
            "id": 2,
            "name": "Handsome Actor"
        },
        {
            "age": 20,
            "gender": "Female",
            "id": 3,
            "name": "Sweet Actress"
        },
        {
            "age": 32,
            "gender": "Female",
            "id": 4,
            "name": "Talented Actress"
        }
    ],
    "success": true
}
```

#### PATCH /actors/actor_id
---
- General:
  - Update an actor
  - Required permission `patch:actors`
  - Takes
    - Authentication bearer token
    - name (String)
    - age (String)
    - gender (String)
  - Returns
    - Success value (bool)
    - A list containing one actor in dictionary of name, age, and gender

- Request
```bash
curl $URL/actors/1 -X PATCH -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" -d '{"name":"Beautiful Actress", "age": 26, "gender": "female"}'
```

- Response
```
{"actor":[{"age":26,"gender":"female","name":"Beautiful Actress"}],"success":true}
```

#### DELETE /actors/actor_id
---
- General:
  - Delete an actor
  - Required permission `delete:actors`
  - Takes
    - Authentication bearer token
    - actor_id (int) as part of the URL
  - Returns
    - Success value (bool)
    - Deleted actor_id (int)

- Request
```bash
curl $URL/actors/4 -X DELETE -H "Authorization: Bearer $TOKEN"
```

- Response
```
{"id":4,"success":true}
```
