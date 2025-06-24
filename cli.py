import data_loader as dl
import analyser as anl
import visualiser as vl
import argparse

def show_summary(non_followers, unrequited_followers, mutual):
    num_of_non_followers = len(non_followers)
    num_of_unrequited = len(unrequited_followers)
    num_of_mutual = len(mutual)

    print(f"Mutual: {num_of_mutual}\nNot following you back: {num_of_non_followers}\nYou are not following back: {num_of_unrequited}")


parser = argparse.ArgumentParser(description="Testing it right now")
parser.add_argument('--followers', type=str, metavar="", default="followers_1.json", help="Path to the followers JSON file") # add the necessary parametres for adding the argument, metavar added to enhance the cli output
parser.add_argument('--following', type=str, metavar="", default="following.json", help="Path to the following JSON file")
parser.add_argument('--visualise', action='store_true', help="Create visualisation")
parser.add_argument('--summarise', action="store_true", help="Summarise the data")
parser.add_argument('--export', type=str, metavar="", default='.csv', help="Export the data")
args = parser.parse_args()

#dl.find_followers(args.followers)
#dl.find_following(args.following)

non_followers, unrequited_followers, mutual = anl.following_follower_analysis(dl.find_following(args.following), dl.find_followers(args.followers))

if args.summarise:
    #print(f"Mutual: {len(mutual)}\nNot Following You Back: {len(non_followers)}\nYou Are Not Following Back: {len(unrequited_followers)}")
    show_summary(non_followers, unrequited_followers, mutual)
else:

    print("🔴 Not Following You Back:")
    print(non_followers)

    print("\n🟢 You Are Not Following Back:")
    print(unrequited_followers)

    print("\n🔁 Mutual Followers:")
    print(mutual)


if args.visualise:
    vl.visualisation(mutual, non_followers, unrequited_followers)