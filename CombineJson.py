#coding:UTF-8

#listdir()
import os
import json

# 依檔案夾讀取出裡面所有資料
DATA_DIR = "E:/AB104/Ctrip/combine"
file_data = []
for filename in os.listdir(DATA_DIR):
    print "Loading: %s" % filename
    with open(os.path.join(DATA_DIR, filename), 'r')as a:
        data = json.load(a)
        print type(data)
        for i in data:
            file_data.append(i)
            # print file_data

# 寫入同一Json檔
print len(file_data)
print type(file_data)

contentjson = json.dumps(file_data, encoding="UTF-8", ensure_ascii=False)
with open("E:/AB104/Ctrip/CtripHotelName.json", "w") as w:
    w.write(contentjson.encode('utf-8'))



