#!/usr/bin/env python
import os
from migrate.versioning.shell import main

db_url = 'postgresql://{}:{}@localhost/{}'.format(
    'openworld',
    '5up3r_s3cur3_p455w0rd',
    'openworld-0.0.1'
)

if __name__ == '__main__':
    main(repository='migrations', url=db_url, debug='False')
