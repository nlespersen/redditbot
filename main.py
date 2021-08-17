# Imports
import re
import os
import smtplib, ssl

import my_posts
from my_posts import *
import my_reddit
import my_email

# Check if text file is created and reads it
if not os.path.isfile("posts_found.txt"):
    posts_found = []
    print("No text file")
else:
    with open("posts_found.txt", "r") as f:
        posts_found = f.read()
        posts_found = posts_found.split("\n")
        posts_found = list(filter(None, posts_found))

# Get the top 10 posts in subreddit
Posts_redditposts = []
subreddit = reddit.subreddit("dota2")
for submission in subreddit.hot(limit=20):

    if submission.id not in posts_found:

        # search for posts
        if re.search("we", submission.title, re.IGNORECASE):
            # print posts found
            print("URL: ", submission.url)
            print("Title: ", submission.title)
            print("Comments: ", submission.num_comments)
            print("Score: ", submission.score)
            print("ID ", submission.id)

            Posts_redditposts.append(Posts(submission.title,
                                           submission.num_comments,
                                           submission.score,
                                           submission.url,
                                           submission.id))


print("\n")
print("***************************************************************")
print("\n")
for post in Posts_redditposts:
    print(post)
    print("")

# Email message body
message = "x"

print(message)

# Establish smtp connection to send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL(my_email.smtp_server, my_email.port, context=context) as server:
    server.login(my_email.sender_email, my_email.password)
    # Send email
    server.sendmail(my_email.sender_email, my_email.receiver_email, message)
