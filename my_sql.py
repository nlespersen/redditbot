import pyodbc
from main import *

connect = pyodbc.connect(
    server="127.0.0.1",
    database="PostsDB",
    user='sa',
    tds_version='7.4',
    password="MYpassword1!",
    port=1433,
    driver='/usr/local/lib/libtdsodbc.so'
)
cursor = connect.cursor()

def selectReddit():
    cursor.execute("SELECT SubmissionId, Title, Comments, Posted FROM dbo.redditposts")
    for row in cursor.fetchall():
        print(row)

# Insert into table
#for posts in Posts_redditposts:

 #   cursor.execute("insert into redditposts(SubmissionId, Title, Comments, Posted) values(?,?,?,?)",
  #                 posts.sub_id,
  #                 posts.title,
  #                 posts.comments,
  #                 posts.posted)
  #  connect.commit()
# commit the transaction
#selectReddit()