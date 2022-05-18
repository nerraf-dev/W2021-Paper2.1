from datetime import datetime
import time

"""
Task 1 – at the start of the day
Write a program to set up arrays to record the following for each hour:
• whether a squash court is booked or available
• the name of the guest
• the mobile phone number of the guest
• the unique 4-digit code for the booking.
Set up a screen to display the court availability at the start of the day.
"""
NUM_OF_COURTS = 8
#Set Arrays
times = ['08:00', '09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00'] 
#index 0 = 08:00, 1 = 09:00 etc
booked = [False, False, False, False, False, False, False, False, False, False]
name = ['', '', '', '', '', '', '', '', '', '']
mobile = ['', '', '', '', '', '', '', '', '', '']
code = ['', '', '', '', '', '', '', '', '', '']

# Create array of above arrays. courts[0] = Court #1, [1] = #2 etc
#courts[n] = [0 - booked],[1 - name],[2 - mobile],[3 - code]
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

runBookings = True
while runBookings:
  print("""**** WELCOME TO BSM HOLIDAY PARK ****
   --- SQUASH COURT BOOKING SYSTEM ---
        """)
  print(f"Today is {dayTime['day']} {date.day} {date.strftime('%B')} {date.year}")
  print(f"The time is {dayTime['hour']}:{dayTime['minute']}\n")
  
  availMsg = (f"""The following times are available:\n\n"""
  f"""Opt  | Time    |  #Courts """)
  print(availMsg)
  print("-"*30)
  for i in range(0, len(times)):    #O/L: iterate courts
    free = 0
    for j in range(0,NUM_OF_COURTS):  #I/L: 
      if courts[j][0][i] == False:
        a = i+1
        free += 1
    print(f"{a if a == 10 else ' '+str(a)}   | {times[i]}   | {free}")
      
    # if booked[i] == False:
    #   a = i+1
    #   print(f"{a if a == 10 else ' '+str(a)}   | {times[i]}   | num")
  
  print()
  print("To make a booking enter the option number for your chosen time:")
  command = input(">> ")
  if command.upper() == "Q":
    runBookings = False
    print("*** QUITTING ***")    #Just to jazz it up a little!
    time.sleep(1)
    print("*** SHUTDOWN COMPLETE ***")
  else:
    pass    #Pass is used to help run empty loops and selection blocks