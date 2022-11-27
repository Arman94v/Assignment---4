import instaloader
import getpass

old_followers = []

f = open('followers.txt','r')
for line in f:
    old_followers.append(line)
f.close()

L = instaloader.Instaloader()

username = input('Enter your Username: ')
password = getpass.getpass('Enter your Password: ')
L.login(username, password)

profile = instaloader.Profile.from_username(L.context, "arman94i")

new_followers = []
for follower in profile.get_followers:
    new_followers.append(follower)

for old_followers in old_followers:
    if old_followers not in new_followers:
        print(old_followers)

f = open('new followers finder.txt','w')
for follower in new_followers:
    f.write(follower + '\n')

f.close()

