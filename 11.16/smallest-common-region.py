def findSmallestRegion(regions, region1, region2):
    """
    :type regions: List[List[str]]
    :type region1: str
    :type region2: str
    :rtype: str
    """
    di = dict()
    for i in range(len(regions)):
        for j in range(1, len(regions[i])):
            di[regions[i][j]] = regions[i][0]

    re1, re2 = [], []
    re1.append(region1)
    re2.append(region2)
    t1, t2 = region1, region2
    while t1 in di:
        re1.append(di[t1])
        t1 = di[t1]
    while t2 in di:
        re2.append(di[t2])
        t2 = di[t2]
    k = -1
    while k+len(re1) >= 0 and k+len(re2) >= 0 and re1[k] == re2[k]:
        k -= 1
    return re1[k+1]

regions = [["Earth","North America","South America"],
           ["North America","United States","Canada"],
           ["United States","New York","Boston"],
           ["Canada","Ontario","Quebec"],
           ["South America","Brazil"]]
region1,region2 = "Canada","Quebec"
print(findSmallestRegion(regions,region1,region2))