def solution(wallpaper):
    n, m = len(wallpaper), len(wallpaper[0])
    minr, minc, maxr, maxc = n, m, 0, 0
    for i in range(n):
        for j in range(m):
            if wallpaper[i][j] == "#":
                minr = min(minr, i)
                minc = min(minc, j)
                maxr = max(maxr, i+1)
                maxc = max(maxc, j+1)
                
    return [minr, minc, maxr, maxc]
