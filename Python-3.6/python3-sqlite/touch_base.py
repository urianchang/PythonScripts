import os
import sqlite3
import textwrap
import time

from datetime import datetime


_SQL_CONNECTION_SETUP = textwrap.dedent("""\
    -- Prevent connections from rolling journal back
    PRAGMA journal_mode = PERSIST;

    -- If app crashes, data is safe, but db may be corrupted if OS crashes
    -- or computer loses power before data is written. Commits can be faster.
    PRAGMA synchronous = OFF;
""")

_SQL_CREATE_SCHEMA = textwrap.dedent("""\
    -- Create markers table
    CREATE TABLE IF NOT EXISTS markers (
      component TEXT NOT NULL,
      asset TEXT NOT NULL,
      stream_type TEXT NOT NULL,
      category TEXT NOT NULL,
      timestamp INTEGER NOT NULL,
      level TEXT NOT NULL,
      message TEXT NOT NULL,
      PRIMARY KEY (component, asset, stream_type, category) ON CONFLICT IGNORE
    );

    -- Create migrations table
    CREATE TABLE IF NOT EXISTS migrations (
      migration_id TEXT NOT NULL,
      PRIMARY KEY (migration_id)
    );
""")

_SQL_INSERT_MARKER = textwrap.dedent("""\
    INSERT INTO
    markers (timestamp, component, asset, stream_type, category, level, message)
    VALUES (:timestamp, :component, :asset, :stream_type, :category, :level, :message)
""")

conn = None

try:
    try:
        conn = sqlite3.connect('./your_base.db')
        res, = list(conn.execute("PRAGMA integrity_check(1);"))[0]
    except sqlite3.DatabaseError:
        res = "error"

    if res != "ok":
        print("DB file is corrupt, recreating it.")
        conn.close()
        conn = None
        os.remove(path)
        conn = sqlite3.connect(path)

    conn.executescript(_SQL_CONNECTION_SETUP)
    conn.executescript(_SQL_CREATE_SCHEMA)
finally:
    if conn is not None:
        conn.close()

_conn = sqlite3.connect('./your_base.db')
_conn.executescript(_SQL_CONNECTION_SETUP)

params = {
    'timestamp': int(time.time()),
    'component': "some_component",
    'asset': "some_asset",
    'stream_type': "some_stream_type",
    'category': "some_category",
    'level': "warning",
    'message': "This is a warning message",
}

cur = _conn.execute(_SQL_INSERT_MARKER, params)

query = "SELECT * FROM markers;"

results = []
for row in cur.execute(query):
    col_names = ('component', 'asset', 'stream_type', 'category', 'timestamp', 'level', 'message')
    result = dict(zip(col_names, row))
    result['datetime'] = datetime.utcfromtimestamp(result['timestamp'])
    results.append(result)
print(results)

components = ['asdf', 'asdf1', 'asdf2', 'some_component']
# query = "DELETE FROM markers WHERE component in (%s);" % ','.join('?' * len(components))
# query = "DELETE FROM markers WHERE component in ({!s});".format(', '.join('?' * len(components)))
c_string = ','.join('?' * len(components))
query = "DELETE FROM markers WHERE component in ({!s})".format(c_string)
# cur.execute(query)
print(query)
cur.execute(query, components)

query = "SELECT * FROM markers;"

results = []
for row in cur.execute(query):
    col_names = ('component', 'asset', 'stream_type', 'category', 'timestamp', 'level', 'message')
    result = dict(zip(col_names, row))
    result['datetime'] = datetime.utcfromtimestamp(result['timestamp'])
    results.append(result)
print(results)

cur.close()

print("END")
