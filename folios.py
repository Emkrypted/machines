from sql import DataBase
import requests
import json
from datetime import date
import logging

today = date.today()
computer_date = today.strftime("%Y/%m/%d")
logging.basicConfig(filename='log/Log_'+ str(computer_date) +'.txt', level=logging.DEBUG, format='%(asctime)s -  %(levelname)s -  %(message)s')

db = DataBase()
data_settings = db.select('settings')
branch_office_id = data_settings['branch_office_id']
cashier_id = data_settings['cashier_id']
quantity = data_settings['folio_quantity']

headers = ''

data_count_folios = db.select_count('folios', 'used_id', 0)
how_many_quantity = quantity - data_count_folios

if data_count_folios < quantity:
    url = "https://jisparking.com/api/folio/get/"+ str(branch_office_id) +"/"+ str(cashier_id) +"/"+ str(how_many_quantity) +"?api_token=AtWYamNvDOfgDOEY6UbXgvGqDiRPR7QOt9Si1hbeMmat4g2Qfxzg7LlT5yzNz5LOozQbcA9uibaSTu4t"
    response = requests.get(url, headers)
    y  = json.loads(response.text)

    data = y["data"]
    logging.info('*****************Desde Folios')
    logging.info('la consulta a la API folio dio como respuesta: '+ str(data))
    length = len(data)

    for n in range(length):
        fields = "used_id, folio, superior_range, inferior_range, date, rsapk_m, rsapk_e, idk, frma, caf"

        values = "0, "+ str(data[n]['folio']) +", "+ str(data[n]['superior_range']) +", "+ str(data[n]['inferior_range']) +", '"+ data[n]['date'] +"', '"+ data[n]['rsapk_m'] +"', '"+ data[n]['rsapk_e'] +"', "+ str(data[n]['idk']) +", '"+ data[n]['frma'] +"', '"+ data[n]['caf'] +"'"

        db.insert('folios', fields, values)

