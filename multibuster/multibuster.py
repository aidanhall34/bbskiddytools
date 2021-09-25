#!/bin/python3
# This was written so I can run multipule gobuster instances at the same time.
# At this stage it only allows you to run a default gobuster dir scan, probably more to come IDK
# This should be run from a VPS to avoid IP bans / blocks from your home IP
import os
import argparse
import subprocess
import concurrent.futures


# Define the Arguments
arguments = argparse.ArgumentParser('Thanks for using multibuster, this will run multipule gobuster dir scans for a list or URL\'s\n')
arguments.add_argument("-u", "--urlfile", help="The location on the URL file", type=str)
arguments.add_argument("-w", "--wordlist", help="The location on the wordlist", type=str)
arguments.add_argument('-o', "--outfolder", help="The location of the output file", type=str)
args = arguments.parse_args()

# Validate the Args
def checkargs():
    # Check the args are submitted
    if args.urlfile == None or args.wordlist == None or args.outfolder == None:
        print('Please supply a URL list, wordlist and output file location')
        print('Your command should look like:\nmultigobuster.py -u <URL list> -w <Wordlist> -o <Output folder>')
        exit()
    # Check for the URL file
    if os.path.exists(args.urlfile) != True:
        print('I can\'t find the URL file')
        exit()
    # Check for the wordlist
    if os.path.exists(args.wordlist) != True:
        print('I can\'t find the wordlist')
        exit()
    # Check for the output file path
    if os.path.exists(args.outfolder) != True:
        print('I can\'t find the output file path')
        exit()

checkargs()

# Manager the Gobuster session
def gobuster(URL):
    # Remove the URL prefix from the string to make it work as a file name
    if URL.startswith('http://'):
        outfile = args.outfolder + '/' + URL.replace('http://', 'http')
    if URL.startswith('https://'):
        outfile = args.outfolder + '/' + URL.replace('https://', 'https')
    URL = URL.strip()
    # Start the session
    print(f"Session for {URL} has started")
    session = subprocess.run(f"gobuster dir -u {URL} -w {args.wordlist.strip()} -o {outfile.strip() + '.log'}",capture_output=True, shell=True)
    # If the session dies
    if session.returncode != 0:
        print(f"Session for {URL} died")
        # Write the error to the log file
        with open(outfile.strip() + '.log', 'a') as f:
            f.write(f"Session for {URL} died with error code {session.returncode}\n ERROR MESSAGE:\n {session.stderr.decode()}")
            f.close
    print(f"Session for {URL} has ended")

# Working with Multiprocessing
with open(args.urlfile, 'r') as URLS:
    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(gobuster, URLS)
        


#### BUGS
# None that I know of atm. I am running some full tests on local systems. If you find one, lemme know
# Features to add:
# Limited fuzzer support(future project)
# Gobuster custom extension support (.txt,.php,.xml...)
# Gobuster custom responce code support (!429,!500,200)
# Gobuster better error handling (more then just writing it to a file)
# Test command with basic args
#multigobuster.py -u <URLfile> -w <Wordlist> -o <Outputfolder>
