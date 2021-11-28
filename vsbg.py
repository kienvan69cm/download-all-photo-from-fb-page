import requests
import json
uid = "474237566014673"
access_token = "EAABsbCS1iHgBADE8dfz32w0SHbVQ2mGub5MaJZCR71I8gTgK7UkAsZA9q4vxZCwk8zDfqFKAYANnyBbyB1ZCNTuFheH8hkwhkifT2wAiI6g2IUrewAzRSIM2eZBBFGdBlFAx4SPxYPyim3h2dBFyIawZB2oPD79QecFjZBUpU8ITwZDZD"
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
