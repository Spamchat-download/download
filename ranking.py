from deta import Deta

deta = Deta("a0nx7pgk_CAsXSD5UjJsWT8xj9nPSAb14xduJ1fUR")
chats = deta.Base("spamchat")
res = chats.fetch()
all_items = res.items
all_items.sort(key=lambda x: x["spamscore"])
for item in all_items:
    h = "The User \"" + item["key"] + "\" has the highest Spamscore with " + item["spamscore"] + "."
print(h)
datei = open("old/Readme.md", "r")
inn = datei.read()
datei.close()
datei = open("Readme.md", "w")
datei.write(inn + h)
datei.close()
