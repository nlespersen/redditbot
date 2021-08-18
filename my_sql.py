import pyodbc

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

