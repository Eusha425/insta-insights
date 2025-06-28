import data_loader as dl
import analyser as anl
import visualiser as vl
import argparse
import csv

def print_summarise(data):
    num_of_mutual = data[0]
    num_of_non_followers = data[1]
    num_of_unrequited = data[2]
    print(f"Mutual: {num_of_mutual}\nNot following you back: {num_of_non_followers}\nYou are not following back: {num_of_unrequited}")

def summarise_data(non_followers, unrequited_followers, mutual):
    num_of_non_followers = len(non_followers)
    num_of_unrequited = len(unrequited_followers)
    num_of_mutual = len(mutual)
    return num_of_mutual, num_of_non_followers, num_of_unrequited # returning a tuple containing the numbers 

def write_summary_to_text(data):
    #print(data)
    label = ['Mutual', 'Not following you back', 'You are not following back']
    with open("data.txt", 'w') as file_writer:
        for i in range(len(data)):
            file_writer.write(f"{label[i]}: {data[i]}\n")
    

def write_summary_to_csv(data):
    #print(data)
    header = ['Mutual', 'Not following you back', 'You are not following back']
    with open("data.csv", "w", newline='', encoding='utf-8') as file_writer:
        writer = csv.writer(file_writer)
        writer.writerow(header)
        writer.writerow(data)


def write_full_data_to_text(non_followers, unrequited_followers, mutual):
    with open('data.txt', 'w') as file_writer:
        
        file_writer.write("Not Following You Back:\n")
        for i in range(len(non_followers)):
            file_writer.write(f"{non_followers[i]}\n")
        file_writer.write('\n') # extra line for better formatting 

        file_writer.write("You Are Not Following Back:\n")
        for i in range(len(unrequited_followers)):
            file_writer.write(f"{unrequited_followers[i]}\n")
        file_writer.write('\n') # extra line for better formatting 

        file_writer.write("Mutual Followers:\n")
        for i in range(len(mutual)):
            file_writer.write(f"{mutual[i]}\n")

def write_full_data_to_csv(non_followers, unrequited_followers, mutual):
    # define the header
    header = ["Not Following You Back", "You Are Not Following Back", "Mutual Followers"]
    max_len = max(len(non_followers), len(unrequited_followers), len(mutual))
    rows = []

    for i in range(max_len):

        # checking the index, If non_followers has an element at this index, use it
        if i < len(non_followers):
            nf = non_followers[i]
        else:
            nf = ""
        if i < len(unrequited_followers):
            ur = unrequited_followers[i]
        else:
            ur = ""
        if i < len(mutual):
            mt = mutual[i]
        else:
            mt = ""
        row = [nf, ur, mt]
        rows.append(row)



    #zipped_rows = zip(header, non_followers, unrequited_followers, mutual)
    with open("data.csv", "w", newline='', encoding='utf-8') as file_writer:
        writer = csv.writer(file_writer)
        writer.writerow(header)
        writer.writerows(rows)




parser = argparse.ArgumentParser(description="📈 Analyze Instagram followers and following data.",epilog="✨ Example: python cli.py --followers followers.json --following following.json")
parser.add_argument('--followers', type=str, metavar="", default="followers_1.json", help="Path to the followers JSON file") # add the necessary parametres for adding the argument, metavar added to enhance the cli output
parser.add_argument('--following', type=str, metavar="", default="following.json", help="Path to the following JSON file")
parser.add_argument('--visualise', action='store_true', help="Create visualisation")
parser.add_argument('--summarise', action="store_true", help="Summarise the data")
parser.add_argument('--export', type=str, metavar="", help="Export the data")
args = parser.parse_args()

#dl.find_followers(args.followers)
#dl.find_following(args.following)

non_followers, unrequited_followers, mutual = anl.following_follower_analysis(dl.find_following(args.following), dl.find_followers(args.followers))

#need to fix this 
if args.summarise:
    #print(f"Mutual: {len(mutual)}\nNot Following You Back: {len(non_followers)}\nYou Are Not Following Back: {len(unrequited_followers)}")
    print_summarise(summarise_data(non_followers, unrequited_followers, mutual))
else:
    #temporary code need to change here
    print("🔴 Not Following You Back:")
    print(non_followers)

    print("\n🟢 You Are Not Following Back:")
    print(unrequited_followers)

    print("\n🔁 Mutual Followers:")
    print(mutual)


if args.visualise:
    vl.visualisation(mutual, non_followers, unrequited_followers)

# defensive check to see if export called or not
if args.export:
    if args.export.lower() == 'csv':
        if args.summarise:
            write_summary_to_csv(summarise_data(non_followers, unrequited_followers, mutual))
        else:
            write_full_data_to_csv(non_followers, unrequited_followers, mutual)
    elif args.export.lower() == 'txt':
        if args.summarise:
            write_summary_to_text(summarise_data(non_followers, unrequited_followers, mutual))
        else:
            write_full_data_to_text(non_followers, unrequited_followers, mutual)
    else:
        print(f"Unsupported export format: {args.export}")


""" 
if args.export == 'csv' or args.export == 'CSV' or args.export == 'txt' or args.export == 'TXT':

    if args.export == 'csv' or args.export == 'CSV':
        print('csv file')
        #write_summary_to_csv(summarise_data(non_followers, unrequited_followers, mutual))
        write_full_data_to_csv(non_followers, unrequited_followers, mutual)

    elif args.export == 'txt' or args.export == 'TXT':
        print('txt file')
        #write_summary_to_text(summarise_data(non_followers, unrequited_followers, mutual))
        write_full_data_to_text(non_followers, unrequited_followers, mutual)
else:
    print(f"Unsupported export format: {args.export}") """