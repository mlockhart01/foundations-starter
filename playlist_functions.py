def show_song(song_name, song_length):
    print ("Song:", song_name)
    print ("Length:", song_length, "minutes")
    
show_song("Just Dance", 4)
show_song("Saturn", 3)
show_song("From the Start", 3)

def total_playlist_length (song1, song2, song3):
    total = song1 + song2 + song3
    return total

playlist_total = total_playlist_length (4, 3, 3)
print ("Total playlist length:", playlist_total, "minutes")