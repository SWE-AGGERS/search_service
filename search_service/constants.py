
USERS_SERVICE_IP = '0.0.0.0'
USERS_SERVICE_PORT = '5002'

STORIES_SERVICE_IP = '0.0.0.0'
STORIES_SERVICE_PORT = "5001"

SEARCH_USER_URL = "http://{}:{}/search".format(USERS_SERVICE_IP, USERS_SERVICE_PORT) # add search key to end of the string by using format

SEARC_STORIES_URL = "http://{}:{}/search_story".format(STORIES_SERVICE_IP,STORIES_SERVICE_PORT) #add search key to end of the string by using format