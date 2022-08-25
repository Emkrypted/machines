from sql import DataBase
import requests
import json
import logging

logging.basicConfig(filename='log/Log.txt', level=logging.DEBUG, format='%(asctime)s -  %(levelname)s -  %(message)s')

db = DataBase()

stored_tickets = db.select_all('stored_tickets')

for row in stored_tickets: 
    data_settings = db.select('settings')

    if row["cash_gross_amount"] != 0:
        total = row["cash_gross_amount"]
        subtotal = round(row["cash_gross_amount"]/data_settings['tax_value'])
        tax = total - subtotal
    else:
        total = row["card_gross_amount"]
        subtotal = round(row["card_gross_amount"]/data_settings['tax_value'])
        tax = total - subtotal

    data = {
            'branch_office_id': row["branch_office_id"],
            'cashier_id': row["cashier_id"],
            'folio': row["folio"],
            'dte_code': row["dte_code"],
            'cash_amount': row["cash_gross_amount"],
            'card_amount': row["card_gross_amount"],
            'subtotal': subtotal,
            'tax': tax,
            'total': total,
            'ticket_serial_number': row["ticket_serial_number"],
            'ticket_hour': row["ticket_hour"],
            'ticket_transaction_number': row["ticket_transaction_number"],
            'ticket_dispenser_number': row["ticket_dispenser_number"],
            'ticket_station_number': row["ticket_station_number"],
            'ticket_sa': row["ticket_sa"],
            'ticket_correlative': row["ticket_correlative"],
            'entrance_hour': row["entrance_hour"],
            'exit_hour': row["exit_hour"],
            'item_quantity': row["item_quantity"],
            'created_at': row["date"],
           } 

    url = "https://jisparking.com/api/api_transaction/store2?api_token=AtWYamNvDOfgDOEY6UbXgvGqDiRPR7QOt9Si1hbeMmat4g2Qfxzg7LlT5yzNz5LOozQbcA9uibaSTu4t"
    response = requests.post(url, data)
    logging.info('*****************Desde Biller')
    logging.info('La respuesta de la API es: '+ response.text)
    status_id = json.loads(response.text)
    logging.info('*****************Desde Biller')
    logging.info('La respuesta tiene estatus es: '+ str(status_id))
    if status_id == 1:
        fields = "branch_office_id, cashier_id, dte_code, folio, cash_gross_amount, cash_net_amount, card_gross_amount, card_net_amount, ticket_serial_number, ticket_hour, ticket_transaction_number, ticket_dispenser_number, ticket_number, ticket_station_number, ticket_sa, ticket_correlative, entrance_hour, exit_hour, item_quantity, sii_status, date"

        values = ""+ str(row['branch_office_id']) +", "+ str(row['cashier_id']) + ", '"+ str(row['dte_code']) +"', '"+ str(row['folio']) +"', "+ str(row['cash_gross_amount']) +", "+ str(row['cash_net_amount']) +", 0, 0, '"+ str(row['ticket_serial_number']) +"', '"+ str(row['ticket_hour']) +"', '"+ str(row['ticket_transaction_number']) +"', '"+ str(row['ticket_dispenser_number']) +"', '"+ str(row['ticket_number']) +"', '"+ str(row['ticket_station_number']) +"', '"+ str(row['ticket_sa']) +"', '"+ str(row['ticket_correlative']) +"', '"+ str(row['entrance_hour']) +"', '"+ str(row['exit_hour']) +"', '1', '"+ '0' +"', '"+ str(row['date']) +"'"
        
        status_insert_id = db.insert('processed_tickets', fields, values)

        move_tickets = db.delete('stored_tickets', 'folio', row["folio"])
        
        logging.info('*****************Desde Biller')
        logging.info('El estatus del ingresar : '+ str(status_insert_id))
        if status_insert_id == 1:
            db.delete("stored_tickets", "folio", row['folio'])
