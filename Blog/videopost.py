from post import Post #call from file (post) a specific class (Post)

class VideoPost(Post):

    def __init__(self, title, author,url):
        super().__init__(title,author, None)
        self.video_url = url
        self.plays = 0

    def play(self):
        self.plays += 1

    def __str__(self):
        return "Title: " + self.title + " Author: " + self.author + " URL: " + self.video_url

samplePost = Post("I like Dogs", "PNP", "BOOMSHAKALAKA")
sampleVideo = VideoPost("sherlock vids", "pnp", "www.china.com")

samplePost.like()
sampleVideo.like() #inherited "like" method from the superclass Post

print(samplePost)
print(sampleVideo)
