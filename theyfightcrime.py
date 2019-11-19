# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 12:26:55 2019

@author: gordon.garisch
Created for FE595 Assignment 2
"""

from requests import get # import for curl
import re # regex package
import time # sleep function to delay curl requests


def theyfightcrime():

    # Open files for writing
    m= open("hes.txt","w+")
    f= open("shes.txt","w+")
    
    # Do this 50 times
    for i in range(50):
        # Retrieve HTML from website
        text = get("http://www.theyfightcrime.org").text
        
        # Set up regexp object
        # Text for male and female superheroes is found between 
        # <P> and ". They fight crime!"
        r = re.compile("(<P>(.+?). They fight crime!)")
        
        # Execute regexp search to retrieve test
        strings = r.findall(text)
        
        # Write to files
        # She must be added back as this is what is split on.
        # Splitting on She is required since the period between 
        # the two sentences is often ommitted.
        m .write("{}. {}\n".format(i+1,strings[0][1].split(" She")[0]))
        f.write("{}. {}{}\n".format(i+1,"She",strings[0][1].split(" She")[1]))
        
        # Wait a while
        time.sleep(0.05)
    
    # Close the text files    
    m.close()
    f.close()

if __name__ == "__main__":
    theyfightcrime()