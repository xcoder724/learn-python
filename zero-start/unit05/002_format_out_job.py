print("\n* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n")
import datetime
timeStr = "2023-05-15 17:39:44"
time_obj = datetime.datetime.strptime(timeStr, "%Y-%m-%d %H:%M:%S")
result = "智能助手为你报时，当前时间是 {0} 年 {1} 月 {2} 日 {3} 点 {4} 分 {5} 秒"
print(result.format(time_obj.strftime("%Y"), 
                    time_obj.strftime("%m"),
                    time_obj.strftime("%d"),
                    time_obj.strftime("%H"),
                    time_obj.strftime("%M"),
                    time_obj.strftime("%S"),
                    time_obj.strftime("%m")))