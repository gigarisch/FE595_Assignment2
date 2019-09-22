# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 12:26:55 2019

@author: gordon.garisch
Created for FE595 Assignment 2
"""

from requests import get # import for curl
import re # regex package
import time # sleep function to delay curl requests
import os

# Open files for writing
os.chdir("C:\\Users\\gordon.garisch\\Documents\\Projects\\Stevens\\fe595\\FE595_Assignment2")
m= open("hes.txt","w+")
f= open("shes.txt","w+")

# Do this 50 times
for i in range(50):
    # Retrieve HTML from website
    text = get("http://www.theyfightcrime.org").text
    
    # Set up regexp object
    r = re.compile("(<P>(.+?)</P>)")
    
    # Execute regexp search to retrieve test
    strings = r.findall(text)
    
    # Write to files
    m .write("{}. {}\n".format(i+1,strings[0][1].split(". ")[0]))
    f.write("{}. {}\n".format(i+1,strings[0][1].split(". ")[1]))
    
    # Wait a while
    time.sleep(0.05)

# Close the text files    
m.close()
f.close()
