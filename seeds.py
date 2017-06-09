from app import db
from sqlalchemy import text

insert_admin = text(
    """INSERT INTO user VALUES
    ('admin','admin')
    """
)

insert_airport = text(
    """INSERT INTO airport VALUES
    ('AER', 'URSS', 'Sochi International Airport', 'Sochi', 'Russia', 'Medium'),
    ('KRR', 'URKK', 'Krasnodar International Airport', 'Krasnodar', 'Russia', 'Small'),
    ('SIN', 'WSSS', 'Singapore Changi Airport', 'Singapore', 'Singapore', 'Large'),
    ('ABC','ABCD','Randomly Named Airport','Randcity','Randcountry','Randsize')
    """
)

delete_airport = text(
    'DELETE FROM airport'
)

insert_check_in = text(
    """INSERT INTO check_in VALUES
    ('AER', '2015-02-12', '0.85', '5.62', '3.22', '3.42', '4.13'),
    ('KRR', '2015-05-12', '0.85', '5.62', '3.22', '3.42', '4.13'),
    ('SIN', '2015-07-12', '0.85', '5.62', '3.22', '3.42', '4.13')
    """
)

delete_check_in = text(
    'DELETE FROM check_in'
)

insert_emigration = text(
    """INSERT INTO emigration VALUES
    ('AER', '2015-02-12', '0.85', '5.62', '3.22', '3.42', '4.13'),
    ('KRR', '2015-05-12', '0.85', '5.62', '3.22', '3.42', '4.13'),
    ('SIN', '2015-07-12', '0.85', '5.62', '3.22', '3.42', '4.13')
    """
)

delete_emigration = text(
    'DELETE FROM emigration'
)

insert_security = text(
    """INSERT INTO security_checkpoint VALUES
    ('AER', '2015-02-12', '0.85', '5.62', '3.22', '3.42', '4.13'),
    ('KRR', '2015-05-12', '0.85', '5.62', '3.22', '3.42', '4.13'),
    ('SIN', '2015-07-12', '0.85', '5.62', '3.22', '3.42', '4.13')
    """
)

delete_security = text(
    'DELETE FROM security_checkpoint'
)

def run():
    db.engine.execute(insert_airport)
    db.engine.execute(insert_check_in)
    db.engine.execute(insert_emigration)
    db.engine.execute(insert_security)

def clear():
    db.engine.execute(delete_security)
    db.engine.execute(delete_emigration)
    db.engine.execute(delete_check_in)
    db.engine.execute(delete_airport)