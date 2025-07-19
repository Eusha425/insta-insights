import datetime
import json
from pathlib import Path
import os

def save_snapshot(followers, following):
    user_followers = followers #dl.find_followers('followers_1.json')
    user_following = following #dl.find_following('following.json')

    #print(user_followers)

    #print(user_following)

    current_date = str(datetime.date.today())
    #print(current_date)
    data_dictionary = {
        'date': current_date,
        'followers': user_followers,
        'following': user_following 
    }

    # create a path object for the file directory
    file_path = Path(f"snapshot/snapshot_{current_date}.json")
    # Ensure the parent directory exists
    file_path.parent.mkdir(parents=True, exist_ok=True)

    with open(file_path,'w') as output_file:
        json.dump(data_dictionary, output_file,indent=4)

    return True


def list_snapshots():
    try:
        path = 'snapshot/'
        files_in_the_path = os.listdir(path)
        return files_in_the_path
    except:
        return None

def load_follower_from_snapshot(snapshot_name):
    try:
        snapshot_name = 'snapshot/' + snapshot_name
        with open(snapshot_name, 'r') as file_reader:
            data = json.load(file_reader)
        followers = data['followers']
        #print(followers)
        return followers
    except:
        return None

def load_following_from_snapshot(snapshot_name):
    try:
        snapshot_name = 'snapshot/' + snapshot_name
        with open(snapshot_name, 'r') as file_reader:
            data = json.load(file_reader)
        following = data['following']
        #print(following)
        return following
    except:
        return None

def compare_data(current_tuple, snapshot_tuple):

    current_non_followers = current_tuple[0]
    snapshot_non_followers = snapshot_tuple[0]

    difference_in_non_followers = list(set(current_non_followers) - set(snapshot_non_followers))

    result = tuple()
    result = result + (difference_in_non_followers,)
    
    current_unrequited = current_tuple[1]
    snapshot_unrequited = snapshot_tuple[1]

    difference_in_unrequited = list(set(current_unrequited) - set(snapshot_unrequited))
    result = result + (difference_in_unrequited,)

    current_mutual = current_tuple[2]
    snapshot_mutual = snapshot_tuple[2]

    difference_in_mutual = list(set(current_mutual) - set(snapshot_mutual))
    result = result + (difference_in_mutual,)

    return result


def compare_followers(current_followers, snapshot_followers):

    difference_in_followers = list(set(current_followers) - set(snapshot_followers))

    if len(difference_in_followers) == 0:
        return None
    else:
        return difference_in_followers

def main():
    print("This is the snapshot manager module")
    #list_snapshots()
    #load_follower_from_snapshot('snapshot_2025-07-18.json')
    #load_following_from_snapshot('snapshot_2025-07-18.json')



if __name__ == "__main__":
    main()