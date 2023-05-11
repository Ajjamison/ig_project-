import json
follower_usernames = []
following_usernames = []
def list_followers():
    followers_file = open("followers_1.json")
    lst_file = json.load(followers_file)
    for follower in lst_file:
      username_lst = follower.get("string_list_data")
      username = username_lst[0].get('value')
      follower_usernames.append(username)
    followers_file.close()
    return follower_usernames
def lst_following():
  following_file = open('following.json')
  lst_file = json.load(following_file)
  lst_file_two = lst_file.get('relationships_following')
  for followe in lst_file_two:
    username_lst = followe.get("string_list_data")
    username = username_lst[0].get('value')
    following_usernames.append(username)
  following_file.close()
  return following_usernames
def unfollow(following, followers):
   not_following_me = set(following) - set(followers)
   not_following_me_two = set(followers) - set(following)
   return list(not_following_me) + list(not_following_me_two)


   
   

print(len(list_followers()) - len(lst_following()))
# print(len(lst_following()))
# print(len((unfollow(lst_following() , list_followers()))))
   