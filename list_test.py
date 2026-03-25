# 🎯 Your task: Build a simple music player (using lists)

# Start very small. Don’t overcomplicate.

# 🔹 Core features (Phase 1)

# You must implement:

# Add a song
# Show playlist
# Play next song (remove from front)

def create_playlist():
    playlist = []
    return playlist

def enter_songs(playlist):
    while True:
        song = input("Enter the songs you want to listen to. Type 'stop' to stop adding songs to the queue:")
        if song == "stop":
            break
        playlist.append(song)
        if song.strip() == "":
            playlist.pop()
        if not playlist:
            print("Playlist cannot be empty. Enter atleast one song.")
            continue
    return playlist

def play_song(playlist):
    print(f"Now playing: {playlist.pop(0)}")
    
def show_playlist(playlist):
    for song in playlist:
        print(song)

# def skip_song(playlist):
#     for song in playlist:
#         if song:
#             continue
#     print(f"Song skipped. Now playing{song}")