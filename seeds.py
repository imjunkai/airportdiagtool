from app import db
from sqlalchemy import text

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

def run():
    db.engine.execute(insert_airport)
    db.engine.execute(insert_check_in)
    # db.engine.execute(insert_appointment)

def clear():
	db.engine.execute(delete_check_in)
	db.engine.execute(delete_airport)
	# db.engine.execute(delete_patient)