from app import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
	username = db.Column(db.String(16), primary_key=True)
	password = db.Column(db.String(16), nullable=False)

	def __init__(self,**kwargs):
		self.username = kwargs['username']
		self.password = kwargs['password']

	def verify_password(self, password):
		return self.password==password

	def get_id(self):
		return self.username

	def __repr__(self):
		return 'User {}'.format(self.username)

class Airport(db.Model):
	iata_code = db.Column(db.String(3), primary_key=True)
	icao_code = db.Column(db.String(4), nullable=False)
	name = db.Column(db.String(45), nullable=False)
	city = db.Column(db.String(45), nullable=False)
	country = db.Column(db.String(45), nullable=False)
	size = db.Column(db.String(10), nullable=False)

	def __init__(self,**kwargs):
		self.iata_code = kwargs['iata_code']
		self.icao_code = kwargs['icao_code']
		self.name = kwargs['name']
		self.city = kwargs['city']
		self.country = kwargs['country']
		self.size = kwargs['size']

	def __repr__(self):
		return self.iata_code

class Check_in(db.Model):
	airport_id = db.Column(db.String(3), db.ForeignKey('airport.iata_code'), primary_key=True)
	diag_time = db.Column(db.Date, primary_key=True)
	uti_rate = db.Column(db.Float, nullable=False)
	queue_avgpeople = db.Column(db.Float, nullable=False)
	queue_waitingtime = db.Column(db.Float, nullable=False)
	sys_avgpeople = db.Column(db.Float, nullable=False)
	sys_waitingtime = db.Column(db.Float, nullable=False)

	def __init__(self,**kwargs):
		self.airport_id = kwargs['airport_id']
		self.diag_time = kwargs['diag_time']
		self.uti_rate = kwargs['uti_rate']
		self.queue_avgpeople = kwargs['queue_avgpeople']
		self.queue_waitingtime = kwargs['queue_waitingtime']
		self.sys_avgpeople = kwargs['sys_avgpeople']
		self.sys_waitingtime = kwargs['sys_waitingtime']

	def __repr__(self):
		return '%s, %s' % (self.airport_id, self.diag_time)

	@property
	def proc_info(self):
		return {
		# 'airport_id': self.airport_id,
		# 'diag_time': self.diag_time,
		'uti_rate': self.uti_rate,
		'queue_avgpeople': self.queue_avgpeople,
		'queue_waitingtime': self.queue_waitingtime,
		'sys_avgpeople': self.sys_avgpeople,
		'sys_waitingtime': self.sys_waitingtime,
		}

class Emigration(db.Model):
	airport_id = db.Column(db.String(3), db.ForeignKey('airport.iata_code'), primary_key=True)
	diag_time = db.Column(db.Date, primary_key=True)
	uti_rate = db.Column(db.Float, nullable=False)
	queue_avgpeople = db.Column(db.Float, nullable=False)
	queue_waitingtime = db.Column(db.Float, nullable=False)
	sys_avgpeople = db.Column(db.Float, nullable=False)
	sys_waitingtime = db.Column(db.Float, nullable=False)

	def __init__(self,**kwargs):
		self.airport_id = kwargs['airport_id']
		self.diag_time = kwargs['diag_time']
		self.uti_rate = kwargs['uti_rate']
		self.queue_avgpeople = kwargs['queue_avgpeople']
		self.queue_waitingtime = kwargs['queue_waitingtime']
		self.sys_avgpeople = kwargs['sys_avgpeople']
		self.sys_waitingtime = kwargs['sys_waitingtime']

	def __repr__(self):
		return '%s, %s' % (self.airport_id, self.diag_time)

	@property
	def proc_info(self):
		return {
		# 'airport_id': self.airport_id,
		# 'diag_time': self.diag_time,
		'uti_rate': self.uti_rate,
		'queue_avgpeople': self.queue_avgpeople,
		'queue_waitingtime': self.queue_waitingtime,
		'sys_avgpeople': self.sys_avgpeople,
		'sys_waitingtime': self.sys_waitingtime,
		}

class Security_checkpoint(db.Model):
	airport_id = db.Column(db.String(3), db.ForeignKey('airport.iata_code'), primary_key=True)
	diag_time = db.Column(db.Date, primary_key=True)
	uti_rate = db.Column(db.Float, nullable=False)
	queue_avgpeople = db.Column(db.Float, nullable=False)
	queue_waitingtime = db.Column(db.Float, nullable=False)
	sys_avgpeople = db.Column(db.Float, nullable=False)
	sys_waitingtime = db.Column(db.Float, nullable=False)

	def __init__(self,**kwargs):
		self.airport_id = kwargs['airport_id']
		self.diag_time = kwargs['diag_time']
		self.uti_rate = kwargs['uti_rate']
		self.queue_avgpeople = kwargs['queue_avgpeople']
		self.queue_waitingtime = kwargs['queue_waitingtime']
		self.sys_avgpeople = kwargs['sys_avgpeople']
		self.sys_waitingtime = kwargs['sys_waitingtime']

	def __repr__(self):
		return '%s, %s' % (self.airport_id, self.diag_time)

	@property
	def proc_info(self):
		return {
		# 'airport_id': self.airport_id,
		# 'diag_time': self.diag_time,
		'uti_rate': self.uti_rate,
		'queue_avgpeople': self.queue_avgpeople,
		'queue_waitingtime': self.queue_waitingtime,
		'sys_avgpeople': self.sys_avgpeople,
		'sys_waitingtime': self.sys_waitingtime,
		}