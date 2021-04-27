from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
        html = "<H1> Mне надоели твои розовые сиськи и твой микрофон. Даааа. Пезда! Встала и пошла отсюда ! (С)"
        return html

if __name__=="__main__":
        app.run(host="0.0.0.0", port=80)
