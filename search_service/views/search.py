from flask import Blueprint
from search_service.constants import SEARCH_USER_URL, SEARC_STORIES_URL
from flask import jsonify
import requests

search = Blueprint('search', __name__)


@search.route("/search/<search_text>", methods=["GET"])
def index(search_text):
    user_search_url = "{}/{}".format(SEARCH_USER_URL, search_text)
    headers = {'Content-type': 'application/json; charset=UTF-8'}
    call_user_search = requests.get(user_search_url, headers=headers)

    users = call_user_search.json()

    stroies_search_url =

    stories = find_story(text=search_text)
    if users and stories:
        return render_template("search.html", users=users, stories=stories)
    elif users:
        return render_template("search.html", users=users)
    elif stories:
        return render_template("search.html", stories=stories)
    else:
        return render_template("search.html")

    return jsonify(data)

