# Imports
import re
import os
import smtplib, ssl
from my_posts import *
from my_reddit import *
from my_email import *
from my_sql import *

if __name__ == "__main__":

    # Get data from SQL table redditposts
    cursor.execute("select submissionid from redditposts")
    sql_list = []
    for row in cursor.fetchall():
        data = ''.join(row)
        sql_list.append(data)
    if not sql_list:
        print("No data found in Table: redditposts")
    else:
        print(sql_list)

    # Get the top 20 posts in subreddit
    Posts_redditposts = []
    subreddit = reddit.subreddit("dota2")
    for submission in subreddit.hot(limit=20):
        if submission.id not in sql_list:
            # search for posts
            if re.search(r'\bpatch\b', submission.title, re.IGNORECASE):
                Posts_redditposts.append(Posts(
                    (submission.title[:95] + '...') if len(submission.title) > 95 else submission.title,
                    submission.num_comments,
                    submission.score,
                    submission.permalink,
                    submission.id,
                    str(datetime.utcfromtimestamp(submission.created_utc).strftime('%Y-%m-%d'))))

    print(Posts_redditposts)

    if not Posts_redditposts:
        print("No new posts found")
    else:
        # convert Posts_redditposts list to string
        listToString = ''.join([str(item) + "\n" for item in Posts_redditposts])

        # add string to email_msg
        email_msg = "Subject: New Reddit posts found!" + "\n" + "\n" + "\n" + listToString
        print(email_msg)
        print("***************************************************************")

        # Sql insert data from Posts_redditposts object
        for posts in Posts_redditposts:
            cursor.execute("insert into redditposts(SubmissionId, Title, Comments, Posted) values(?,?,?,?)",
                           posts.sub_id,
                           posts.title,
                           posts.comments,
                           posts.posted)
            connect.commit()

        # Show redditpost sql table entries
        selectReddit()
        # Close sql connection
        connect.close()

        # Establish smtp connection to send email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            # Send email
            server.sendmail(sender_email, receiver_email, email_msg)