#!/usr/bin/env python

import json
import requests

def apod(api_key : str, date = None) -> None:
    if date != None:
        url = f"https://api.nasa.gov/planetary/apod?date={date}&api_key={api_key}"
    else:        
        url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"

    response = requests.get(url)
    json_data = response.content
    json_object = json.loads(json_data)

    with open('apod.md','w') as f:
        data =  {'title':json_object['title'],'url':json_object['url'], 
                'explanation':json_object['explanation'],'date':json_object['date']}
        f.write(f"# {data['title']}\n#### Date : {data['date']}\n## Description :" \
                f"\n\t{data['explanation']}\n## Image:\n\n![]({data['url']})\n\n")


apod("DEMO_KEY", input("Date : "))
