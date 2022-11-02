from datetime import datetime, date

#print (datetime.strptime("12/31/2000", "%m/%d/%Y"))
#print( datetime.today())
#print(date.today())

#print(datetime.now())


#today_raw = str( date.today() )
#today = int(today_raw[-2:])
#print(today)

"""
#given string
string1="Романов, 9"


#confirming the type()
print("Type of string: ",type(string1))

#type-casting the string into list using list()
print("String coverted to list :\n",list(string1))
"""
"""
from datetime import datetime

date_time_str = '19/07/22 10:00:00'
				#'18/09/19 01:55:19' 2022-07-19


date_time_obj = datetime.strptime(date_time_str, '%d/%m/%y %H:%M:%S')


print ("The type of the date is now",  type(date_time_obj))
print ("The date is", date_time_obj)
"""
import datetime
from datetime import datetime


time_from_html = '09.00'
today = str(date.today())
sep_data = today.split(sep='-')
cache_today = sep_data[2]+'.'+sep_data[1]+'.'+sep_data[0]+' '+time_from_html
print(cache_today)
print(type(cache_today))

import calendar
import datetime
now = datetime.datetime.now()
print (calendar.monthrange(now.year, now.month)[1])

