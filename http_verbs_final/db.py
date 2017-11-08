from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://tpqzvjjbuxkflr:bbe309ef06b4d6d1e9448f2d6a3aa822442322f7c817b0a4713aebe4cf70ebce@ec2-107-20-226-93.compute-1.amazonaws.com:5432/dedft0csks1uog'
db = SQLAlchemy(app)

# Create our database model
class User(db.Model):
    __tablename__ = "curso_table"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True)

    @property
    def serialize(self):
       return {
           'id': self.id,
           'name': self.name,
       }

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Nombre %r>' % self.name

@app.route('/prereg', methods=['POST', "GET"])
def prereg():
    name = None
    if request.method == 'POST':
        name = request.form['name']
        # Check that name does not already exist (not a great query, but works)
        if not db.session.query(User).filter(User.name == name).count():
            reg = User(name)
            db.session.add(reg)
            db.session.commit()
            res = {'task': 'profit!'}
            return jsonify(res)
    elif request.method == "GET":
    	users = User.query.all() #Get all users
    	return jsonify([i.serialize for i in users])
    #return "Fail!"

if __name__ == '__main__':
    app.run(debug=True)
