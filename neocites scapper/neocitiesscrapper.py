#!/bin/python3
# I wrote this to find the page a fake Covid-19 vaccine passport web site hosted by neocites (Still waiting for a response from them).
# It loops through the search pages and looks for the target URL.
# The site has been reported to the ASD (Australian Signals Directorate).
# If you are thinking of creating an Australian fake Covid-19 vaccination certificate website please know I'll find and report you.
# Don't fuck around, just get the jab for yourself and people around you.
# The vaccine isn't an invasion of your rights, it's an obligation of living in a productive society.
# Rant over, now for the nerd stuff:
# If we know which page has the site listed we can then go and find the site statics including:
# The time it was first uploaded
# The time it was last updated
# Traffic stats about the site including total requests and unique requests
# This one of many tools used to enumerate the and find informamtion about the site.

import requests
from bs4 import BeautifulSoup
# Neocites search function, this searches by the pages which have been updated most recently
url = 'https://neocities.org/browse?sort_by=last_updated&tag=&page='
# Change this to the site you want to find:
target = 'https://<sitename>.neocities.org'
pagenum = 1
# Check the latest max page number to ensure you are covering all of the baseses
maxpage = 1699
links = []
while pagenum < maxpage:
    r = requests.get(url + str(pagenum))
    soup = BeautifulSoup(r.content, 'html.parser')
    print('Checking: ' + r.request.url)
    for link in soup.find_all('a'):
        if link.get('href') == target:
            print(link.get('href') + " found on page " +  str(pagenum))
            print(r.request.url)
            exit()
    pagenum = pagenum + 1
