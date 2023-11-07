from flask import Blueprint, jsonify, redirect, render_template, request, url_for
from flask_jwt_extended import create_access_token, jwt_required,get_jwt_identity

auth = Blueprint("auth",__name__)

@auth.route("/",methods=['GET'])
def get_index_view():
    return  render_template('login.html')
@auth.route("/auth",methods=['POST','GET'])
def get_token():
    if request.method=='POST':
        username=request.form['username']
        password=request.form["password"]
        print(f"Username: {username} \n Password: {password} ")
        access_token = create_access_token(identity=username)
        json_response ={
            "token":access_token,
            "user_id":username
        }
        return jsonify(json_response)
    return redirect(url_for("auth.get_index_view"))
@auth.route('/admin',methods =['GET'])
@jwt_required(optional=True)
def view_admin():
    datos={"username":"pepe123"}
    return render_template("admin.html",datos=datos)

