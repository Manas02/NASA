import requests
import json


def mars(rover_name : str, api_key : str, date : str) -> None:
    url = f"https://api.nasa.gov/mars-photos/api/v1/rovers/{rover_name}/"\
            f"photos?earth_date={date}&api_key={api_key}"
    response = requests.get(url)

    json_data = response.content
    json_object = json.loads(json_data)

    url = [i['img_src'] for i in json_object['photos']]
    cam = [i['camera']['name'] for i in json_object['photos']]

    data = [url, cam]

    with open('mars.md','w') as f:
        f.write(f"# {rover_name.capitalize()} \n### Date : {date}\n\n")
        for i in range(len(data[0])):
            f.write('\n### ' + data[1][i] + ":\n")
            f.write("\n![](" + data[0][i] + ")\n")

mars(input("Rover :\n\tSpirit\n\tCuriosity\n\tOpportunity\n-> "), "DEMO_KEY", input("Date \n-> "))
