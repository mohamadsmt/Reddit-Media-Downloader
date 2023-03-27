import praw
import urllib.request
import os
import tkinter as tk
from tkinter import ttk

class RedditMediaDownloader:
    def __init__(self, root):
        # Create a Reddit instance using your app credentials
        self.reddit = praw.Reddit(client_id='your_client_id',
                                  client_secret='your_client_secret',
                                  user_agent='your_user_agent')

        # Create the GUI
        self.root = root
        self.root.title("Reddit Media Downloader")
        self.root.geometry('400x300')

        # Create a label and entry box for the Reddit username
        self.reddit_username_label = ttk.Label(self.root, text="Enter a Reddit username:")
        self.reddit_username_label.grid(column=0, row=0, padx=5, pady=5)

        self.reddit_username_entry = ttk.Entry(self.root, width=30)
        self.reddit_username_entry.grid(column=1, row=0, padx=5, pady=5)

        # Create a button to start downloading media
        self.download_button = ttk.Button(self.root, text="Download Media", command=self.download_media)
        self.download_button.grid(column=0, row=1, columnspan=2, padx=5, pady=5)

        # Create a label to show the status of the download process
        self.status_label = ttk.Label(self.root, text="")
        self.status_label.grid(column=0, row=2, columnspan=2, padx=5, pady=5)

    def download_media(self):
        # Retrieve the username from the entry box
        username = self.reddit_username_entry.get()

        # Retrieve the user object for the specified username
        try:
            redditor = self.reddit.redditor(username)
        except:
            self.status_label.configure(text=f"Error: Could not retrieve user {username}.")
            return

        # Make a directory to store the media files
        directory = f"{username}_media"
        if not os.path.exists(directory):
            os.makedirs(directory)

        # Loop through each submission made by the user
        count = 0
        for submission in redditor.submissions.new():
            # Retrieve the URL of the submission
            url = submission.url

            # Check if the URL is an image or video link
            if url.endswith('.jpg') or url.endswith('.png') or url.endswith('.gif'):
                # Download the image or gif
                urllib.request.urlretrieve(url, f"{directory}/{submission.id}_{submission.title}.{url.split('.')[-1]}")
                count += 1
            elif url.endswith('.gifv'):
                # Download the gifv as an mp4
                urllib.request.urlretrieve(url.replace('.gifv', '.mp4'), f"{directory}/{submission.id}_{submission.title}.mp4")
                count += 1
            elif url.endswith('.mp4'):
                # Download the mp4
                urllib.request.urlretrieve(url, f"{directory}/{submission.id}_{submission.title}.mp4")
                count += 1

        self.status_label.configure(text=f"{count} media files from {username} have been downloaded and stored in the {directory} directory.")


root = tk.Tk()
app = RedditMediaDownloader(root)
root.mainloop()
