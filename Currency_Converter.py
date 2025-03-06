import requests
import json





def currency_converter(c_f,c_t,am):

    
   url = f"https://Currency-Conversion.proxy-production.allthingsdev.co/currency-conversion?amount={am}&currencyFrom={c_f}&currencyTo={c_t}"

   payload = {}
   headers = {
      'x-apihub-key': 'EZdhFZGbdR6NHRk3PBtfVuM8ww883Uy1FKeOCUnMr1ZUO9mFX1',
      'x-apihub-host': 'Currency-Conversion.allthingsdev.co',
      'x-apihub-endpoint': '680f0a7a-13fe-4409-9077-849146ce975d'
   }

   response = requests.request("GET", url, headers=headers, data=payload)

   data = json.loads(response.text)

   print(data['convert']['currencyTo'])





def run():

   cur_from = input('Enter your local currency : ')
   cur_to = input('Enter the currency you want to convert : ')
   amount = int(input('Insert Your Amount : '))

   while(True):
      currency_converter(cur_from,cur_to,amount)
      presser = input('Type exit to Exit,Or else Continue.')
      if 'exit' in presser:
         break
      else:
         continue



run()
