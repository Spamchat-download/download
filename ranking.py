from deta import Deta

deta = Deta("a0nx7pgk_CAsXSD5UjJsWT8xj9nPSAb14xduJ1fUR")
chats = deta.Base("spamchat")
res = chats.fetch()
all_items = res.items
def sort_by_key(list):
	return int(list['spamscore'])
all_items = sorted(all_items, key=sort_by_key)
for item in all_items:
    h = "The User \"" + item["key"] + "\" has the highest Spamscore with " + item["spamscore"] + "."
print(h)
datei = open("old/User.svg", "r")
inn = datei.read()
datei.close()
datei = open("icons/User.svg.md", "w")
datei.write(inn.replace("%ghg%, h)
datei.close()
