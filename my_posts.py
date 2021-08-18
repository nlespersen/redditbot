from datetime import datetime
# Class for posts
class Posts:
    def __init__(self, title="", comments=0, score=0, url="", sub_id="", posted=0):
        self.title = title
        self.comments = comments
        self.score = score
        self.url = url
        self.sub_id = sub_id
        self.posted = posted

    def __str__(self):
        return ("Title: " + self.title + "\n" +
                "Comments: " + str(self.comments) + "\n" +
                "Score: " + str(self.score) + "\n" +
                "Posted: " + self.posted + "\n" +
                #"Posted: " + str(datetime.utcfromtimestamp(self.posted).strftime('%Y-%m-%d')) + "\n" +
                "URL: " + "https://reddit.com" + str(self.url)
                )
