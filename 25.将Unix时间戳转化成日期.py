"""
unix时间戳                                            日期格式字符串

1620747224 ---------------------------------------> 2021-05-11 23:33:44
来自日志文件,MySQL数据库字段

"""
import datetime

unix_time = 1620747647

datetime_object = datetime.datetime.fromtimestamp(unix_time)

datetime_str = datetime_object.strftime('%Y-%m-%d %H:%M:%S')

print(datetime_str)  # 2021-05-11 23:40:47

























