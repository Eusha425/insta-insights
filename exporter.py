import csv
import io

def streamlit_export_txt(non_followers, unrequited_followers, mutual):
    """
    Generates a formatted text summary of Instagram follower relationships.

    This function takes three lists representing follower categories and writes 
    them into a structured text format. The output includes:
    - People who do not follow you back
    - People you do not follow back
    - Mutual followers

    Args:
        non_followers (list of str): a list of non followers
        unrequited_followers (list of str): a list of people not followed back
        mutual (list of str): a list that contains name that are both following and followed 

    Returns:
        str: A single formatted string with the categorized follower information.
    """
    buffer = io.StringIO()
    buffer.write("Not Following You Back:\n")
    for i in range(len(non_followers)):
            buffer.write(f"{non_followers[i]}\n")
    buffer.write('\n') # extra line for better formatting 

    buffer.write("You Are Not Following Back:\n")
    for i in range(len(unrequited_followers)):
        buffer.write(f"{unrequited_followers[i]}\n")
    buffer.write('\n') # extra line for better formatting 

    buffer.write("Mutual Followers:\n")
    for i in range(len(mutual)):
        buffer.write(f"{mutual[i]}\n")

    output = buffer.getvalue()
    buffer.close()
    return output


def streamlit_export_csv(non_followers, unrequited_followers, mutual):
    """
    Generates a CSV-formatted string summarising Instagram follower relationships.

    This function takes three lists of usernames and aligns them under respective
    CSV columns:
    - "Not Following You Back"
    - "You Are Not Following Back"
    - "Mutual Followers"

    The output is structured so each row contains one entry from each list, 
    padding with empty strings where necessary to ensure all columns are aligned.

    Args:
        non_followers (str): a list of non followers
        unrequited_followers (str): a list of people not followed back
        mutual (str): a list that contains name that are both following and followed 

    Returns:
        str: A CSV-formatted string containing the follower relationship data.
    """

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

    buffer = io.StringIO()
    writer = csv.writer(buffer)
    writer.writerow(header)
    writer.writerows(rows)

    output = buffer.getvalue()
    buffer.close()
    return output


def summarise_data(non_followers, unrequited_followers, mutual):
    """
    Takes 3 lists getting length of those lists and returning those 3 lengths as a tuple

    Args:
        non_followers (list of str): a list of non followers
        unrequited_followers (list of str): a list of people not followed back
        mutual (list of str): a list that contains name that are both following and followed 

    Returns:
        tuple: 3 length of the 3 lists
    """
    num_of_non_followers = len(non_followers)
    num_of_unrequited = len(unrequited_followers)
    num_of_mutual = len(mutual)
    return num_of_mutual, num_of_non_followers, num_of_unrequited # returning a tuple containing the numbers 


def write_summary_to_text(data):
    """Writes follower summary statistics to a text file.

    This function takes a tuple containing counts of followers, unrequited and mutual
    relationships and writes them to a file named 'data.txt'. Each 
    line in the file corresponds to one of the following categories:
    
    - Mutual followers
    - Users not following you back
    - Users you are not following back

    The data is written in the format: "<Category>: <Value>".

    Args:
        data (tuple): A tuple of three elements corresponding to:
            [0] Mutual followers
            [1] Not following you back
            [2] You are not following back

    Raises:
        ValueError: If `data` does not contain exactly three elements.
    """
    label = ['Mutual', 'Not following you back', 'You are not following back']
    with open("data.txt", 'w') as file_writer:
        for i in range(len(data)):
            file_writer.write(f"{label[i]}: {data[i]}\n")


def write_summary_to_csv(data):
    """Writes follower summary statistics to a CSV file.

    This function takes a tuple of three elements representing follower relationship
    data and writes it to a CSV file named 'data.csv'. The CSV file will contain a 
    header row followed by a single row of corresponding values.

    The columns represent:
    - Mutual followers
    - Users not following you back
    - Users you are not following back

    Args:
        data (tuple): A tuple of three elements corresponding to:
            [0] Mutual followers
            [1] Not following you back
            [2] You are not following back

    Raises:
        ValueError: If `data` does not contain exactly three elements.
    """
    header = ['Mutual', 'Not following you back', 'You are not following back']
    with open("data.csv", "w", newline='', encoding='utf-8') as file_writer:
        writer = csv.writer(file_writer)
        writer.writerow(header)
        writer.writerow(data)


def write_full_data_to_text(non_followers, unrequited_followers, mutual):
    """Writes detailed follower relationship data to a text file.

    This function takes three lists of usernames representing follower 
    relationships and writes them into a text file named 'data.txt'. Each 
    section is labelled clearly for readability.

    The output file will include:
    - A list of users who are not following you back
    - A list of users you are not following back
    - A list of mutual followers

    Each category is followed by the relevant usernames, one per line, and 
    separated by a blank line for formatting.

    Args:
        non_followers (list of str): Usernames who are not following you back.
        unrequited_followers (list of str): Usernames you are not following back.
        mutual (list of str): Usernames who mutually follow you.

    """
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
    """Writes detailed follower relationship data to a CSV file.

    This function takes three lists of usernames representing different types of 
    follower relationships and writes them to a CSV file named 'data.csv'. Each row 
    in the CSV corresponds to one user from each list, aligned by index. If one list 
    is shorter than the others, empty strings are written in place to maintain row integrity.

    The columns in the CSV are:
    - Not Following You Back
    - You Are Not Following Back
    - Mutual Followers

    Args:
        non_followers (list of str): Usernames who are not following you back.
        unrequited_followers (list of str): Usernames you are not following back.
        mutual (list of str): Usernames who mutually follow you.

    """
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

    with open("data.csv", "w", newline='', encoding='utf-8') as file_writer:
        writer = csv.writer(file_writer)
        writer.writerow(header)
        writer.writerows(rows)


def main():
    print("This is the exporter module")


if __name__ == "__main__":
    main()