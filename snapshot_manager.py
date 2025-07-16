import data_loader as dl
import datetime
import json
from pathlib import Path


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


def main():
    print("This is the snapshot manager module")


if __name__ == "__main__":
    main()