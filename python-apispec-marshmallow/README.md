# Subject

Hey Jack,

A while ago, I started to write an API to expose users. It works pretty well:

```
$> curl localhost:1111/users
[
  {
    "email": "bob@marley.com",
    "firstname": "Bob",
    "id": 1,
    "lastname": "Marley"
  },
  {
    "email": "jmjarre@dance.com",
    "firstname": "Jean-Michel",
    "id": 2,
    "lastname": "Jarre"
  },
  {
    "email": "me@fight.com",
    "firstname": "Conor",
    "id": 3,
    "lastname": "McGregor"
  }
]
```

I wanted to add two new endpoints, `/books` and `/movies`. For these endpoints, I want items to be under the top-level key `data`, such as:

```
$> curl localhost:1111/books
{
  "data": [
    {
      "id": 1,
      "name": "L'insoutenable l\u00e9g\u00e8ret\u00e9 de l'\u00eatre"
    },
    {
      "id": 2,
      "name": "La promesse de l'aube"
    }
  ]
}
$> curl localhost:1111/movies
{
  "data": [
    {
      "id": 1,
      "name": "Fight Club"
    },
    {
      "id": 2,
      "name": "American History X"
    }
  ]
}
```

The swagger documentation generated with `apispec` is available at `http://localhost:1112` and displays the `/users` endpoint correctly, but for `/books` and `/movies` there is no documentation available and a strange error is displayed:

```
Resolver error at paths./movies.get.responses.200.content.application/json.schema.$ref
Could not resolve reference: Could not resolve pointer: /components/schemas/WrappedMovieSchema does not exist in document
```

Can you help me to understand why the documentation does not appear, why this error is displayed, and how to fix it?


Thanks,

# Installation

Build and run the container:

```
$> docker-compose build
$> docker-compose up
```

Check you can access the API from the host:

```
$> curl http://localhost:1111
```

Swagger documentation is available at `http://localhost:1112`.
