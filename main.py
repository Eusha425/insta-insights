import json
import matplotlib.pyplot as plt

def find_followers():
    with open("followers_1.json") as follower_file:
        follower_data = json.load(follower_file)

    follower_name = []

    #print(len(follower_data))
    for each_row in follower_data:
        each_name = each_row['string_list_data'][0]['value']
        #print(each_name)
        follower_name.append(each_name)

    return follower_name


def find_following():
    with open("following.json") as following_file:
        following_data = json.load(following_file)

    following_data = following_data['relationships_following']
    #print((following_data))
    c = 0
    following_name = list()
    for i in range( len(following_data)):
        #print(following_data[i]['string_list_data'][0]['value'])
        following_name.append(following_data[i]['string_list_data'][0]['value'])

    #print(c)
    #print(following_name)
    return following_name

def visualisation(mutual, non_followers, unrequited_followers):
    count_mutal = len(mutual)
    count_non_follower = len(non_followers)
    count_unrequited = len(unrequited_followers)
    """ print(count_mutal)
    print(count_non_follower)
    print(count_unrequited)
    """
    label_list = ["Mutuals", "Not Followed Back", "Not Following"]

    plt.pie([count_mutal, count_non_follower, count_unrequited], labels=label_list)
    plt.legend()
    plt.show()

user_followers = find_followers()
user_following = find_following()

# following who not follow back (i.e non-followers)
non_followers = []

for each_following in user_following:
    if each_following not in user_followers:
        non_followers.append(each_following)

# followers not followed back (i.e Unrequited Followers)
unrequited_followers = []

for each_follower in user_followers:
    if each_follower not in user_following:
        unrequited_followers.append(each_follower)

# mutuals
mutual = []

for each_following in user_following:
    if each_following in user_followers:
        mutual.append(each_following)

print("🔴 Not Following You Back:")
print(non_followers)

print("\n🟢 You Are Not Following Back:")
print(unrequited_followers)

print("\n🔁 Mutual Followers:")
print(mutual)

visualisation(mutual, non_followers, unrequited_followers)

