#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding=utf8  


'''
Created on 22 Sep 2016

@author: phegde
'''

from subprocess import call
from string import Template
import codecs
import json
import os
        
def generate_pdf():
    try:
        #open the base_template
        f = codecs.open("base_template.html", 'r', 'utf-8')
        base_template = f.read()
        
        #open the raw json file
        raw_data =  open('profile.json')
        
        #encodes data to json
        json_data = json.load(raw_data)
        
        #replace placeholders with data from the json
        ready_for_generation = Template(base_template).safe_substitute(json_data)
        
        #write the ready_for_generation.html to disk
        FILE = open('ready_for_generation.html', "wb")
        FILE.write(ready_for_generation)
        FILE.close()
        
        #generate the PDF from the ready_for_generation.html
        call(["phantomjs", "rasterize.js", "ready_for_generation.html", "your_PDF.pdf"])
        
        #delete the ready_for_generation.html as it is no longer required
        os.remove('ready_for_generation.html')
        
    except Exception as e:
       print e
        
if __name__ == "__main__":
    generate_pdf()