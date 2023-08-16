from Packages.packages import *
from Route.route import rout

app = Flask(__name__)
app.register_blueprint(rout)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)