#!/bin/python3
## This will find all of the forbidden assest from an aquatone header scan
import os
import argparse

# Arguments
arguments = argparse.ArgumentParser('Thanks for using 403 finder\nThis is meant to be used with aquatone to find all forbidden assets results from a aquatone headers file scan')
arguments.add_argument("-hp", "--headersfilepath", help="The location on the headers folder", type=str)
arguments.add_argument('-of', "--outputfolder", help="The location of the output file", type=str)

args = arguments.parse_args()

def checkargs():
    # Check to make sure the headers folder exists
    if args.headersfilepath == None:
        print('You must supply a headers folder')
        exit()
    # Check to make sure the output folder exists if output is required
    if os.path.exists(args.headersfilepath) != True:
        print('This folder doesn\'t exist')
    # If you provide an output folder make sure it exists
    if args.outputfolder != None:
        if not os.path.exists(args.outputfolder):
            print('Please create the output folder')
checkargs()
urls403 = []
defaultfile = '403.log'
# For all of the file names in the input path
for file in os.listdir(args.headersfilepath):
    with open(args.headersfilepath + '/' + file) as filecontents:
        for contents in filecontents.readlines():
            # Forbidden sites will start with a 403
            if contents.startswith('403'):
                # Clean up the crappy file name and gimme a URL to work with
                URL = file.replace('__', '://',1)
                URL = URL.split('__')
                URL = URL[0].replace('_', '.')
                print(URL)
                # Write to the URL's to a file if an output folder is provided
                if args.outputfolder != None:
                    urls403.append(URL)
                    outputfile = open(args.outputfolder + '/' + defaultfile, 'a')
                    outputfile.write(URL + '\n')
# Test run examples
#./aquatone403finder.py -hp <headers folder> -o <Where you want to put your output URL file>
