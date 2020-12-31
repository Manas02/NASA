#!/usr/bin/env python

"""
MIT License. 

Copyright (c) 2020 Manas Mahale

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import re
import urllib.request 
import json
import os

# Clearing the screen
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
    print('\nNasa Mars Rover Image Search :')
cls()

# Add API key 
api = input("API key : ")
cls()

# Creating URL
print("\nChose a rover from given options 1️⃣ ,2️⃣ or3️⃣ :")
rover = ["","opportunity","curiosity","spirit"][int(input("\t1️⃣ Opportunity\n\t2️⃣ Curiosity\n\t3️⃣ Spirit\n>>> "))]
cls()

a = input('\nEnter a Date in YYYY-MM-DD Format\n\t📆📆📆 >> ')
earth_date = "&earth_date=" + a
cls()

camera = ["","FHAZ","RHAZ","MAST","PANCAM","MINITES","CHEMCAM","MAHLI","MARDI","NAVCAM",""][int(input("\nChoose a Camera:\n\t1️⃣  FHAZ\t2️⃣  RHAZ\t3️⃣  MAST\t4️⃣  PANCAM\t5️⃣  MINITES\n\t6️⃣  CHEMCAM\t7️⃣  MAHLI\t8️⃣  MARDI\t9️⃣  NAVCAM\t🔟 ALL\n>>> "))]
cls()


print('\nYou selected ->')
print("🤖 -> " + rover,end='      ')
print("📅 -> "+ a[-2:]+'/'+a[-5:-3]+'/'+ a[:4],end='      ')
print('🎥 ->',camera if camera != "" else "All")


url = f"https://api.nasa.gov/mars-photos/api/v1/rovers/{rover}/photos?{earth_date}${camera}&api_key={api}"


req = urllib.request.urlopen(url).read() 


if req == b'{"photos":[]}':
    cls()
    print(f"🛑🛑🛑 There are no Images of mars for {rover} rover on {a[-2:]+'/'+a[-5:-3]+'/'+ a[:4]} with {camera} camera.\n🟡🟡🟡 Try again with different inputs")
    quit()
else :
    res = json.loads(req)
    data = (json.dumps(res, indent = 4, sort_keys=True))
    
    
    # RegEx
    url = '"http.+"'
    sol = '"sol":.+'
    rover = '"name":.+'
    camera = '"full_name":.+'
    
    
    # Find RegEx pattern
    result1 = re.findall(url, data)
    result2 = re.findall(sol, data)
    result3 = re.findall(camera, data)
    result4 = re.findall(rover, data)
    
    
    # # Making .MD file with image Urls
    with open('./mars.md','w') as g:
        g.write("# Rover name : " + result4[1][9:-2] + '\n')
        g.write("## camera : " + result3[0][14:-2] + '\n')
        g.write("## sol : " + result2[0][-4:-1] + '\n')
        # Adding image url
        for i in result1:
            g.write('![]('+i[1:-1]+')\n')
    
    
    print('\nDone ✅✅✅\nNow open mars.md to see the images 🌠🌠🌠\n')
