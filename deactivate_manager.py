
def format_data(usernames : str):

    list_of_names = usernames.split()
    return list_of_names

def remove_deactive(account_list : list, deactivated_list : str):
    
    deactivated_list = format_data(deactivated_list)
    filtered_list = list()

    for i in range(len(account_list)):
        if account_list[i] not in deactivated_list:
            filtered_list.append(account_list[i])

    store_deactive_account_names(deactivated_list)

    return filtered_list

def store_deactive_account_names(account_list : list):

    with open("account.txt", "w") as file_writer:
        for i in range(len(account_list)):
            file_writer.write(account_list[i] + "\n")


def extract_names_from_file(filename):
    account_names = ""
    with open(filename, "r") as file_reader:

        for each_name in file_reader:       
            each_name = each_name.rstrip("\n")
            account_names = account_names + each_name + " " 

    print((account_names))


usernames="aanikamahi pritha0.1"
follower_names = ["nusrat_liaa", "aanikamahi", "pritha0.1", "studytasmania"]

print(remove_deactive(follower_names, usernames))
#store_deactive_account_names(remove_deactive(follower_names, usernames))
#extract_names_from_file("account.txt")