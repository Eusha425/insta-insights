import data_loader as dl
import analyser as anl
import visualiser as vl
import argparse
import exporter as ex

def print_summarise(data):
    num_of_mutual = data[0]
    num_of_non_followers = data[1]
    num_of_unrequited = data[2]
    print(f"Mutual: {num_of_mutual}\nNot following you back: {num_of_non_followers}\nYou are not following back: {num_of_unrequited}")


def section_title(icon, title):
    print(f"{icon}  {title} {icon}".center(50, "-"))


def print_list(data_list):

    for i in range(len(data_list)):
        print(f"{i+1}. {data_list[i]}")
    print() # for formatting


parser = argparse.ArgumentParser(description="📈 Analyze Instagram followers and following data.",epilog="✨ Example: python cli.py --followers followers.json --following following.json")
parser.add_argument('--followers', type=str, metavar="", default="followers_1.json", help="Path to the followers JSON file") # add the necessary parametres for adding the argument, metavar added to enhance the cli output
parser.add_argument('--following', type=str, metavar="", default="following.json", help="Path to the following JSON file")
parser.add_argument('--visualise', action='store_true', help="Create visualisation")
parser.add_argument('--summarise', action="store_true", help="Summarise the data")
parser.add_argument('--export', type=str, metavar="", help="Export the data")
parser.add_argument('--version', action='version', version='%(prog)s 1.0.0')
args = parser.parse_args()


try:
    non_followers, unrequited_followers, mutual = anl.following_follower_analysis(dl.find_following(args.following), dl.find_followers(args.followers))

    # functions to do based on arguments passed 
    if args.summarise:
        print_summarise(ex.summarise_data(non_followers, unrequited_followers, mutual))
    else:
        section_title("🔴", "Not Following You Back")
        print_list(non_followers)

        section_title("🟢","You Are Not Following Back")
        print_list(unrequited_followers)

        section_title("🔁","Mutual Followers")
        print_list(mutual)



    if args.visualise:
        vl.visualisation(mutual, non_followers, unrequited_followers)

    # defensive check to see if export called or not
    if args.export:
        if args.export.lower() == 'csv':
            if args.summarise:
                ex.write_summary_to_csv(ex.summarise_data(non_followers, unrequited_followers, mutual))
            else:
                ex.write_full_data_to_csv(non_followers, unrequited_followers, mutual)
        elif args.export.lower() == 'txt':
            if args.summarise:
                ex.write_summary_to_text(ex.summarise_data(non_followers, unrequited_followers, mutual))
            else:
                ex.write_full_data_to_text(non_followers, unrequited_followers, mutual)
        else:
            print(f"Unsupported export format: {args.export}")

except FileNotFoundError:
    print("The file does not exist, please check again")
except:
    print("Further operations could not be carried")
