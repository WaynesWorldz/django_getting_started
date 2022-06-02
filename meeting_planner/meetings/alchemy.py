#!/usr/bin/env python
import time

from sqlalchemy import create_engine

engine = create_engine(
    'snowflake://{user}:{password}@{account_identifier}/'.format(
        user='WRICHARD',
        password='Wandffm58!',
        account_identifier='redclassic.east-us-2.azure',
    )
)
try:
    connection = engine.connect()
    print("Submitting query...")
    results = connection.execute('select current_version()').fetchone()
    print(results[0])
    wait = input("Press Enter to continue.")
    print("something")
finally:
    connection.close()
    engine.dispose()
