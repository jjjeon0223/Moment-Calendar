import sys
import re
import arrow
import collections
from konlpy.tag import Mecab
from translate import *
from make_true_event import *
import json
# default for date is today, duration default is all-day, default time is pm

mecab = Mecab()

total = len(sys.argv)
cmdargs = str(sys.argv)
cm = sys.argv[1]
cm = cm.replace('.', '월')
cm = cm.replace('-', '부터')

ret = mecab.morphs(u''+cm)


grammar = ["사이", "동안", "부터", "에서", "까지", "후", "뒤"]
date = ["모레", "월", "일", "오늘", "내일", "다음주", "다음달", "월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일", "다음날"]
time = ["시", "분", "오후", "오전", "pm", "am", "시간", '아침']
rep = ["매일", "매주", "매달"]
event = []
data = dict()
delete = []
translation = [["에서", '-'], ["한", "1"], ["두", "2"], ["세", "3"], ["네", "4"], ["다섯", "5"], ["여섯", "6"], ["일곱", "7"], ["여덟", "8"], ["아홉", "9"], ["열", "10"], ["열한", "11"], ["열두", "12"]]

for i in range(len(ret)):
    if ret[i].isdigit() == True:
        if ret[i-1] == '월':
            if ret[i-3] == '부터':
                if ret[i+1] != '일':
                    ret.insert(i+1, '일')
                    if ret[i+1] != '까지':
                        ret.insert(i+2,'까지')
                if ret[i+1] == '일' and '부터' in ret[:i+1]:
                    if ret[i+2] != '까지':
                        ret.insert(i+2, '까지')
            if ret[i+1] == '부터':
                ret.insert(i+1, '일')
    # if ret[i] == '일' and '부터' in ret[:i]:
    #     if ret[i+1] != "까지":
    #         ret.insert(i+1, '까지')         

    


# print(ret)
for i in range(len(ret)):
    for j in range(len(translation)):
        if translation[j][0] == ret[i]:
            ret[i] = translation[j][1]



