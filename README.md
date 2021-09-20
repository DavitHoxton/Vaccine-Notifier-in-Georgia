# [OUTDATED] Vaccine Notifier in Georgia
A small Python script, designed to be ran in background and notify you, once there's an available slot for the Sinnopharm Vaccine Appointment in the capital - Tbilisi.

How to use:
- Install Python3
- Open the script with Powershell or any Python Editor (python ../Yourdirectory/vaccine.py) and keep it running on the background

Editting the alarm sound:
- You can easily edit the alarm sound effect at Line #34 

Editting the city:
- On default, the script is set on Tbilisi. 
- You can change this by going to the official website (https://booking.moh.gov.ge/Hmis/Hmis.Queue.Web/#/register) >> Right Click >> Inspect >> Network.
- Now select the city and Copy the correct request's cURL. (Screenshot: http://prntscr.com/12s0chn)
- Convert the cURL to Python at https://curl.trillworks.com/
- Replace the params (at line #20) and response.get (at line #30) from the converted Python code and you should be good to go !

#StopTheVirus
