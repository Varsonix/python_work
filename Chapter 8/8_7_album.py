def make_album(artist_name, album_title, song_count=None):
    if song_count:
        album = {
            'artist': artist_name,
            'album_name': album_title,
            'song_count': song_count,
        }
    else:
        album = {'artist': artist_name, 'album_name': album_title}
    return album


while True:
    print("Enter some information about the album: ")
    print("enter 'q' at any time to quit")

    a_name = input("Artist Name: ")
    if a_name == 'q':
        break

    album_name = input("Album Name: ")
    if album_name == 'q':
        break

    print(make_album(a_name, album_name))