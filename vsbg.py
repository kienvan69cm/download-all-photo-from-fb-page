import requests
import json
uid = "474237566014673"
access_token = "EAABsbCS1iHgBAPqycePFfHlKg8Y7wWt8jtdXqLZBZBbZCpD8wvyLo1GAA8ESJKhZAoLKQ20KkGLfJU5hes7HGUXkwg6dbHZAe6prqZAQebCAkosZAbUnz2x0HeDV4DUrwShNgedvjNOypktbPPQfn27bZBMd4hMTCGTXkiIeuHllZBQZDZD'"
url = "https://graph.facebook.com/"+uid + \
    "?fields=feed.limit(670)%7Bfull_picture%7D&access_token="+access_token
data = json.loads(requests.get(url).text)
index = 0
for piture in data["feed"]["data"]:
    try:
        index += 1
        img_data = requests.get(piture["full_picture"]).content
        with open("photos/image_"+str(index)+".jpg", 'wb') as f:
            f.write(img_data)
    except KeyError:
        pass
