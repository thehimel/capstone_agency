import os
from auth import AUTH0_DOMAIN, API_AUDIENCE

RUN_IN_THE_CLOUD = True


def get_database_path(database_name):
    username = 'admin'
    password = 'abc123'
    host_port = 'localhost:5432'
    database_path = 'postgres://{}:{}@{}/{}'.format(
        username,
        password,
        host_port,
        database_name)
    return database_path


if RUN_IN_THE_CLOUD is True:
    try:
        database_path = os.environ['DATABASE_URL']
        test_database_path = os.environ['HEROKU_POSTGRESQL_BRONZE_URL']

    except Exception:
        print('Please define environmental variables with | . setup.sh |')
        exit()

    host = 'https://thecastingagency.herokuapp.com'

else:
    database_name = 'agency'
    database_path = get_database_path(database_name)

    test_database_name = 'agency_test'
    test_database_path = get_database_path(test_database_name)

    host = 'http://127.0.0.1:5000'


CLIENT_ID = 'ORnLAD0MOrczpz4mav0EhzrMhLZDDQ8n'
CALLBACK_URI = '{}/login-results'.format(host)

request_uri = "https://{}/authorize?audience={}&response_type=token&client_id={}&redirect_uri={}".format(
    AUTH0_DOMAIN,
    API_AUDIENCE,
    CLIENT_ID,
    CALLBACK_URI
)
