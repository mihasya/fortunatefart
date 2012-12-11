#!/usr/bin/env python
import subprocess, os, sys, optparse, random

parser = optparse.OptionParser()
parser.add_option('-o', '--odds', type=int, action='store', dest='odds', default=360)

(options, args) = parser.parse_args()

files = os.listdir(args[0])
odds = options.odds * len(files)

os.chdir(args[0])

fortune = random.randint(1, odds)
index = fortune % len(files)

if fortune <= len(files):
    subprocess.Popen(['afplay', files[index]], stdout=subprocess.PIPE).communicate()
