#This function goes to a reddit link, retrieves the title, and up to 3 responses depending on the length
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import praw
import pandas as pd

def RedditScraper(numberOfStories):
    numberOfStories+=2
    
    reddit = praw.Reddit(

    client_id="CLIENT ID",

    client_secret="CLIENT SECRET",

    user_agent="my user agent" )


    titles = []
    file = open("Stories", "w")
    for count, submission in enumerate(reddit.subreddit("stories").hot(limit=numberOfStories)): #set count to x-10 to get story
        if count == 0 or count == 1:
            continue
        print("-----------------------------------------------------------------------")
        print(submission.title)
        titles.append(submission.title)
        
       # print(vars(submission))
        print("\n"+ "\n"+"\n"+submission.selftext)
        print("-----------------------------------------------------------------------")
        
        file.write(submission.title + "\n")
        file.write("\n"+ "\n"+"\n"+ str(submission.selftext) +"\n")
        file.write("-----------------------------------------------------------------------\n")
    
    
    file.close()
    return titles
