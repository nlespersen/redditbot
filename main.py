# Imports
import re
import os
import smtplib, ssl
from my_posts import *
from my_reddit import *
import my_email

if __name__ == "__main__":
    # Check if text file is created and reads it
    if not os.path.isfile("posts_found.txt"):
        posts_found = []
        print("No text file")
    else:
        with open("posts_found.txt", "a") as f:
            posts_found = f.read()
            posts_found = posts_found.split("\n")
            posts_found = list(filter(None, posts_found))

    # Get the top 10 posts in subreddit
    Posts_redditposts = []
    subreddit = reddit.subreddit("dota2")
    for submission in subreddit.hot(limit=20):

        if submission.id not in posts_found:

            # search for posts
            if re.search("patch", submission.title, re.IGNORECASE):
                Posts_redditposts.append(Posts(submission.title,
                                               submission.num_comments,
                                               submission.score,
                                               submission.permalink,
                                               submission.id))

    print("\n")
    print("***************************************************************")

    # convert Posts_redditposts list to string
    listToString = ''.join([str(item)+"\n" for item in Posts_redditposts])
    # add string to email_msg
    email_msg = "Subject: New Reddit posts found!"+"\n"+"\n"+"\n"+listToString
    print(email_msg)

    print("***************************************************************")

    # Establish smtp connection to send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(my_email.smtp_server, my_email.port, context=context) as server:
        server.login(my_email.sender_email, my_email.password)
        # Send email
        server.sendmail(my_email.sender_email, my_email.receiver_email, email_msg)

    #os.remove("out.txt")