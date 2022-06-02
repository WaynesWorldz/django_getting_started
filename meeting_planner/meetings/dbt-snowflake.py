#!/usr/bin/env python
import snowflake.connector

# Gets the version
ctx = snowflake.connector.connect(
    user='WRICHARD',
    password='Wandffm58!',
    account='redclassic.east-us-2.azure'
    )
cs = ctx.cursor()
try:
    cs.execute("SELECT * FROM RC_PROD.MDMLOADS.PNETNEWDRIVERS")
    all_rows = cs.fetchall()
    print(all_rows[0])
    wait = input("Press Enter to continue.")
    print("something")
finally:
    cs.close()
ctx.close()