flag = ""
for i in range(len(ret)):
    if ret[i] in delete:
        continue
    if ret[i] == "내" and ret[i+1] =='이' and ret[i+2] == 'ㄹ':
        ret[i] = '내일'
        delete.append(ret[i+1])
        delete.append(ret[i+2])
    elif ret[i].isdigit() == True and i != len(ret) -1:
        if ret[i+1] == ':':  #4:30과 같은 시간 기록
            ret[i] += ret[i+1] + ret[i+2]
            delete.append(ret[i+1])
            delete.append(ret[i+2])
        elif ret[i+1] == ".":
            ret[i] += ret[i+1] + ret[i+2]
            delete.append(ret[i+1])
            delete.append(ret[i+2])
            if ret[i+3] == "일":
                delete.append(ret[i+3])
            elif ret[i+3] == "-":
                k = i +3
                while ret[k] == '.' or ret[k].isdigit() or ret[k] == '-':
                    ret[i] += ret[k]
                    delete.append(ret[k])
                    k += 1
                if ret[k] == "일":
                    delete.append(ret[k])
        elif ret[i+1] == "-": #4:00 - 5:00 혹은 5월17일-19일 입력
            flag = "-"
            ret[i] += ret[i +1] + ret[i+2]
            delete.append(ret[i+1])
            delete.append(ret[i+2])
            if ret[i+3] == "일": #5월17-19일
                ret[i] += "일"
                delete.append(ret[i+3])
            elif ret[i-1] == "월": #5월17-19 휴가
                ret[i] += "일"
            elif ret[i+3] == '시':
                ret[i] += '시'
                delete.append(ret[i+3])
            else:
                ret[i] += '시'
        elif ret[i+1] == "시간": #한 시간 동안 ...
            if ret[i+2] == "동안":
                ret[i] += ret[i+1] + ret[i+2]
                delete.append(ret[i+1])
                delete.append(ret[i+2])
            else:
                ret[i] += ret[i+1]
                delete.append(ret[i+1]) 
        elif ret[i+1] == "분": #30분 동안 ...
            if ret[i+2] == "동안":
                ret[i] += ret[i+1] + ret[i+2]
                delete.append(ret[i+1])
                delete.append(ret[i+2])
            else:
                ret[i] += ret[i+1]
                delete.append(ret[i+1])
        elif ret[i+2] == "부터" and ret[i+1] in ret[i+2:]: #0일부터 0일까지 | 0일부터 0일 | 0일부터 0 (몇일 혹은 몇시)
            ret[i] += ret[i + 1] + ret[i + 2]
            delete.append(ret[i+1])
            delete.append(ret[i+2])
            if ret[i + 3].isdigit():
                ret[i] += ret[i+3]
                delete.append(ret[i+3])
                if ret[i+4] == "일" or ret[i+4] == "시":
                    ret[i] += ret[i+4]
                    delete.append(ret[i+4])
            if "까지" in ret:
                k = i + 3
                while ret[k] != "까지":
                    ret[i] += ret[k]
                    delete.append(ret[k])
                    k += 1
        elif "까지" in ret:
            delete.append('까지')
            k = i + 1
            while ret[k] != "까지":
                ret[i] += ret[k]
                delete.append(ret[k])
                k += 1
        elif flag != "-": #5월 12일 5시 30분 기록
            if ret[i+1] == "월" or ret[i+1] == "일" or ret[i+1] == "시" or ret[i+1] == "분":
                if ret[i+2] == "-":
                    ret[i] += ret[i+1] + ret[i+2] + ret[i+3]
                    delete.append(ret[i+1])
                    delete.append(ret[i+2])
                    delete.append(ret[i+3])
                    if ret[i+4] == "일" or ret[i+4] == "시":
                        ret[i] += ret[i+4]
                        delete.append(ret[i+4])
                else:
                    ret[i] += ret[i+1]
                    delete.append(ret[i+1])
    
    elif ret[i] == "다음": #다음주 ~
        ret[i] += ret[i+1]
        delete.append(ret[i+1])
    # print(ret)

    
# print(ret)

    
for item in ret:
    if item in grammar:
        delete.append(item)

for deletion in delete:
    if deletion in ret:
        ret.remove(deletion)
    else:
        continue

# print(ret)

for i in range(len(ret)):
    if ret[i] == '-':
        ret[i] = ret[i-1] + '-' + ret[i+1]
        delete.append(ret[i-1])
        delete.append(ret[i+1])

for deletion in delete:
    if deletion in ret:
        ret.remove(deletion)
    else:
        continue 


for i in range(len(ret)):
    if ret[i] in rep:
        data["rep"] = ret[i]
    elif ret[i] in date or ret[i].rfind('일') != -1 or ret[i].rfind('월') != -1 or ret[i].find(".") != -1:
        if ret[i] not in rep:
            if "date" not in data:
                data["date"] = [ret[i]]
            else:
                data["date"].append(ret[i])
    elif ret[i] in time or ret[i].rfind('시') != -1 or ret[i].rfind('분') != -1 or ret[i].find(':') != -1 or ret[i].find("시간") != -1:
        if "time" not in data:
            data["time"] = [ret[i]]
        else:
            data["time"].append(ret[i])
    else:
        if "event" not in data:
            data["event"] = [ret[i]]
        else:
            data["event"].append(ret[i])

#translate.py
data["date"] = date_to_en(data)
data["time"] = time_to_en(data)
data["rep"] = rep_to_en(data)
data["event"] = event_to_en(data)
# print(data["time"])
#make_true_event.py
data["date"] = true_date(data)
data["time"] = true_time(data)
# print(data["time"])

data = collections.OrderedDict(sorted(data.items()))

json_object = json.dumps(data)   
print(json_object)  
# print(data)
sys.stdout.flush()