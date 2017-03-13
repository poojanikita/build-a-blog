class Post:
    def __init__(self, title, author, body):
        self.title = title
        self.author = author
        self.body = body
        self.likes = 0

    def like(self):
        self.likes += 1

    def __str__(self):
        return self.title + " by " + self.author

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

class LinkPost(Post):
    def __init__(self, title, author, url):
        super().__init__(title, author, None)
        self.link_url = url
        self.clicks = 0

    def clicks(self):
        self.clicks += 1

    def __str__(self):
        return self.title + " has " + str(self.clicks) + " clicks " + " URL: " +  self.link_url
sampleLink = LinkPost("boom", "blap", "www.googlyeyes.com")
print(sampleLink)

class ImagePost(Post):
    def __init__(self, title, author, file_name):
        super().__init__(title, author, None)
        self.file_nm = file_name

    def __str__(self):
        return self.title + " by " + self.author + " at " + self.file_nm

sampleImage =  ImagePost("bobba", "pooja", "bubbles.gif")
print(sampleImage)
