# Telegram bot + django message sender

## Setup

The first thing to do is to clone the repository:

```sh
$ https://github.com/AldiyarBolat/django-telegrambot-messagesender.git
$ cd sdjango-telegrambot-messagesender
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv2 --no-site-packages env
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv2`.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd telegram_bot
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/admin/`.

Also in a new tab run the bot:
```sh
(env)$ cd telegram_bot
(env)$ python manage.py bot
```

## Connect To Bot
First start telegram bot: `@messagesenderrrrbot`

Then send auto generated token to bot as a message, bot will try to connect 
your telegram account with given tokens user.
Hint: you cant find token value in django admin Profile section.

## API

### Register

To register user send POST request to `http://127.0.0.1:8000/api/register/` with body:
```json
{
	"username": "admin",
	"password": "asdfasdf",
        "first_name":"admin name"
}
```

### Login

To login user send POST request to `http://127.0.0.1:8000/api/login/` with body:
```json
{
	"username": "admin",
	"password": "qazwsxedc"
}
```
As a result you will get auth Token that you will use in following API calls

### Post Message

To post message send POST request to `http://127.0.0.1:8000/api/message/` with body:
```json
{
	"text": "message text"
}
``` 
and `Authorization = Token token_from_login` headers 

### Get List Of All Messages

To post message send Get request to `http://127.0.0.1:8000/api/message/` with headers:
`Authorization = Token token_from_login` 
