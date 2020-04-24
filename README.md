# FSDN Capstone Project
## Casting Agency
The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies.

I have learned a lot of new technologies throughout the whole course at Udacity and this is the time to implement all my knowledge by compiling them in the capstone project.

All backend code follows [PEP8 style guidelines](https://www.python.org/dev/peps/pep-0008/ "PEP8 style guidelines").

## Features
* Models:
	* Movies with attributes title and release date
	* Actors with attributes name, age and gender
* Endpoints:
	* GET /actors and /movies
	* DELETE /actors/ and /movies/
	* POST /actors and /movies and
	* PATCH /actors/ and /movies/
*  Roles:
	* Casting Assistant
		* Can view actors and movies
	* Casting Director
		* All permissions a Casting Assistant has and…
		* Add or delete an actor from the database
		* Modify actors or movies
	* Executive Producer
		* All permissions a Casting Director has and…
		* Add or delete a movie from the database

## Getting Started
#### Installing Dependencies
##### Python 3.7
Follow instructions to install the latest version of python for your platform in the [Python docs](https://docs.python.org/3/)

#### PIP Dependencies

`pip install -r requirements.txt`

This will install all of the required packages we selected within the requirements.txt file.

#### Key Dependencies
* [Flask](http://flask.pocoo.org/ "Flask") is a lightweight backend microservices framework. Flask is required to handle requests and responses.
* [SQLAlchemy](https://www.sqlalchemy.org/ "SQLAlchemy") is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py.
* [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/ "Flask-CORS") is the extension we'll use to handle cross-origin requests from our frontend server.

#### Database Setup
With Postgres, create a database named **agency**

`createdb agency`

> Make sure to include the database credentials in **env_file.py**

#### Running the server
From the project directory to run the server, execute:

`. setup.sh`

`export FLASK_DEBUG=true`

`python app.py`

The app will now run on debug mode and auto restart if any change is made.
The application runs on http://127.0.0.1:5000/ by default.

#### Authentication
This project uses Auth0 for authentication.
Click on the login button and signup. Note down the access token from the URL for further use.

#### Tests
##### pytest
In order to run tests, navigate to the project folder and run the following commands:

`. setup.sh`

`pytest test_app.py`

> Include the tokens in the test_app.py before running the test. Make sure the tokens are healthy.
> By default the test uses cloud database to run the test which is a slower approach when running in local server. You can go to env_file.py and select RUN_IN_THE-CLOUD=False and enter the database credential to choose the local database which is a faster approach while running in local server. But if you are running the test from the heroku remotely, the default method is faster enough with no issue at all.
> It's very important to use different database for the application and test.

All tests are kept in that file and should be maintained as updates are made to app functionality.

##### [Postman](https://www.postman.com/)
* Open the postman application and import all the files from the **postman** directory inside the project folder.
	* **Environment to test the cloud server:** agency_env_cloud
	* **Environment to test the local server:** agency_env_localhost
* Click on Runner.
* Select collection and the appropriate environment.
* Run the test.

> Tokens are included in the environment. Generate new tokens if tokens are expired.

## API Reference
Refer to the README-API.md

## Deployment
We are using Heroku for deployment.
* Install heroku in your machine.
* Login to heroku
```bash
heroku login
```
* Create an app
```bash
heroku create appname
```
* Create database
```bash
heroku addons:create heroku-postgresql:hobby-dev --app appname
```
* Check configuration variables in Heroku
```bash
heroku config --app appname
```
> Note down the **DATABASE_URL** and include it in the setup.sh to use this database while running the app locally.

* Initialize git in the project directory
```bash
git init
git remote add heroku https://git.heroku.com/appname.git
```

* Push it to heroku
```bash
git add .
git commit -am "make it better"
git push heroku master
```

## Author
* [Himel Das](https://www.linkedin.com/in/himeldas/ "Himel Das")

## Acknowledgements
* The incredible team at Udacity.
* Special thanks to my teachers in this course who have taught me beautiful things.
	* [Amy Hua](https://www.linkedin.com/in/huaamy/ "Amy Hua")
	* [Caryn McCarthy](https://www.linkedin.com/in/carynmccarthy/ "Caryn McCarthy")
	* [Gabriel Ruttner](https://www.linkedin.com/in/gruttner/ "Gabriel Ruttner")
	* [Kennedy Behrman](https://www.linkedin.com/in/kennedybehrman/ "Kennedy Behrman")
