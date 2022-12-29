import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()
setlist_api_key = os.getenv('SETLIST_API_KEY')


def get_setlist(setlist_id):
    # setlist info

    # get track info from setlist
    url = f'https://api.setlist.fm/rest/1.0/setlist/{setlist_id}'
    headers = {'x-api-key': setlist_api_key, 'Accept': 'application/json'}

    response = requests.get(url, headers=headers)
    setlistdata = json.loads(response.text)

    artist = setlistdata["artist"]["name"]
    songs = []
    for set_item in setlistdata['sets']['set']:
        for song_item in set_item['song']:
            songs += [song_item['name']]
    return artist, songs


if __name__ == "__main__":
    get_setlist('4bbf0f46')
