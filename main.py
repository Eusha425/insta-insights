import data_loader as dl
import analyser as anl
import visualiser as vl

user_followers = dl.find_followers()
user_following = dl.find_following()

non_followers, unrequited_followers, mutual = anl.following_follower_analysis(user_following, user_followers)

print("🔴 Not Following You Back:")
print(non_followers)

print("\n🟢 You Are Not Following Back:")
print(unrequited_followers)

print("\n🔁 Mutual Followers:")
print(mutual)

vl.visualisation(mutual, non_followers, unrequited_followers)