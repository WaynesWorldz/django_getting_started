#!/usr/bin/env python
import time

from sqlalchemy import create_engine

engine = create_engine(
    'snowflake://{user}:{password}@{account_identifier}/'.format(
        user='snowflake',
        password='i9.et!YK9&J6@fA',
        account_identifier='redclassic.east-us-2',
    )
)
try:
    connection = engine.connect()
    print("Submitting query...")
    results = connection.execute('select current_version()').fetchone()
    print(results[0])
finally:
    connection.close()
    engine.dispose()
