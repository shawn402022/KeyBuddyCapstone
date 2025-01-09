from flask import Blueprint, jsonify
from app.models import db
from app.models.user_models import User

bp = Blueprint("user", __name__, url_prefix="/user")

@bp.route("/")
def users():
    # USE THE DB TO QUERY ALL USERS
    all_users = db.session.query(User)
    #Create a tring to add <p> tabs for each user
    result_list= []

    #iterate thrrough the users and add their names to the string
    for user in all_users:
        new_user = user.to_dict()
        result_list.append(new_user)

    return jsonify(result_list)
