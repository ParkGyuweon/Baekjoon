from collections import defaultdict
from heapq import heappush, heappop

def solution(genres, plays):
    answer = []
    song_dict = defaultdict(int)
    genre_dict = defaultdict(list)
    
    for i in range(len(genres)):
        genre_dict[genres[i]].append([plays[i], i])    
        song_dict[genres[i]] += plays[i]
        
    many_song_genre = sorted(song_dict.items(), key=lambda x:x[1], reverse=True)
    for genre in many_song_genre:
        songs = sorted(genre_dict[genre[0]], key=lambda x:x[0], reverse=True)
        if len(songs) > 2:
            for song in songs[0:2]:
                answer.append(song[1])
        else:
            for song in songs:
                answer.append(song[1])
            
    return answer