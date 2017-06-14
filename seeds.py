from app import db
from sqlalchemy import text

insert_airport = text(
    """INSERT INTO airport VALUES
    ('FRA', 'EDDF', 'Frankfurt Airport', 'Frankfurt', 'Germany', 'Large'),
    ('PEK', 'ZBAA', 'Beijing Capital International Airport', 'Beijing', 'China', 'Large'),
    ('AMS', 'EHAM', 'Amsterdam Airport Schiphol', 'Amsterdam', 'Netherlands', 'Medium'),
    ('HND', 'RJTT', 'Haneda Airport', 'Tokyo', 'Japan', 'Large'),
    ('IAH', 'KIAH', 'George Bush Intercontinental Airport', 'Houston', 'United States',        'Medium'),
    ('LGW', 'EGLL', 'London Heathrow Airport', 'London', 'United Kingdom', 'Large'),
    ('KUL', 'WMKK', 'Kuala Lumpur International Airport', 'Kuala Lumpur', 'Malaysia',    'Medium')
    """
)

delete_airport = text(
    'DELETE FROM airport'
)

insert_check_in = text(
    """INSERT INTO check_in VALUES
    ('FRA', '2015-04-26', '0.62', '0.36', '28.44', '4.07', '323.58'),
    ('FRA', '2016-05-10', '0.55', '0.18', '12.96', '3.48', '257.06'),
    ('FRA', '2017-04-02', '0.67', '0.61', '38.74', '4.66', '295.02'),
    ('PEK', '2015-01-02', '0.67', '0.6', '41.82', '4.62', '324.69'),
    ('PEK', '2016-06-03', '0.68', '0.66', '42.05', '4.75', '302.75'),
    ('PEK', '2017-05-03', '0.68', '0.67', '46.78', '4.77', '334.12'),
    ('AMS', '2015-01-09', '0.51', '0.11', '8.6', '3.14', '254.45'),
    ('AMS', '2016-03-28', '0.49', '0.08', '6.75', '3.0', '242.23'),
    ('AMS', '2017-05-07', '0.52', '0.13', '10.07', '3.27', '254.4'),
    ('HND', '2015-03-24', '0.65', '0.48', '31.66', '4.37', '289.15'),
    ('HND', '2016-05-03', '0.51', '0.12', '7.84', '3.2', '215.9'),
    ('HND', '2017-05-01', '0.62', '0.35', '24.7', '4.04', '289.07'),
    ('IAH', '2015-05-29', '0.59', '0.25', '18.1', '3.77', '267.68'),
    ('IAH', '2016-04-21', '0.65', '0.47', '35.85', '4.34', '333.3'),
    ('IAH', '2017-05-16', '0.61', '0.32', '24.72', '3.95', '310.09'),
    ('LGW', '2015-02-07', '0.84', '3.33', '178.81', '8.4', '451.06'),
    ('LGW', '2016-06-07', '0.6', '0.29', '19.11', '3.88', '255.11'),
    ('LGW', '2017-04-25', '0.5', '0.1', '6.76', '3.08', '216.31'),
    ('KUL', '2015-01-18', '0.88', '5.31', '335.47', '10.61', '670.41'),
    ('KUL', '2016-04-08', '0.6', '0.3', '20.36', '3.9', '267.16'),
    ('KUL', '2017-03-20', '0.62', '0.36', '25.42', '4.07', '289.78')
    """
)

delete_check_in = text(
    'DELETE FROM check_in'
)

insert_emigration = text(
    """INSERT INTO emigration VALUES
    ('FRA', '2015-04-26', '0.62', '0.36', '28.44', '4.07', '323.58'),
    ('FRA', '2016-05-10', '0.55', '0.18', '12.96', '3.48', '257.06'),
    ('FRA', '2017-04-02', '0.67', '0.61', '38.74', '4.66', '295.02')
    """
)

delete_emigration = text(
    'DELETE FROM emigration'
)

insert_security = text(
    """INSERT INTO security_checkpoint VALUES
    ('FRA', '2015-04-26', '0.62', '0.36', '28.44', '4.07', '323.58'),
    ('FRA', '2016-05-10', '0.55', '0.18', '12.96', '3.48', '257.06'),
    ('FRA', '2017-04-02', '0.67', '0.61', '38.74', '4.66', '295.02')
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