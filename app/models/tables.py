from app import db

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoimplement=True)
    nome = db.Column(db.String)
	cpf = db.Column(db.Integer)
	email = db.Column(db.String)
	celular = db.Column(db.Integer)
	senhaUser = db.Column(db.String)
	senhaUserConf = db.Column(db.String)

    	def __init__(self, nome, cpf, email, celular, senhaUser, senhaUserConf):
		self.nome = nome
		self.cpf = cpf
		self.email = email
		self.celular = celular
		self.senhaUser = senhaUser
		self.senhaUserConf = senhaUserConf

	db.create_all()
    db.commit
