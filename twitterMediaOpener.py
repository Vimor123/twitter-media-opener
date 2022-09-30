import webbrowser

def open_twitter_media(user):
    url = "https://twitter.com/" + user + "/media"
    webbrowser.open_new(url)

user_list_file = open("users.txt")

for user_profile in user_list_file:
    open_twitter_media(user_profile)

user_list_file.close()
