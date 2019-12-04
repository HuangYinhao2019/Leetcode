def suggestedProducts(products, searchWord):
    """
    :type products: List[str]
    :type searchWord: str
    :rtype: List[List[str]]
    """
    pro = []
    ans = []
    for i in range(len(searchWord)):
        for j in range(len(products)):
            if products[j].startswith(searchWord[:i+1]):
                pro.append(products[j])
        pro = sorted(pro)
        products = pro.copy()
        ans.append(pro[:3])
        pro = []
    return ans

products = ["havana"]
searchWord = "tatiana"
print(suggestedProducts(products,searchWord))
