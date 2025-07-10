import json

def find_followers(file_or_path):
    # error checking to see correct file format
    try:
        if isinstance(file_or_path, str): # to check the type of parametre passed, expect string when using CLI expect file object when running GUI
            with open(file_or_path) as follower_file:
                follower_data = json.load(follower_file)
        else:
            follower_data = json.load(file_or_path)

        follower_name = []

        #print(len(follower_data))
        for each_row in follower_data:
            each_name = each_row['string_list_data'][0]['value']
            #print(each_name)
            follower_name.append(each_name)

        return follower_name
    except:
        print("Invalid JSON file format")



def find_following(file_or_path):
    # error checking to see correct file format
    try:
        # to check the type of parametre passed, expect string when using CLI expect file object when running GUI
        if isinstance(file_or_path, str):

            with open(file_or_path) as following_file:
                following_data = json.load(following_file)
        else:
            following_data = json.load(file_or_path)

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
    except:
        print("Invalid JSON file format")

def main():
    print("This is the data loader module")

if __name__ == "__main__":
    main()