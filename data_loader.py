import json

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

def main():
    print("This is the data loader module")

if __name__ == "__main__":
    main()