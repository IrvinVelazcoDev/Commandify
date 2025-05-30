import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
from cred import logo

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

def current_song():

    current_tracks = sp.current_user_playing_track()
    current_track = current_tracks['item']
    print (current_track['name'])


def manipulate_song(operation_1):
    if operation_1 == '1':
        next_song()
    elif operation_1 == '2':
        previous_song()
    elif operation_1 == '3':
        pause_song()
    elif operation_1 == '4':
        resume_song()
    elif operation_1 == '5':
        current_song()
    elif operation_1 == '6':
        return


def menu():
    while True:
        print("1.Manipulate song")
        print("2.Queue song")
        print("3.Just view song")
        operation = input("What we doing now?: ")
        if operation == '1':
            print("1.Skip to next song")
            print("2.Previous song")
            print("3.Pause song")
            print("4.Resume song")
            print('5.Preview')
            print('6.exit')

            operation_1 = input("So whats the haps?")
            manipulate_song(operation_1)

        elif operation == '2':
            print('Pick a song Jackass')
            queue_request()


        elif operation == '3':
            print('your a cuck')
            current_song()





if __name__ == '__main__':
    try:
        logo()
        menu()
    except Exception as e:
        print("Error:", e)





