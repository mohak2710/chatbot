# Chatbot Flask service
A Flask Application that serves as middleware for chatbot interaction with Watson API

## Instructions
As always ensure you create a virtual environment for this application and install
the necessary libraries from the `requirements.txt` file.

```
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

Then create the sqlite3 database file and create the tables based on our `app/models.py`.

```
$ touch /tmp/mydatabase.db
$ python
>>> from app import db
>>> db.create_all()
>>> quit()
```

Then start the development server

```
$ python run.py
```

Browse to http://0.0.0.0:5000
