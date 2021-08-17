# Class for posts
class Posts:
    def __init__(self, title="", comments=0, score=0, url="", sub_id=""):
        self.title = title
        self.comments = comments
        self.score = score
        self.url = url
        self.sub_id = sub_id

    def __str__(self):
        return ("Title: " + self.title + "\n" +
                "Comments: " + str(self.comments) + "\n" +
                "Score: " + str(self.score) + "\n" +
                "URL: " + str(self.url))

    def spaces(self):
        