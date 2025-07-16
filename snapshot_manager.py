import data_loader as dl
import datetime
import json

user_followers = dl.find_followers('followers_1.json')
user_following = dl.find_following('following.json')

#print(user_followers)

#print(user_following)

current_date = str(datetime.date.today())
#print(current_date)
data_dictionary = {
    'date': current_date,
    'followers': user_followers,
    'following': user_following 
}
file_path = f"snapshot/snapshot_{current_date}.json"

with open(file_path,'w') as output_file:
    json.dump(data_dictionary, output_file,indent=4)

