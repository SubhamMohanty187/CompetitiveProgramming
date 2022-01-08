ranked = sorted(list(set(ranked)),reverse = True)
    player.sort(reverse = True)
    j = 0
    l = len(ranked)
    result = []
    for i in range(len(player)):
        while j<l and player[i]<ranked[j]:
            j+=1
        result.append(j+1)
    return result[::-1]
