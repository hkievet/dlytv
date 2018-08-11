#!/usr/bin/env python3
import sys
import os
import subprocess
from pytube import YouTube

# Downloads YouTube Video to directory this was called from
urls = sys.argv[1:]

dirName = "tmp"
ogContents = []

if (not(os.path.exists(dirName))):
        os.makedirs(dirName)
        ogContents = os.listdir(dirName)


for url in urls:
        yt = YouTube(url)
        yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(dirName)

# convert to thing
newContents = os.listdir(dirName)


for content in newContents:
    if not(content in ogContents):
        fileToConvert = dirName + "/" + content
        outputName = content[0:str.find(content, ".")] + ".mp3"
        subprocess.call(["ffmpeg", "-i", fileToConvert, "-f", "mp3", "-ab", "192000", "-vn", outputName])

