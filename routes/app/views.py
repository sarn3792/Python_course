from app import app2

@app2.route("/")
@app2.route("/index")
def index():
	return "Hello world"