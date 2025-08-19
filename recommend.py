import requests
import sys
from urllib.parse import quote_plus
import json

API_KEY = "a6c014def6c2f9675e7dd4ed5ddbcc30"

def get_similar_tracks(track_name, artist_name):
    """Fetch similar songs from Last.fm API"""
    encoded_track = quote_plus(track_name)
    encoded_artist = quote_plus(artist_name)

    url = (
        f"https://ws.audioscrobbler.com/2.0/"
        f"?method=track.getsimilar&track={encoded_track}&artist={encoded_artist}"
        f"&api_key={API_KEY}&format=json"
    )

    try:
        response = requests.get(url)
        response.raise_for_status()
        json_data = response.json()

        if "similartracks" in json_data and "track" in json_data["similartracks"]:
            similar_tracks = json_data["similartracks"]["track"]
            return [f"{track['name']} - {track['artist']['name']}" for track in similar_tracks[:10]]
        else:
            return ["No similar tracks found."]
    except Exception as e:
        return [f"Error: {str(e)}"]

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(json.dumps(["Error: Please provide a track and artist."]))
    else:
        track = sys.argv[1].strip()
        artist = sys.argv[2].strip()
        result = get_similar_tracks(track, artist)
        print(json.dumps(result)) 
