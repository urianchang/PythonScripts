from sqlalchemy import (
    Column,
    create_engine,
    MetaData,
    Table,
    Text
)
from sqlalchemy.schema import CreateSchema
import copy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

def make_db_url(user, password, db, host='localhost', port=5432):
    """
    Returns a postgres database url
    """
    url = "postgresql://{}".format(user)
    if password:
        url += ":{}".format(password)
    url += "@{}:{}".format(host, port)
    if db:
        url += "/{}".format(db)

    return url

def quick_mapper(table):
    Base = declarative_base()
    class GenericMapper(Base):
        __table__ = table
    return GenericMapper

def make_session(url_string):
    engine = create_engine(url_string, client_encoding="utf8")
    Session = sessionmaker(bind=engine)
    return Session(), engine

def transfer_table(from_db, from_schema, to_db, to_schema, table_name):
    # (str, str, str, str, str) -> None
    """
    Transfer a table from one schema in a database to a schema
    in another database.
    """
    source, sengine = make_session(from_db)
    smeta = MetaData(bind=sengine)
    destination, dengine = make_session(to_db)

    # Get the desired table and make a copy of it
    table_source = Table(table_name, smeta, autoload=True, schema=from_schema)
    table_copy = copy.deepcopy(table_source)
    table_copy.schema = to_schema

    # Create table in destination schema
    table_copy.metadata.create_all(dengine)

    # Copy data from source table to destination
    NewRecord = quick_mapper(table_copy)
    columns = table_copy.columns.keys()
    for record in source.query(table_source).all():
        data = dict(
            [(str(column), getattr(record, column)) for column in columns]
        )
        destination.merge(NewRecord(**data))

    # Execute the changes
    destination.commit()

db1_url = make_db_url('urian', None, 'testdb1')
db2_url = make_db_url('urian', None, 'testdb2')
table_name = "department"
transfer_table(db1_url, 'schema1', db2_url, 'public', table_name)

""" This works:
testdb1 = make_db_url('urian', None, 'testdb1')
source, engine = make_session(testdb1)
smeta = MetaData(bind=engine)

testdb2 = make_db_url('urian', None, 'testdb2')
destination, dengine = make_session(testdb2)

table_source = Table('department', smeta, autoload=True, schema='schema1')
table_copy = copy.deepcopy(table_source)
table_copy.schema = "public"
table_copy.metadata.create_all(dengine)

NewRecord = quick_mapper(table_copy)
columns = table_copy.columns.keys()
for record in source.query(table_source).all():
    data = dict(
        [(str(column), getattr(record, column)) for column in columns]
    )
    destination.merge(NewRecord(**data))
destination.commit()
"""

# Get list of all databases
# eng = connect('urian', None, None)
# query = "SELECT datname FROM pg_database WHERE datistemplate = false;"
# db_rows = eng.execute(query).fetchall()
# db_list_clean = []
# for db_row in db_rows:
#     db_list_clean.append(str(db_row[0]))
#
# eng.dispose()

# Check if schema exists and create it if not
# q = "select schema_name from information_schema.schemata"
# all_schema_rows = engine.execute(q).fetchall()
# if not ('schema2',) in all_schema_rows:
#     engine.execute(CreateSchema('schema2'))
