from app import db
from sqlalchemy import text



def run():
    db.engine.execute(insert_patient)
    db.engine.execute(insert_therapist)
    db.engine.execute(insert_appointment)

def clear():
	db.engine.execute(delete_appointment)
	db.engine.execute(delete_therapist)
	db.engine.execute(delete_patient)