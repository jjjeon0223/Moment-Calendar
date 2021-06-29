def date_to_en(data_dict):
    update = []
    if "date" in data_dict:
        for i in range(len(data_dict["date"])):
            if data_dict["date"][i].rfind("월") != -1 and data_dict["date"][i][0].isdigit() and data_dict["date"][i].find("부터") == -1:
                if len(data_dict["date"][i]) == 2:
                    update.append(["0" + data_dict["date"][i][:-1], "MM"]) 
                else:
                    update.append([data_dict["date"][i][:-1], "MM"])
                continue
            elif data_dict["date"][i] == "내일" or data_dict["date"][i] == "다음날":
                update.append([1, 'day'])
                continue
            elif data_dict["date"][i].rfind("일") != -1 and data_dict["date"][i][0].isdigit() and data_dict["date"][i].rfind("-") == -1 and data_dict["date"][i].rfind("부터") == -1:
                if len(data_dict["date"][i]) == 2:
                    update.append(["0" + data_dict["date"][i][:-1], "DD"])
                else:
                    update.append([data_dict["date"][i][:-1], "DD"])
                continue
            elif data_dict["date"][i].find("-") != -1 and data_dict["date"][i][0].isdigit(): #5.17 - 5.19도 해야함...
                if len(data_dict["date"][i]) == 4:
                    update.append(["0" + data_dict["date"][i][:2] + "0" + data_dict["date"][i][2:-1], "Range"])
                elif len(data_dict["date"][i]) == 5:
                    if data_dict["date"][i][1] == "-":
                        update.append(["0" + data_dict["date"][i][:-1], "Range"])
                    if data_dict["date"][i][2] == "-":
                        update.append([data_dict["date"][i][:3] + "0" + data_dict["date"][i][-2], "Range"])
                elif len(data_dict["date"][i]) == 6:
                    update.append([data_dict["date"][i][:-1], "Range"])
                elif len(data_dict["date"][i]) == 7:
                    if "." in data_dict["date"][i]:
                        update.append([data_dict["date"][i].replace('.', 'M'), "Range"])
                    else:
                        update.append([data_dict["date"][i][:2] + data_dict["date"][i][3:-1], "Range"])
                elif "." in data_dict["date"][i]:
                    update.append([data_dict["date"][i].replace('.', 'M'), "Range"])
                continue
            elif data_dict["date"][i].find("부터") != -1:
                temp = data_dict["date"][i].replace('부터','').replace('까지','').replace('일', '-').replace("월", 'M')
                if temp[-1] == '-':
                    temp = temp[:-1]
                update.append([temp, "Range"])
            elif data_dict["date"][i].find('.') != -1:
                update.append([data_dict["date"][i][:data_dict["date"][i].find('.')], "MM"]) 
                update.append([data_dict["date"][i][data_dict["date"][i].find('.') + 1:], "DD"]) 
            elif data_dict["date"][i] == "오늘":
                update.append("today")
                continue
            elif data_dict["date"][i] == "모레":
                update.append([2, 'day'])
                continue
            elif data_dict["date"][i] == "다음주":
                update.append([1, 'week'])
                continue
            elif data_dict["date"][i] == "다음달":
                update.append([1, 'month'])
                continue
            elif data_dict["date"][i] == "월요일":
                update.append("monday")
                continue
            elif data_dict["date"][i] == "화요일":
                update.append("tuesday")
                continue
            elif data_dict["date"][i] == "수요일":
                update.append("wednsday")
                continue
            elif data_dict["date"][i] == "목요일":
                update.append("thursday")
                continue
            elif data_dict["date"][i] == "금요일":
                update.append("friday")
                continue
            elif data_dict["date"][i] == "토요일":
                update.append("saturday")
                continue
            elif data_dict["date"][i] == "일요일":
                update.append("sunday")
                continue

    else:
        update.append("today")
    return update

def time_to_en(data_dict):
    update = []
    delete = []
    if "time" in data_dict:
        for i in range(len(data_dict["time"])):
            if data_dict["time"][i].rfind("시") != -1 and data_dict["time"][i].rfind("시간") == -1 and data_dict["time"][i].find("부터") == -1 and data_dict["time"][i].find("-") == -1:
                if len(data_dict["time"][i]) == 2:
                    update.append("0" + data_dict["time"][i][:-1] + ":00") 
                else:
                    update.append(data_dict["time"][i][:-1] + ":00")
                continue
            elif data_dict["time"][i].find("부터") != -1 or data_dict["time"][i].find("-") != -1:
                temp = data_dict["time"][i].replace('부터','').replace('까지','')
                if '-' in data_dict["time"][i]:
                    temp = temp.replace('시', '')
                else:
                    temp = temp.replace('시', '-')
                if temp[-1] == '-':
                    temp = temp[:-1]
                update.append([temp, "Range"])
            elif data_dict["time"][i].rfind("분") != -1 and data_dict["time"][i].rfind("동안") == -1:
                if len(data_dict["time"][i]) == 2:
                    new_min = "0" + data_dict["time"][i][:-1]
                    for item in update:
                        if item.rfind(":00") != -1:
                            delete.append(item)
                            item = item[:-2]
                            item += new_min
                            update.append(item)
                else:
                    for item in update:
                        if item.rfind(":00") != -1:
                            delete.append(item)
                            item = item[:-2]
                            item += data_dict["time"][i][:-1]
                            update.append(item)
                continue
            elif data_dict["time"][i].rfind(":") != -1:
                if len(data_dict["time"][i]) == 4:
                    update.append("0" + data_dict["time"][i])
                else:
                    update.append(data_dict["time"][i])
                continue
            elif data_dict["time"][i] == "오후" or data_dict["time"][i] == "낮" or data_dict["time"][i] == "저녁":
                update.append("pm") 
                continue
            elif data_dict["time"][i] == "pm":
                update.append("pm") 
                continue
            elif data_dict["time"][i] == "am" or data_dict["time"][i] == "새벽" or data_dict["time"][i] == "오전" or data_dict["time"][i] == "아침":
                update.append("am") 
                continue
            elif data_dict["time"][i].find("동안") != -1:
                if data_dict["time"][i].find("시간") != -1:
                    update.append([int(data_dict["time"][i][:data_dict["time"][i].find("시")]), "duration", "hour"])
                else:
                    update.append([int(data_dict["time"][i][:data_dict["time"][i].find("분")]), "duration", "minute"])
                continue
    for deletion in delete:
        update.remove(deletion)
    # print(update)
    # print(data_dict["time"])
    default_time = ["오후", "오전", "pm", "am", '아침']
    default = 0
    if "time" in data_dict:
        for item in update:
            if item in default_time:
                default = 1
        if default == 0:
            update.append("pm")
    return update

def rep_to_en(data_dict):
    update = "None"
    if "rep" in data_dict:
        if data_dict["rep"] == "매일":
            update = "everyday"
        elif data_dict["rep"] == "매주":
            update = "everyweek"
        elif data_dict["rep"] == "매일":
            update = "everymonth"
    return update

def event_to_en(data_dict):
    update = " ".join(data_dict["event"])
    return update