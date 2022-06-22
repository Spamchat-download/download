from deta import Deta

deta = Deta("a0nx7pgk_CAsXSD5UjJsWT8xj9nPSAb14xduJ1fUR")
chats = deta.Base("spamchat")
res = chats.fetch()
all_items = res.items
#print(all_items)
#print("-------------")
all_items.sort(key=lambda x: x["spamscore"])
for item in all_items:
    h = "Der User \"" + item["key"] + "\" hat den höchsten Spamscore mit " + item["spamscore"] + "."
print(h)
datei = open("old/Readme.md", "r")
in = datei.read()
datei.close()
datei = open("Readme.md", "a")
in = datei.write(h)
datei.close()
