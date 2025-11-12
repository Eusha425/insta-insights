import io
import streamlit 

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

    with open("account.txt", "a") as file_writer:
        for i in range(len(account_list)):
            file_writer.write(account_list[i] + "\n")


def extract_names_from_file(file_or_path):
    
    account_names = ""
    # to check the type of parameter passed
    if isinstance(file_or_path, streamlit.runtime.uploaded_file_manager.UploadedFile):
        file_read = io.StringIO(file_or_path.getvalue().decode("utf-8"))
        for each_name in file_read:
            each_name = each_name.rstrip("\n")
            account_names = account_names + each_name + " " 

    else: 
        with open(file_or_path, "r") as file_reader:

            for each_name in file_reader:       
                each_name = each_name.rstrip("\n")
                account_names = account_names + each_name + " " 

    return account_names


def main():
    print("This is the deactive account manager module")

if __name__ == "__main__":
    main()