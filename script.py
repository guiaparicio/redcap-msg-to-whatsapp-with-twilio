import os
import requests

os.system('pip install twilio')

from twilio.rest import Client

# CONFIGS
counter             = 0
twilio_account_sid  = "99sd9wi29u12738ahxnc7d737362588"
twilio_auth_token   = "0938i3o9d88383829299iudyatz72655"
twilio_number_from  = "+88888888888"
redcap_api_url      = "https://your-redcap/api/"
redcap_api_token    = "9999999999999999999999999999999"
generate_survey_url = True
survey_url          = "N/A"
msg                 = "Your message!"

fields = {
    "token": redcap_api_token,
    "content": "record",
    "format": "json",
    "type": "flat",
    "filterLogic": "[send_message] = 1"
}

r = requests.post(redcap_api_url,data=fields)

if(r.status_code == 200):

    for record in r.json():

        if(generate_survey_url == True):

            fields_survey = {
                "token": redcap_api_token,
                "content": "surveyLink",
                "format": "json",
                "instrument": "instrument_name",
                "event": "",
                "record": record['record_id'],
                "returnFormat": "json"
            }

            survey_url_r = requests.post(redcap_api_url,data=fields_survey)

            if(survey_url_r.status_code == 200):
                survey_url = survey_url_r.text

        print("\n")
        print(record['record_id'])
        print(record['name'])
        print(record['phone_number'])
        print(msg + " | Survey: " + survey_url)

        client = Client(twilio_account_sid, twilio_auth_token)

        message = client.messages \
            .create(
                from_='whatsapp:' + twilio_number_from,
                body=msg,
                to='whatsapp:' + record['phone_number']
            )

        print(message.sid)

        counter += 1

    print("\nTotal Records: " + str(counter))