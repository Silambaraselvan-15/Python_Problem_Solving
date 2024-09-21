song="JINGLE Bells jingle Bells Jingle All The Way"
a=song.upper()
print(a)
song_words=song.split()
print(song_words)
count=0
for word in song_words:
    if(word.startswith("jingle")):
        count=count+1
print(count)