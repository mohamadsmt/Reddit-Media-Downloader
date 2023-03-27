# Reddit Media Downloader

A Python program for downloading all media files (images, gifs, and videos) posted by a specified Reddit user, using the PRAW library.

## Features

- Downloads all media files associated with a specified Reddit username
- Works with images (.jpg, .png) and gifs (.gif, .gifv) as well as videos (.mp4)
- Automatically creates a new directory to store the downloaded media files
- Provides a simple Graphical User Interface (GUI) using the tkinter library

## Prerequisites

Before running this program, you'll need to:

- Create a new Reddit app on [Reddit's website](https://www.reddit.com/prefs/apps) (you'll need to sign in to Reddit if you haven't already)
- Make a note of your app's client ID, client secret, and user agent (you'll need these to create a Reddit instance in the Python program)
- Install the following Python libraries (you can use pip to install them):
  - praw
  - tkinter
  
## Usage

To use this program:

1. Clone this repository or download the zip file and extract the contents to a local directory
2. Open the `reddit_media_downloader_gui.py` file in a Python editor or IDE
3. Update the `client_id`, `client_secret`, and `user_agent` variables with your app credentials from the Reddit website
4. Run the `reddit_media_downloader_gui.py` file from the Python editor or IDE
5. Enter the Reddit username you want to download media from in the text box and click the "Download Media" button
6. Wait for the program to finish downloading the media files (the status label will show you how many files were downloaded and where they were stored)

## License

This program is licensed under the MIT License. See the `LICENSE` file for details.

## Contributing

Contributions are welcome! If you find a bug, have a feature request, or want to contribute code or documentation, please submit an issue or pull request on GitHub.

