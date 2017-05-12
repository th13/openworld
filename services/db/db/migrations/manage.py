#!/usr/bin/env python
import os
from migrate.versioning.shell import main

db_url = 'postgresql://{}:{}}@localhost/{}'.format(
    os.environ['POSTGRES_USER'],
    os.environ['POSTGRES_PASSWORD'],
    os.environ['POSTGRES_DB']
)

if __name__ == '__main__':
    main(repository='migrations', url=db_url, debug='False')
