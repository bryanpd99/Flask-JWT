from flask import Flask

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "ASDJFGHAJGFJFDAGKJFGHKJG"
@app.route("/",methods=['GET'])
def get_index_view():
    return "hola que tal"

app.run()
