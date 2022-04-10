def findTheCity(n, edges, distanceThreshold):
    """
    :type n: int
    :type edges: List[List[int]]
    :type distanceThreshold: int
    :rtype: int
    """
    di = [[99999999] * n for _ in range(n)]
    for i in range(n):
        di[i][i] = 0
    for i in range(len(edges)):
        di[edges[i][0]][edges[i][1]] = min(edges[i][2], di[edges[i][0]][edges[i][1]])
        di[edges[i][1]][edges[i][0]] = min(edges[i][2], di[edges[i][1]][edges[i][0]])
        for j in range(n):
            di[edges[i][0]][j] = min(di[edges[i][0]][j],di[edges[i][1]][j] + di[edges[i][0]][edges[i][1]])
            di[j][edges[i][0]] = di[edges[i][0]][j]
            di[edges[i][1]][j] = min(di[edges[i][1]][j],di[edges[i][0]][j] + di[edges[i][0]][edges[i][1]])
            di[j][edges[i][1]] = di[edges[i][1]][j]

    Min = n + 1;
    ans = -1;
    for i in range(n):
        nu = 0
        for j in range(n):
            if di[i][j] <= distanceThreshold:
                nu += 1
        if nu <= Min:
            Min = nu
            ans = i
    return ans

edges = [[3,11,4805],[18,25,5356],[24,31,5072],[7,8,761],[26,31,1578],[17,25,6132],[14,19,4714],[16,27,749],[23,31,7991],[13,28,1141],[8,15,7788],[15,27,7699],[11,15,3994],[6,16,2923],[12,17,5337],[13,17,4309],[16,30,5427],[11,22,2570],[7,10,8096],[0,22,1173],[32,33,8437],[4,26,9256],[12,32,7990],[7,19,5549],[15,34,2936],[8,11,1737],[2,29,6543],[2,28,703],[11,26,3639],[8,30,823],[18,24,7404],[13,30,2725],[31,34,8963],[14,31,9430],[14,35,8316],[1,28,885],[3,10,4079],[26,35,684],[5,15,9727],[7,15,8216],[0,19,5920],[29,34,995],[3,28,5815],[12,13,9030],[8,14,2084],[25,35,3690],[18,28,3808],[8,28,4932],[12,25,6920],[0,30,814],[19,21,5332],[32,35,2074],[3,21,8193],[11,18,1899],[15,30,3687],[3,26,8351],[4,32,3949],[22,30,9372],[0,10,1144],[9,19,5644],[15,18,2414],[0,26,3637],[7,9,4348],[2,11,8321],[13,33,8005],[6,8,8527],[4,12,9952],[11,27,9558],[8,25,4681],[10,33,26],[3,14,2125],[1,8,5518],[18,22,7275],[3,5,6792],[20,28,9916],[10,19,5445],[12,21,1768],[6,12,2509],[10,15,3388],[7,26,8447],[28,29,6053],[23,33,9374],[4,28,2598],[6,24,7353],[3,15,7570],[6,31,5973],[5,26,6860],[17,26,1625],[6,11,7232],[22,34,7138],[23,25,4427],[27,34,9876],[3,6,8417],[7,25,661],[11,25,127],[4,24,5779],[14,20,6155],[4,22,1619],[9,30,3195],[24,27,5710],[8,31,3038],[2,32,690],[0,25,1673],[9,10,9328],[15,24,263],[4,33,8703],[7,35,7791],[25,34,309],[19,35,8891],[26,32,3694],[9,18,7462],[0,9,2723],[9,32,4418],[5,9,6301],[24,33,1584],[5,23,1590],[8,17,801],[9,28,9699],[4,16,1936],[13,26,9167],[26,34,5172],[17,20,3941],[5,27,8238],[30,34,3579],[13,22,7534],[22,24,7675],[2,24,2442],[14,18,5488],[12,19,887],[13,14,7075],[11,19,1815],[6,34,3591],[12,15,1673],[6,33,5178],[19,29,2065],[0,33,6321],[2,18,7884],[20,25,648],[2,15,4560],[1,4,1258],[7,27,3611],[3,35,1629],[3,34,4833],[12,24,2937],[13,35,1080],[20,29,543],[14,32,8531],[9,14,896],[11,28,3258],[30,31,5662],[4,19,1117],[18,26,9503],[20,24,7144],[14,23,9072],[26,27,8765],[15,31,7486],[17,33,3753],[1,15,9590],[13,32,1035],[5,12,476],[11,20,5115],[2,5,553],[6,20,4289],[2,27,1306],[25,32,3762],[31,33,7393],[27,32,5710],[9,24,4677],[19,30,9397],[2,30,4909],[30,35,4386],[13,16,9536],[3,25,7911],[0,14,9525],[21,23,8544],[2,7,9735],[5,14,4590],[6,10,8531],[0,15,1349],[11,13,5685],[14,29,5232],[4,17,6447],[15,23,1050],[11,24,9641],[19,31,193],[1,31,2925],[22,28,565],[17,18,1277],[2,25,2184],[1,25,6429],[22,27,7339],[16,34,5538],[17,22,3614],[12,22,1683],[22,32,3731],[7,13,2352],[25,30,9468],[20,21,730],[32,34,5465],[6,29,3743],[17,27,6447],[6,22,1898],[6,19,7115],[13,18,5254],[7,14,937],[9,11,4221],[11,31,8568],[9,22,1870],[0,12,3200],[11,32,2529],[20,30,618],[7,33,6606],[0,4,4125],[10,28,6887],[1,11,9858],[1,19,2617],[1,2,9215],[1,13,2092],[17,19,4383],[0,16,9347],[12,34,312],[16,26,8492],[28,33,5840],[2,22,5948],[34,35,1191],[10,30,7416]]
print(findTheCity(36,edges,2978))