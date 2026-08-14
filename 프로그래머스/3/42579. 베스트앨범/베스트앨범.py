def solution(genres, plays):
    genre_total = {}        # 장르별 총 재생시간
    genre_songs = {}        # 장르별 노래

    for i, (genre, play) in enumerate(zip(genres, plays)):
        genre_total[genre] = genre_total.get(genre, 0) + play

        if genre not in genre_songs:
            genre_songs[genre] = []

        genre_songs[genre].append((i, play))

    sorted_genres = sorted(
        genre_total,
        key=lambda genre: genre_total[genre],
        reverse=True
    )

    answer = []

    for genre in sorted_genres:
        songs = genre_songs[genre]

        songs.sort(key=lambda x: (-x[1], x[0]))

        for song_id, play in songs[:2]:
            answer.append(song_id)

    return answer