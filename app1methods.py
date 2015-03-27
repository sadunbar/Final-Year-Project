#!/usr/bin/python


__author__ = 'Stephen Dunbar'

import hashlib
import os

from PyQt4.QtGui import *


# to check for the presence of a file to avoid duplicates
def check_file(testhash, outfile):
    with open(outfile, 'r') as f:
        for name, sig in testhash.items():
            for line in f:
                line = line.strip("\n")
                a, b = line.split(" : ")
                if sig == b:
                    return True
    return False


def ask_yes_no():
    answer = QMessageBox.critical(None, "Create File?", "Create New Library File?", QMessageBox.Yes, QMessageBox.No)
    if answer == QMessageBox.Yes:
        return True
    else:
        return False


def create_file():
    if ask_yes_no():
        create = QFileDialog.getSaveFileName(None, 'Create New Library File')
        if file:
            with open(create, 'w'):
                return create
    else:
        create = QFileDialog.getOpenFileName(None, 'Select Library File')
        return create


def add_file():
    file_name = QFileDialog.getOpenFileName(None, 'Select file to add to library')

    out_file = create_file()
    test_hash = dict()
    hasher = hashlib.md5()
    with open(file_name, 'rb') as afile:
        buf = afile.read()
        hasher.update(buf)
        test_hash[hasher.hexdigest()] = file_name

    if not (check_file(test_hash, out_file)):
        # write both the the file name/path and the resulting hash to a text file
        with open(out_file, 'a') as f:
            for name, sig in test_hash.items():
                f.write(name + " : " + sig + "\n")
            return "File : " + sig + " - added"
    else:
        return "File : {} - already exists".format(file_name)


# to add files to a list from which to check against for matches
def add_directory():
    # dictionary to store the hashes and file names from the test files
    test_hash = dict()
    test = {}
    total = 0
    # open the file chooser dialogue and store chosen file and file path
    dirname = QFileDialog.getExistingDirectory(None, 'Please select a directory')
    library = create_file()

    text_output = []
    # get the file, hash it and store both in dictionary
    os.chdir(dirname)
    for f in os.listdir('.'):
        hasher = hashlib.md5()
        if os.path.isfile(f):
            with open(f, 'rb') as afile:
                buf = afile.read()
                hasher.update(buf)
                test_hash[hasher.hexdigest()] = dirname + '/' + f
    with open(library, 'r') as f:
        a = f.readlines()
        for line in a:
            b, c = line.split(' : ')
            test[b] = c
    with open(library, 'a') as f:
        for name, sig in test_hash.items():
            if name not in test:
                text_output.append(sig)
                total += 1
                f.write(name + " : " + sig + "\n")
    text_output.append("{} Files added".format(total))
    return text_output


# to remove files from the library
def delete_image():
    # dictionary to store the hashes and file names from the test files
    test_hash = {}
    temp = {}
    # open the file chooser dialogue
    file_name = QFileDialog.getOpenFileName(None, 'Select File to Remove')
    library = QFileDialog.getOpenFileName(None, 'Select Library File')
    # reset the hasher to ensure matches for identical files
    hasher = hashlib.md5()

    # get the file, hash it and store both in dictionary
    with open(file_name, 'rb') as f:
        buf = f.read()
        hasher.update(buf)
        test_hash[hasher.hexdigest()] = file_name
        f.close()

    if check_file(test_hash, library):
        # remove both the the file name/path and the resulting hash from the text file
        result = QMessageBox.critical(None, "Delete?", "Are You Sure You Want\nTo Remove This File?", QMessageBox.Yes,
                                      QMessageBox.No)
        if result == QMessageBox.Yes:
            with open(library, 'r') as f:
                for name, sig in test_hash.items():
                    for line in f:
                        line = line.strip("\n")
                        a, b = line.split(" : ")
                        if name != a:
                            temp[a] = b

            os.remove(library)
            with open(library, 'a')as f:
                for name, sig in temp.items():
                    f.write(name + " : " + sig + "\n")
            return 'File : {} - Deleted'.format(file_name)
    else:
        return "File does not exist!"