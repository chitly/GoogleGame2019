from urllib.request import urlopen
import json
rootUrl = "https://techchallenge.withgoogle.com/midrule/"
urlList = ['https://techchallenge.withgoogle.com/midrule/start']
url_idx = 0
url_len = 1
visited = set()
tf = []
while url_idx < url_len:
    url = urlList[url_idx]
    response = urlopen(url)
    data = json.loads(response.read())
    print(data)
    print(urlList[url_idx:])
    for k in data:
        if k == 'TETRAFORCE':
            tf.append(data[k])
        elif data[k] not in visited:
            urlList.append(rootUrl + data[k])
            visited.add(data[k])
    url_idx += 1
    url_len = len(urlList)
print(tf)