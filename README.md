## Similar Tracks Script (via Last.fm API)

This Python script fetches **similar songs** from the [Last.fm API](https://www.last.fm/api) based on a given track and artist.  
It encodes the query parameters, sends an HTTP request, and returns related tracks in clean JSON format — making it easy to integrate with other apps.

###  Features
- Input: Track name + Artist name
- Fetches similar tracks using Last.fm’s `track.getsimilar` method
- Returns results in **clean JSON format** for easy parsing
- Handles API errors gracefully

<img width="1218" height="104" alt="Image" src="https://github.com/user-attachments/assets/4a3fc083-10d0-41b6-b350-0a6449bac3b8" />

### Usage
Run the script with a track and artist as arguments:

```bash
python similar_tracks.py "Shape of You" "Ed Sheeran"
