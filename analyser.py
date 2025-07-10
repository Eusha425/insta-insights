def following_follower_analysis(user_following, user_followers):
    # error checking if no parametre could be passed
    try:
        # following who not follow back (i.e non-followers)
        non_followers = []

        for each_following in user_following:
            if each_following not in user_followers:
                non_followers.append(each_following)

        # followers not followed back (i.e Unrequited Followers)
        unrequited_followers = []

        for each_follower in user_followers:
            if each_follower not in user_following:
                unrequited_followers.append(each_follower)

        # mutuals
        mutual = []

        for each_following in user_following:
            if each_following in user_followers:
                mutual.append(each_following)

        return non_followers, unrequited_followers, mutual
    except:
        print("Files could not be properly analysed")
    
def main():
    print("This is the analyser module")

if __name__ == "__main__":
    main()