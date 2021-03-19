import instaloader
i = instaloader.Instaloader()
username = input("enter username:- ")
i.download_profile(username,profile_pic_only=True)
