def guitar(songs, n):
    sm = 0
    songs.sort(reverse=True)
    for i in range(0, n):
        sm = sm + ((n-i)*songs[i])

    return sm

print(guitar([23,45,12,34,23], 5))