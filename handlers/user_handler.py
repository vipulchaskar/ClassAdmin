from common_error_codes import *
import mongo_config

def get_user_by_username(username):
	user = mongo_config.mongo.db.users.find_one({'username': username})
	if not user:
		raise NotFoundError("The user does not exist.")
	return user