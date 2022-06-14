import json
import pandas as pd
data = []
url = "https://cdn-dop-uat.hdbank.com.vn"
class MyClass(object):
    def __init__(self, title,link,author,img):
        self.title = title
        self.link = link
        self.author = author
        self.img = img

with open("input.txt", 'r') as f:
    data = [[x for x in line.strip().split(" ") if x] for line in f]

exceptData = [{"title": s[3].split("/").pop(), "link": s[3], "author": s[1], "img": url + "/" + s[3]} for s in data]
print(json.dumps(exceptData))
# pd.DataFrame(data).to_csv("file.csv")

# d = [
#   {
#     "title": "Vue.js",
#     "link": "https://vuejs.org/",
#     "author": "Chris",
#     "img": "https://vuejs.org//images/logo.png"
#   },
#   {
#     "title": "React.js",
#     "link": "https://facebook.github.io/react/",
#     "author": "Tim",
#     "img": "https://daynin.github.io/clojurescript-presentation/img/react-logo.png"
#   },
#   {
#     "title": "Vue.js",
#     "link": "https://vuejs.org/",
#     "author": "Chris",
#     "img": "https://vuejs.org//images/logo.png"
#   },
#   {
#     "title": "Vue.js",
#     "link": "https://vuejs.org/",
#     "author": "Chris",
#     "img": "https://vuejs.org//images/logo.png"
#   }
# ]

# html = open("dist/index.html", "r")
# text = html.read().format(data=my_objects)
# print(text)
