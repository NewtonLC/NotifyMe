'''
OBJECTIVES:

Create a system that takes in a date, time, alarm sound, and user message.
When the date and time are met, play the sound and display the user message.

Create a system that takes in a set time, alarm sound, and a user message. Wait that many seconds, then play the sound and display the user message.

'''

#Necessary for tracking the current date, time
from datetime import datetime
import pytz    #Necessary for checking time zone

#NEcessary for setting a timer
import time
from threading import Timer

#Tracking the datetime based on LA time zone since that's the one I'm in
losAngelesTZ = pytz.timezone("America/Los_Angeles")

today = datetime.now(losAngelesTZ)
today = today.strftime("%B %d, %Y %H:%M:%S")

print("today's date:", today)
print("time zone:", losAngelesTZ)

#def Reminder():
#  Check if the datetime in the current time zone is later than the listed reminder.
#  Play a sound and display the user message

#Takes in the number of hours, minutes, and seconds, waits, then calls a function
def RemindTimer(numHours = 0, numMinutes = 0, numSeconds = 0, alarm = "None", message = "Timer"):
  # Calculate the number of seconds to wait
  # Wait that many seconds
  totalSecs = numHours * 3600 + numMinutes * 60 + numSeconds
  timer = Timer(totalSecs, timerUp, args=(alarm,message))
  timer.start()

#Helper function of RemindTimer:
#Play the alarm and display the message
def timerUp(alarm, message):
  #TODO: Play the alarm sound
  print(message)

#Testing
RemindTimer(0,0,6,"None","Waited 6 seconds!!!")
RemindTimer(0,0,3,"None","Waited 3 seconds!!!")