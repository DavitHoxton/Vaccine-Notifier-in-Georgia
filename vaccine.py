import requests
from playsound import playsound
import time
import json

headers = {
    'authority': 'booking.moh.gov.ge',
    'accept': 'application/json, text/plain, */*',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Mobile Safari/537.36',
    'authorization': 'Bearer null^@null',
    'securitynumber': '26279972450',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://booking.moh.gov.ge/Hmis/Hmis.Queue.Web/',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': '_ga=GA1.1.1687795598.1620645474; _ga_MPX1GWT6K2=GS1.1.1620645474.1.1.1620650285.0',
}

params = (
    ('serviceId', 'd1eef49b-00b9-4760-9525-6100c168e642'),
    ('onlyFree', 'true'),
)


i = 0
run = 0

while run == 0:
    response = requests.get('https://booking.moh.gov.ge/Hmis/Hmis.Queue.API/api/CommonData/GetMunicipalities/5d129a50-30e9-4b10-8d4d-3febb32ec32c', headers=headers, params=params)
    try:
        if response.json()!=[]:  
            ## PUT YOUR ALARM SOUND HERE      
            playsound('https://www.zapsplat.com/wp-content/uploads/2015/sound-effects-pmsfx/PM_BlurryDreams_144_253.mp3')  
            i+=1          
            print ('Free Slot - Attempt #' + str(i))                
            time.sleep(6)
        else:
            i+=1
            time.sleep(2)
            print ('All slots are full ! - Attempt #' + str(i))
    except:        
        i+=1
        print ('Server is busy ! - Attempt #' + str(i))
        time.sleep(5)
        continue