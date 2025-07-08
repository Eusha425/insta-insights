import csv

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


def main():
    print("This is the exporter module")


if __name__ == "__main__":
    main()