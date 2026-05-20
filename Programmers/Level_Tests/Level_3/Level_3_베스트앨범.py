from collections import defaultdict
def solution(genres, plays):
    answer = []
    hash_map = defaultdict(list)
    g_total_p = defaultdict(int)

    for i in range(len(genres)):
        hash_map[genres[i]].append(i)
        g_total_p[genres[i]] += plays[i]

    sorted_genre = sorted(g_total_p.items(),key=lambda x:x[1],reverse=True)
    

    for genre, _ in sorted_genre:
        songs = sorted(hash_map[genre],key=lambda x:plays[x],reverse=True)

        answer.extend(songs[:2])

    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"],[500, 600, 150, 800, 2500]))