Script for sending messages based on REDCAP records to WhatsApp with Twilio

# How to use

Change the variables in the configuration section of the file, to your Twilio and REDCap data.

```php

// ALTER TO TWILIO ACCOUNT SID
twilio_account_sid = "99sd9wi29u12738ahxnc7d737362588"

// ALTER TO TWILIO AUTH TOKEN
twilio_auth_token = "0938i3o9d88383829299iudyatz72655"

// ALTER TO TWILIO NUMBER FROM
twilio_number_from = "+88888888888"

// ALTER TO REDCAP API URL
redcap_api_url = "https://your-redcap/api/"

// ALTER TO REDCAP API TOKEN
redcap_api_token = "9999999999999999999999999999999"

// SET TRUE, IF YOU WANT TO GENERATE A SURVEY URL PER RECORD
generate_survey_url = FALSE

// SET YOUR MESSAGE
msg = "Your message!"


```
