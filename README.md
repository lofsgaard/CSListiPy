# CSListiPy

#### Video Demo:  xxx
#### Description: Creates a spotify playlist using data from a live setlist at setlist.fm. 
#### This is my final project for Harvards CS50X

## Installation
For this project I used [Poetry](https://python-poetry.org/) to manage package dependencies.

For Poetry:

Step 1:
Clone or  this repository to a local folder

Step 2:
Create a virtual environment using Poetry:


`cd to the folder where the code is located`
```
poetry shell
```
To install dependencies:
```
poetry install
```

For other virtual environment:

Create a virtual environment using your preferred software and install packag
dependencies which are listed in the `requirements.txt` file.

## Configure the environment variables

Rename the file .env-example to .env

These are the API keys and other mandatory keys we 
need to authenticate to both the setlist.fm API and the Spotify API.
```
SPOTIPY_CLIENT_ID = xxx
SPOTIPY_CLIENT_SECRET = xxx

SETLIST_API_KEY = xxx
```

### How to get the spotify client ID and client SECRET:

Log into `https://developer.spotify.com/dashboard/applications` with your
spotify account.

Click the green button called `CREATE AN APP`

>App name: Choose the name of your app. Can be whatever

>App description: Something descriptive

Agree to the Terms of Service

Client ID is on the left, copy that and save it to `.env`

Click `SHOW CLIENT SECRET`

Client SECRET is on the left, copy that and save it to `.env`

Now click `EDIT SETTINGS`

And add `http://127.0.0.1:8080` under `Redirect URIs`

Click add then `SAVE`

### How to get the setlist.fm API key:

Sign in or register an account on `https://www.setlist.fm`

Once signed in go here to request an API key `https://www.setlist.fm/settings/api`

After a little while you will get an API key. Paste that into `.env`
behind `SETLIST_API_KEY = `


## How to use this script

After installing the dependencies and fixing `.env` to have all necessary keys 
navigate to your folder in the terminal and run the following.

First navigate to `setlist.fm` and find a setlist you want to make into a 
spotify playlist.

You need the `setlistID` located last in the URL. It looks like this `33bc8cd5`

Next run the script:

`python main.py`

The first time this project is run, or if the API keys from spotify has expired
a web browser will open and ask you to sign in.

Once that is done it will prompt you for
- `Name of the playlist`
- `Description of the playlist`
- `setlist.fm setlistID`

Output will look like this:

```
Name of the playlist: Test Playlist
Description of the playlist: Description of a playlist
SetlistID from setlist.fm: 33bc8cd5
29-Dec-22 13:50:44 - Tracks and artist fetched from Setlist
29-Dec-22 13:50:45 - Playlist created
29-Dec-22 13:50:49 - Tracks fetched from Spotify API
29-Dec-22 13:50:49 - Tracks added from setlist to playlist!
```

Now head over to spotify and enjoy. Please make an issue or ask if something is not working.

Andreas Løfsgaard




