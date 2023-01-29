# Data modeling using dictionary & list

playlist = {
    "title": "Patagonia Bus",
    "author": "Colt Steele",
    "songs": [
        {
            "title": "song1",
            "artist": ["Blue the cat"],
            "duration": 2.5,
        },
        {
            "title": "song2",
            "artist": ["Kitty", "DJ Kat"],
            "duration": 5.25,
        },
        {
            "title": "meow-meow",
            "artist": ["Garfield"],
            "duration": 2.0,
        }
    ]
}

print(f"Playlist content: {playlist}")

# Iterate through the duration of each song, total the sum & print it
total_length = 0
for song in playlist["songs"]:
    total_length += song["duration"]

print(f"Total duration: {total_length} minutes")
