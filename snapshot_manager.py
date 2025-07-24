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

def get_mutual_analysis(current_mutual, snapshot_data):
    snapshot_mutual = snapshot_data[2]

    mutual_gain = list()

    for i in range(len(current_mutual)):
        if current_mutual[i] not in snapshot_mutual:
            mutual_gain.append(current_mutual[i])
    
    mutual_loss = list()
    for i in range(len(snapshot_mutual)):
        if snapshot_mutual[i] not in current_mutual:
            mutual_loss.append(snapshot_mutual[i])

    result = tuple()
    result = result + (mutual_gain,)
    result = result + (mutual_loss,)

    return result

def get_followers_gain(current_followers, snapshot_followers):
    try:
        gain_followers = list()
        print(snapshot_followers)
        for i in range(len(current_followers)):
            if current_followers[i] not in snapshot_followers:
                gain_followers.append(current_followers[i])
        
        return gain_followers
    except:
        return None

def get_followers_lost(current_follower, snapshot_follower):
    try:
        lost_followers = list()

        for i in range(len(snapshot_follower)):
            if snapshot_follower[i] not in current_follower:
                lost_followers.append(snapshot_follower[i])
        return lost_followers
    except:
        return None

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