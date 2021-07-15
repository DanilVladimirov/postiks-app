# postiks-app

## Run

```sh
>> python migrate
>> python manage.py createsuperuser
>> python manage.py runserver 8000
>> celery celery -A postiks worker -l info
>> celery -A postiks worker --beat -l info -S django
```

Heroku: https://postiks.herokuapp.com/

Postman collection: https://www.getpostman.com/collections/5466fd583152d6defc4e
