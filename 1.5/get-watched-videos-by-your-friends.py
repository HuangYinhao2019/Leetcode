def watchedVideosByFriends(watchedVideos, friends, id, level):
    """
    :type watchedVideos: List[List[str]]
    :type friends: List[List[int]]
    :type id: int
    :type level: int
    :rtype: List[str]
    """
    t = set()
    t.add(id)
    fr = set()
    fr.add(id)
    for i in range(level):
        f = set()
        for j in fr:
            for k in range(len(friends[j])):
                if friends[j][k] not in t:
                    f.add(friends[j][k])
                    t.add(friends[j][k])
        fr = f
    d = {}
    for fri in fr:
        for v in watchedVideos[fri]:
            if v not in d:
                d[v] = 1
            else:
                d[v] += 1
    sorted_x = sorted(d.items(), key=lambda x:(x[1],x[0]))
    ans = []
    for x in sorted_x:
        ans.append(x[0])
    return ans




watchedVideos = [["bjwtssmu"],["aygr","mqls"],["vrtxa","zxqzeqy","nbpl","qnpl"],["r","otazhu","rsf"],["bvcca","ayyihidz","ljc","fiq","viu"]]
friends = [[3,2,1,4],[0,4],[4,0],[0,4],[2,3,1,0]]
id = 3
level = 1

print(watchedVideosByFriends(watchedVideos,friends,id,level))