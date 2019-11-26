from flask import Blueprint, render_template
from flask import request
from search_service.constants import GET_USERS_URL
search = Blueprint('search', __name__)


@search.route('/search', methods=["GET"])
def index():
    search_text = request.args.get("search_text")
    if search_text:

        users = find_user(text=search_text)

        stories = find_story(text=search_text)

        if users and stories:
            return render_template("search.html", users=users, stories=stories)
        elif users:
            return render_template("search.html", users=users)
        elif stories:
            return render_template("search.html", stories=stories)
        else:
            return render_template("search.html")
    else:
        return render_template("search.html")


def find_story(text):
    result = Story.query.filter(func.lower(Story.text).contains(func.lower(text)))
    return result if result.count() > 0 else None