import json
usernames = []
def list_followers():
    followers_file = open("followers_1.json")
    lst_file = json.load(followers_file)
    for follower in lst_file:
      username_lst = follower.get("string_list_data")
      username = username_lst[0].get('value')
      usernames.append(username)
    followers_file.close()
    return usernames
# def lst_following():
#    following_file = open('/Users/awhite/Documents/python_project_ig/')
      
  #  username_list= lst_file[0].get('string_list_data')
  #  username = username_list[0].get('value')
  #  print(username)

print(list_followers())
   