# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests

url = 'http://localhost:5000/results'
r = requests.post(url,json={'cico':0.5, 'chem2':3.2, 'chem3':2.4, 
                            'chem4':0, 'chem5':1, 'chem6':2.6})

print(r.json())