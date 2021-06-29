import arrow
from datetime import datetime, timedelta
current = arrow.now('Asia/Seoul')
weekday = current.weekday()
def true_date(data):
    current = arrow.now('Asia/Seoul')
    start = arrow.get(current - timedelta(days=current.weekday()))
    end = arrow.get(current.shift(weekday=6))

    for item in data["date"]:
        if isinstance(item, str):
            if item == "today":
                continue
            elif item == "monday":
                current = current.shift(weekday=0)
            elif item == "tuesday":
                current = current.shift(weekday=1)
            elif item == "wednsday":
                current = current.shift(weekday=2)
            elif item == "thursday":
                current = current.shift(weekday=3)
            elif item == "friday":
                current = current.shift(weekday=4)
            elif item == "saturday":
                current = current.shift(weekday=5)
            elif item == "sunday":
                current = current.shift(weekday=6)
        else:
            if item[1] == "day":
                if arrow.get(current).is_between(start, end, '[]'):
                    current = current.shift(days=+int(item[0]))
            elif item[1] == "week":
                if arrow.get(current).is_between(start, end, '[]'):
                    current = current.shift(weeks=+int(item[0]))
                    current = arrow.get(current - timedelta(days=current.weekday()))
            elif item[1] == "month":
                if arrow.get(current).is_between(start, end, '[]'):
                    current = current.shift(months=+int(item[0]))
                    current = arrow.get(current - timedelta(days=current.weekday()))
            elif item[1] == "MM":
                   current = current.replace(month=int(item[0]))
            elif item[1] == "DD":
                    current = current.replace(day=int(item[0]))
            elif item[1] == "Range":
                check = 0
                if isinstance(item[0][:2], int) and isinstance(item[0][3:], int):
                    if int(item[0][:2]) >= int(item[0][3:]):
                        check = 1

                flag = 0
                for it in data["date"]:
                    if isinstance(item, list) and it[1] == "MM":
                        flag = it[0]
                if flag != 0:
                    current_s = current.replace(month=int(flag), day = int(item[0][:2])).format('YYYY-MM-DD')
                    if check == 1:
                        current_e = current.replace(month=int(flag)+1, day = int(item[0][3:])).format('YYYY-MM-DD')
                    else:
                        current_e = current.replace(month=int(flag), day = int(item[0][3:])).format('YYYY-MM-DD')
                elif "M" in item[0]:
                    start, end = map(str, item[0].split('-'))
                    s = current.replace(month = int(start[:start.find('M')]), day = int(start[start.find('M')+1:]))
                    e = current.replace(month = int(end[:end.rfind('M')]), day = int(end[end.rfind('M')+1:]))
                    current = s.format('YYYY-MM-DD') + ' to ' + e.format('YYYY-MM-DD')
                    continue
                else:
                    current_s = current.replace(day = int(item[0][:2])).format('YYYY-MM-DD')
                    if check == 1:
                        current_e = current.shift(months =+ 1)
                        current_e = current_e.replace(day = int(item[0][3:])).format('YYYY-MM-DD')
                    else:
                        current_e = current.replace(day = int(item[0][3:])).format('YYYY-MM-DD')
                current = current_s + " to " + current_e
    if isinstance(current, str):
        return current
    else:
        return current.strftime('%d-%m-%Y')

def true_time(data):
    current = arrow.now('Asia/Seoul')
    no_time = '00:00 to 24:00'
    time = ""
    temp = current
    flag = 0
    set_hour = 0
    if "pm" in data["time"]:
        flag = 1
    for item in data["time"]:
        if isinstance(item, str):
            if item.rfind(":") != -1:
                h = int(item[:2])
                m = int(item[3:])
                if flag == 1:
                    if h < 12:
                        h += 12
                current = current.replace(hour = h, minute = m)
                time = current.strftime('%H:%M') + " to " + current.shift(hours =+ 1).strftime('%H:%M')
                set_hour = 1
        else:
            if item[1] == "duration":
                if set_hour == 1:
                    if item[2] == "hour":
                        time = current.strftime('%H:%M') + ' to ' + current.shift(hours =+ item[0]).strftime('%H:%M')
                    elif item[2] == "minute":
                        time = current.strftime('%H:%M') + ' to ' + current.shift(minutes =+ item[0]).strftime('%H:%M')
                if set_hour != 1:
                    time = current.replace(hour = 12, minute = 0).strftime('%H:%M') + ' to ' + current.replace(hour = 12, minute = 0).shift(hours =+ item[0]).strftime('%H:%M')
                    current = arrow.now()
                    continue
            elif item[1] == "Range":
                if ":" not in item[0][:item[0].find("-") - 1]:
                    if flag == 1:
                        start = current.replace(hour = int(item[0][:item[0].find("-")]) + 12, minute = 00)
                    else:
                        start = current.replace(hour = int(item[0][:item[0].find("-")]), minute = 00) 
                # elif item[0].find   #동안
                else:
                    if flag == 1:
                        start = current.replace(hour = int(item[0][:item[0].find(":")]) + 12, minute = int(item[0][item[0].find(":")+1:item[0].find("-")])) 
                    else:
                        start = current.replace(hour = int(item[0][:item[0].find(":")]), minute = int(item[0][item[0].find(":")+1:item[0].find("-")]))
                if ":" not in item[0][item[0].find("-") + 1:]:
                    if flag == 1:
                        end = current.replace(hour = int(item[0][item[0].find("-") + 1:]) + 12, minute = 00)
                    else:
                        end = current.replace(hour = int(item[0][item[0].find("-") + 1:]), minute = 00)
                else:
                    if flag == 1:
                        end = current.replace(hour = int(item[0][item[0].find("-") + 1:item[0].find(":", item[0].find("-"))]) + 12, minute = int(item[0][item[0].find(":", item[0].find("-")) + 1:]))
                    else:
                        end = current.replace(hour = int(item[0][item[0].find("-") + 1:item[0].find(":", item[0].find("-"))]), minute = int(item[0][item[0].find(":", item[0].find("-")) + 1:]))
                time = start.strftime('%H:%M') + ' to ' + end.strftime('%H:%M')
                current = 9999
    if temp == current:
        if "pm" in data["time"]:
            return '12:00 to 13:00'
        else:
            return no_time
    return time