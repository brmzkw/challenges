# Subject

Hey, I have this PostgreSQL database.

I want to remove all users with the query `DELETE FROM users` but it is super slow. I don't understand why, I have only
25000 entries, it should not take more than a few seconds.

Can you tell me why it takes so long, and how to improve?


# Setup

Run the container:

```
$> docker-compose up
```

Connect to the database:

```
$> docker-compose exec psql -U postgres
```
