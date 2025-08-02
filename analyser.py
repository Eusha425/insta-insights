def following_follower_analysis(user_following, user_followers):
    """Analyses Instagram-style follower relationships.

    Given two lists of usernames — users you follow and users who follow you —
    this function determines:

    - Users you follow who do not follow you back (non-followers)
    - Users who follow you but you do not follow back (unrequited followers)
    - Mutual followers (you follow each other)

    Args:
        user_following (list of str): Usernames you are following.
        user_followers (list of str): Usernames who are following you.

    Returns:
        tuple: A tuple of three lists:
            - non_followers (list of str): Users not following you back.
            - unrequited_followers (list of str): Users you are not following back.
            - mutual (list of str): Users who mutually follow you.

    Raises:
        Exception: If there is an error during the analysis (e.g. invalid input).
    """
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