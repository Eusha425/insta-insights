import matplotlib.pyplot as plt

def visualisation(mutual, non_followers, unrequited_followers):
    
    count_mutal = len(mutual)
    count_non_follower = len(non_followers)
    count_unrequited = len(unrequited_followers)
    label_list = ["Mutuals", "Not Followed Back", "Not Following"]

    plt.pie([count_mutal, count_non_follower, count_unrequited], labels=label_list)
    plt.legend()
    plt.show()

def main():
    print("This is the visualiser module")

if __name__ == "__main__":
    main()