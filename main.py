from TextToSpeech import TextToSpeech
from RedditScraper import RedditScraper
from videoClipper import videoClipper
from videoSplitter import videoSplitter
from Subtitles import Subtitles
def main():
    numberofPosts = int(input("Enter amount of posts: "))
    titles = RedditScraper(numberofPosts)
    TextToSpeech()
    videoClipper(numberofPosts)
    titles = videoSplitter(numberofPosts, titles)
    Subtitles(titles)

main()