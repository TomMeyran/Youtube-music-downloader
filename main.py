#######################################################
# Created by Tom Meyran
#######################################################
from pytube import YouTube, Playlist
import pytube                                                       # helpers
import os
import random
import subprocess
from termcolor import colored

def getPlaylist(playlist_link, start_at=0, stop_at=0):
    video_links = list(Playlist(playlist_link).video_urls)          # get video links in a list
    video_titles = []                                               # create a list for the titles
    for link in video_links:                                        # put titles in the list
        video_titles.append(YouTube(link).title)
    appeareances = dict(zip(video_titles, [0] * len(video_titles))) # appearances counts the number of times a title is
                                                                    # in the list. It creates a dict of the titles that
                                                                    # have as many empty elements in its elements as
                                                                    # videos in the playlist
    for i in range(len(video_titles)):                            # for each of the titles
        title = video_titles[i]                                   # take individual title
        if appeareances[title] > 0:                               # if it shows in appearances
            print(colored('remove at index: ', 'blue'), i)        # it should be removed with the help of its index
            video_titles[i] = None                                # replaces duplicates with None
            video_links[i] = None                                 # replaces duplicates with None
        else:                                                     # if the title is not yet in appearances
            appeareances[title] += 1                              # add it
    video_links = [x for x in video_links if x is not None]       # using list comprehension, removes None elements in the
                                                                  # list leaving only relevant links
    video_titles = [x for x in video_titles if x is not None]     # using list comprehension, removes None elements in the
                                                                  # list leaving only relevant titles
    print(video_titles, colored(len(video_titles), 'blue'))       # prints the list of titles
    print(video_links, colored(len(video_links), 'blue'))         # prints the list of links
    if stop_at != 0:                                              # if there is a stopping point (starting point also
                                                                  # optional)
        for i in range(start_at, stop_at):
            yt = YouTube(video_links[i])                          # gets the links
            yt.title = video_titles[i]                            # gets the titles
            print(yt.title)
            video = yt.streams.filter(only_audio=True).first()    # gets the audio
            a=pytube.helpers.safe_filename(yt.title)+'.mp3'
            b=os.listdir(outputPath)
            # the safe_filename is used because windows doesn't allow all symbols that may appear in a title. comparing
            # the safe name with the file in the output folder prevents missing files with those illegal symbols like :
            # that would cause an attempt to download and an error
            if pytube.helpers.safe_filename(yt.title)+'.mp3' in os.listdir(outputPath): # if file exists already in the
                                                                                        # output folder
                print(colored("File already exists, skipping",'red'))
            else:                                                 # if file doesn't exist already in the output folder
                out_file = video.download(output_path=outputPath) # download mp4 file
                subprocess.run(['ffmpeg', '-i', mp4_file, mp4_file.removesuffix('4') + '3'])  # convert mp4 to mp3
                print('converted to mp3')
                os.remove(mp4_file)                               # delete mp4
                print('mp4 removed')
                print(colored(str(i)+'done','green'))             # prints the index of the finished file
    else:  # if no stopping point was given it assumes no starting point and will download the whole list
        for i in range(len(video_links)):
            yt = YouTube(video_links[i])
            yt.title=video_titles[i]
            print(yt.title)
            video = yt.streams.filter(only_audio=True).first()
            if pytube.helpers.safe_filename(yt.title)+'.mp3' in os.listdir(outputPath):
                print(colored("File already exists, skipping",'red'))
            else:
                out_file = video.download(output_path=outputPath)
                subprocess.run(['ffmpeg', '-i', out_file, out_file.removesuffix('4') + '3'])  # convert mp4 to mp3
                print('converted to mp3')
                os.remove(out_file)                               # delete mp4
                print('mp4 removed')
                print(colored(str(i) + 'done','green'))           # prints the index of the finished file


def getLink(link):
    print(link)
    yt = YouTube(link)
    print(yt.title)
    video = yt.streams.filter(only_audio=True).first()  # locates the audio part of the youtube video
    mp4_file = video.download(output_path=outputPath)   # must download an mp4 file. If not converted the file will have missing headers
    subprocess.run(['ffmpeg', '-i', mp4_file, mp4_file.removesuffix('4') + '3'])  # convert mp4 to mp3
    print('converted to mp3')
    os.remove(mp4_file)  # delete mp4
    print('mp4 removed')
    print(colored('done', 'green'))  # prints the index of the finished file

outputPath= r".\\"           # here the mp4 file
playlist_link = ''  #link goes here
link=''     #link goes here
# Uncomment what you want to use
#getPlaylist(playlist_link)      #for playlists
getLink(link)                  #for single videos
#getVid(vid_link)
print("Song is at: \n",colored(outputPath,'blue'))
