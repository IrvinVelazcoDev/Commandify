import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
from cred import logo
import t
try:
    load_dotenv()
except Exception as e:
    print("Failed to load environment variables:", e)

scope = ("user-read-email "
         "user-library-read "
         "user-modify-playback-state "
         "user-read-playback-state")

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=os.getenv('SPOTIPY_CLIENT_ID'),
        client_secret=os.getenv('SPOTIPY_SECRET_ID'),
        redirect_uri=os.getenv('SPOTIPY_REDIRECT_URI'),
        scope=scope
    )
)
def queue_request():
    try:
        user_search = input('Welcome to Spotify, So whats on your mind?: ')

        search = sp.search(q=user_search, limit=10)
        tracks = search['tracks']['items']

        for idx, track in enumerate(tracks, start=1):
            print(f"{idx}: {track['name']} (Album: {track['album']['name']})")

        song_choice = input("What song number would you like to choose? ")

        try:
            choice_num  = int(song_choice) - 1
            if 0 <= choice_num < len(tracks):
                print(f"Adding {tracks[choice_num]['name']} to queue")
                sp.add_to_queue(tracks[choice_num]['uri'])
            else:
                print("Number out of range. Please run the program again and pick a valid number.")
        except ValueError:
            print("Invalid input: Please enter a number.")

    except Exception as e:
        print("Error:", e)


def next_song():
    sp.next_track()

def previous_song():
    sp.previous_track()

def pause_song():
    sp.pause_playback()

def resume_song():
    sp.start_playback()



def menu():
    while True:
        print("1.Queue a song")
        print("2.Skip to next song")
        print("3.Previous song")
        print("4.Pause song")
        print("5.Resume song")
        operation = input("What we doing now?: ")
        if operation == '1':
            queue_request()

        elif operation == '2':
            next_song()

        elif operation == '3':
            previous_song()

        elif operation == '4':
            pause_song()

        elif operation == "5":
            resume_song()





if __name__ == '__main__':
    try:
        logo()
        menu()
    except Exception as e:
        print("Error:", e)





