import csv
import json
import pathlib
import datetime

dt_now = datetime.datetime.now()
filename = dt_now.isoformat()
p_temp = pathlib.Path('./')
list = list(p_temp.glob('**/*.json'))
emojiList = {}
for item in list:
    json_open = open(item, 'r')
    json_load = json.load(json_open)
    for load_json in json_load:
        if "reactions" in load_json:
            # print(load_json["reactions"])
            for reaction in load_json["reactions"]:
                if reaction["name"] not in emojiList:
                    emojiList[reaction["name"]] = reaction["count"]
                else:
                    emojiList[reaction["name"]] = emojiList[reaction["name"]] + reaction["count"]

emojiListRank = sorted(emojiList.items(), key=lambda x:x[1],reverse=True)

for i in range(len(emojiListRank)):
    # print(emojiListRank[i][0])
    # print(emojiListRank[i][1])
    with open('./result/' + filename + '.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(["" + emojiListRank[i][0] + ":",emojiListRank[i][1]])