from sqlalchemy import Table, Column, String, Date, MetaData

meta = MetaData()

users =  Table(
    'Users', meta,
    Column('id', String(36), primary_key=True), # UUID length = 36 chars
    Column('first_name', String(30)),
    Column('last_name', String(30)),
    Column('email', String(60)),
    Column('password', String(60)),
    Column('created_at', Date)
)

def upgrade(migrate_engine):
    meta.bind = migrate_engine
    users.create()


def downgrade(migrate_engine):
    meta.bind = migrate_engine
    users.drop()
