import spotipy
import json
import webbrowser

username = '31n744t2vmvlfwmf3zq4wk7cvusa'
clientID = 'f7102d8abc34450c9c2ac4a3f638b7e7'
clientSecret = '498b9c97d5b044808c43bc68d307245f' 
redirectURI = 'https://www.google.com/'

#creating oauth object
oauth_object = spotipy.SpotifyOAuth(clientID, clientSecret, redirectURI)
#creating token
token_dict = oauth_object.get_access_token()
token = token_dict['access_token']
#creating spotify object
spotifyObject = spotipy.Spotify(auth = token)

user = spotifyObject.current_user()
print(json.dumps(user, sort_keys = True, indent = 4))

while True:
    print("Welcome, " + user['display_name'])
    print("Press 0 to Exit at any moment")
    print("Press 1 to Search for a Song")
    choice = int(input("Your choice: "))
    if choice == 1:
        #get song name
        searchQuery = input("Enter song name: ")
        #searching for song 
        searchResults = spotifyObject.search(searchQuery, 1, 0, "track")
        #get required data from json response
        tracks_dict = searchResults['tracks']
        tracks_items = tracks_dict['items']
        song = tracks_items[0]['external_urls']['spotify']
        #opening song in web browser
        webbrowser.open(song)
        print("song has opened in your browser, dumbass")
    elif choice == 0:
        break
    else:
        print("Please don't make my job harder and play by the rules. Dumbass")