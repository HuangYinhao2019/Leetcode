import collections

##并查集
def generateSentences(synonyms,text):

    words = collections.defaultdict(set)
    for a, b in synonyms:
        st = words[a] | words[b] | {a, b}
        for i in st:
            words[i] = st.copy()
            words[i].discard(i)

    text = list(text.split())
    res = [text]
    for i, w in enumerate(text):
        n = len(res)
        for word in words[w]:
            for j in range(n):
                lst = res[j].copy()
                lst[i] = word
                res.append(lst)

    ##join:连接字符串序列
    ##sorted:排序
    return sorted((' '.join(i) for i in res))

synonyms = [["happy","joy"],["sad","sorrow"],["joy","cheerful"]]
text = "I am happy today but was sad yesterday"

print(generateSentences(synonyms,text))