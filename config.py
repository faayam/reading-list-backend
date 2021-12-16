import os

# user = os.environ['POSTGRES_USER']
# password = os.environ['POSTGRES_PASSWORD']
host = os.environ['POSTGRES_HOST']
# database = os.environ['POSTGRES_DB']
# port = os.environ['POSTGRES_PORT']

user = 'postgres'
password = 'postgres'
# host = '192.168.1.121'
database = 'books'
port = 5432


DATABASE_CONNECTION_URI = f'postgresql://{user}:{password}@{host}:{port}/{database}'