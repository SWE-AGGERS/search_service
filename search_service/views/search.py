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
    data = {"story": {
                    "text": search_text
            }
     }
    call_stories_search = requests.post(SEARC_STORIES_URL,json=data, headers=headers)
    stories = call_stories_search.json()
    data = {"users":users,"stories":stories}
    return jsonify(data)

