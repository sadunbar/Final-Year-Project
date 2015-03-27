#!/usr/bin/python

__author__ = 'Stephen Dunbar'

import urllib2
import urllib
import urlparse
from hashlib import md5
from urlparse import urlsplit
import re
import os

from PyQt4.QtGui import *
from bs4 import BeautifulSoup  # for HTML parsing
import flickr

def get_library_file():
    library_file = QFileDialog.getOpenFileName(None, 'Select Library File')
    return library_file


def scrape_url(url, library_file):
    error = ['INVALID URL']
    file_record = {}
    output = []
    try:
        urlContent = urllib2.urlopen(url).read()
        soup = BeautifulSoup(''.join(urlContent))
        imgTags = soup.findAll('img')  # find all image tags
    except:
        return error
    # change directory to download image files to
    os.chdir('/home/stephen/PycharmProjects/APP2/temp')
    # download all images to temp file
    for imgTag in imgTags:
        imgUrl = imgTag['src']
        try:
            imgData = urllib2.urlopen(imgUrl).read()
            fileName = os.path.basename(urlsplit(imgUrl)[2])
            file_record[fileName] = imgUrl
            with open(fileName, 'wb') as f:
                f.write(imgData)
        except:
            pass
    results = search_for_match(library_file)
    for files, urls in file_record.items():
        for image, file_path in results.items():
            if files == image:
                output.append('{}\nMatches - {}'.format(urls, file_path))
    return output


global urlList
urlList = []


def scrape_recursive(url, level, library_file):
    # change directory to download image files to
    os.chdir('/home/stephen/PycharmProjects/APP2/temp')
    global urlList
    file_record = {}
    outputs = []
    if url in urlList:  # prevent using the same URL again
        return
    urlList.append(url)
    try:
        urlContent = urllib2.urlopen(url).read()
    except:
        return

    # find and download all images
    imgUrls = re.findall('<img .*?src="(.*?)"', urlContent)
    for imgUrl in imgUrls:
        try:
            imgData = urllib2.urlopen(imgUrl).read()
            fileName = os.path.basename(urlsplit(imgUrl)[2])
            file_record[fileName] = imgUrl
            output = open(fileName, 'wb')
            output.write(imgData)
            output.close()
        except:
            pass

    # recursion through other links on web page
    if level > 0:
        linkUrls = re.findall('<a .*?href="(.*?)"', urlContent)
        if len(linkUrls) > 0:
            for linkUrl in linkUrls:
                scrape_recursive(linkUrl, level - 1, library_file)
    results = search_for_match(library_file)
    for files, urls in file_record.items():
        for image, file_path in results.items():
            if files == image:
                outputs.append('{}\nMatches - {}'.format(urls, file_path))
    return outputs


url_list = []  # store a list of what was downloaded


def flickr_download(tag, number, library_file):
    file_record = {}
    output = []
    os.chdir('/home/stephen/PycharmProjects/APP2/temp')
    # downloading image data
    f = flickr.photos_search(tags=tag, per_page=number)
    # downloading images
    for k in f:
        url = k.getURL(size='Small', urlType='source')
        url_list.append(url)
        file_name = os.path.basename(urlparse.urlparse(url).path)
        file_record[file_name] = url
        image = urllib.URLopener()
        image.retrieve(url, file_name)

    results = search_for_match(library_file)
    for files, urls in file_record.items():
        for image, file_path in results.items():
            if files == image:
                output.append('{}\nMatches - {}'.format(urls, file_path))
    return output


def search_for_match(library_file):
    testhash = {}
    with open(library_file, 'r')as f:
        lf = f.readlines()
    for line in lf:
        a, b = line.split(' : ')
        testhash[a] = b

    return check_hashes(testhash, hash_image_files())


# create a dictionary of hashes from downloaded image files
def hash_image_files():
    hashes = {}
    for files in os.listdir("."):
        hasher = md5()  # reset md5 generator
        with open(files, 'rb') as afile:
            buf = afile.read()
            hasher.update(buf)
            hashes[hasher.hexdigest()] = files
    return hashes


def check_hashes(known_hashes, image_hashes):
    results = {}
    for hash, file_path in known_hashes.items():
        for target_hash, target_image in image_hashes.items():
            if target_hash == hash:
                results[target_image] = file_path
    return results