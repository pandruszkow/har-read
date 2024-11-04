#!/usr/bin/env python3
#Purpose: List and extract files contained in a HAR file (example: browser traffic dump after loading a website)
#Usage: har-read.py [-x] <filename>.har
#Author: Piotr Andruszkow, (c) 2024
#Licence: GNU GPLv3

import base64
import json
import os
import sys
from argparse import ArgumentParser

#Just the URLs
def list_urls(har_data):
    urls = [entry['request']['url'] for entry in har_data['log']['entries']]
    return urls

#Just the filenames, non-hierarchical
def list_all(har_data):
    urls = list_urls(har_data)
    for url in urls:
        filename = os.path.basename(url)
        print(filename if filename else url)

#Extract to a preset directory
def extract_all(har_data):
    os.makedirs('har_extracted', exist_ok=True)
    os.chdir('har_extracted')

    for entry in har_data['log']['entries']:
        url = entry['request']['url']
        content = entry['response']['content'].get('text', '')
        filename = os.path.basename(url)
        
        if filename:
            #If we get a base64 blob, write it directly to file as binary. PNGs and the like will fail to decode as valid UTF-8.
            mode = 'wb'
            if 'base64' in entry['response']['content'].get('encoding', ''):
                content = base64.b64decode(content)
            else:
                mode = 'w'
            with open(filename, mode) as f:
                f.write(content)
            print(f"Extracted: {filename}, URL {url}")

    os.chdir('..')

def main():
    parser = ArgumentParser(prog='har-read.py', description="List or extract contents of a HAR file.")
    parser.add_argument('-x', '--extract', action='store_true', help="Extract content from HAR file")
    parser.add_argument('har_file', help="Path to the HAR file")
    args = parser.parse_args()

    if not os.path.isfile(args.har_file):
        print(f"File not found or isn't a file: {args.har_file}")
        sys.exit(1)
    else:
        with open(args.har_file, 'r') as har_file:
            har_data = json.load(har_file)
            if args.extract:
                extract_all(har_data)
            else:
                list_all(har_data)

if __name__ == "__main__":
    main()
