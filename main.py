from datetime import datetime

#Set Arrays
times = ['08:00', '09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00'] 
#index 0 = 08:00, 1 = 09:00 etc
booked = [False, False, False, False, False, False, False, False, False, False]
name = ['', '', '', '', '', '', '', '', '', '']
mobile = ['', '', '', '', '', '', '', '', '', '']
code = ['', '', '', '', '', '', '', '', '', '']

# Create array of above arrays. courts[0] = Court #1, [1] = #2 etc
courts = []
for i in range(0,8):
  courts.append([booked, name, mobile, code])
# print(courts[7][0][0])
booking = {
  "time":"",
  "booked":"",
  "name":"",
  "mobile":"",
  "code":""
}
# print(booking)

#Get date, day, time
# date = datetime.now()
# TESTING: Set the date to Monday 9th May 2020 08:05:23
date = datetime(2022, 5, 9, 8,5,23)
#Split time data
dayTime = {
  "day": date.strftime("%A"),   #Get full day as string
  "dayNum": date.strftime("%w"), #Get day as number
  "hour": date.strftime("%H"),
  "minute": date.strftime("%M")
}


print("""*** WELCOME TO BSM HOLIDAY PARK ***
 --- SQUASH COURT BOOKING SYSTEM ---
      """)
print(f"Today is {dayTime['day']} {date.day} {date.strftime('%B')} {date.year}")
print(f"The time is {dayTime['hour']}:{dayTime['minute']}")

availMsg = (f"""The following times are available:\n"""
f"""Opt  | Time    |  #Courts """)
print(availMsg)
print("-"*30)
for i in range(0, len(times)):
  if booked[i] == False:
    a = i+1
    print(f"{a if a == 10 else '0'+str(a)}   | {times[i]}   | num")

