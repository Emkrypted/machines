#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Nuestro Servidor Software sobre el Servidor Físico
import socketserver
from sql import DataBase
from datetime import date
import logging
logging.basicConfig(filename='log/Log.txt', level=logging.DEBUG, format='%(asctime)s -  %(levelname)s -  %(message)s')

# Dirección IP
HOST = "127.0.0.1"

# El puerto privado que queramos escuchar, uno de los comprendidos entre 49152 y 65535  1-65535
PORT = 5502


class Server(socketserver.BaseRequestHandler):
    """
    La clase que controlará las peticiones para nuestro servidor.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        """
        Método sobrescrito para controlar la comunicación que ocurra ne nuestro servidor.
        Aquí recibiremos los mensajes del cliente y le responderemos
        """
        print('[Servidor 3] Cliente conectado desde: {}'.format(self.client_address[0]))
        logging.info('*****************Desde Server')
        logging.info('[Servidor 3] Cliente conectado desde: {}'.format(self.client_address[0]))

        socket_abierto = True
        while socket_abierto:
            print('[Servidor 4] Esperando por petición del cliente...')
            logging.info('*****************Desde Server')
            logging.info('[Servidor 4] Esperando por petición del cliente...')
            dato_recibido_en_bytes = self.request.recv(1024).strip()
            print(dato_recibido_en_bytes)
            logging.info('*****************Desde Server')
            logging.info(dato_recibido_en_bytes)
            if dato_recibido_en_bytes:
                dato_recibido_en_str = dato_recibido_en_bytes.decode("utf-8") 

                if "@**@1" in dato_recibido_en_str:
                    print('[Servidor 5] Recibido desde el cliente: {}'.format(dato_recibido_en_str))
                    logging.info('*****************Desde Server')
                    logging.info('[Servidor 5] Recibido desde el cliente: {}'.format(dato_recibido_en_str))

                    #respuesta_en_str = "0 OK".format(dato_recibido_en_str)
                
                    respuesta_en_str = chr(2) + "0" + chr(9) + "OK" + chr(3) .format(dato_recibido_en_str)
                
                    self.request.sendall(bytes(respuesta_en_str, encoding='utf8'))
                    print('[Servidor 6] Se ha respondido al cliente con el mensaje: {}'.format(respuesta_en_str))
                    logging.info('*****************Desde Server')
                    logging.info('[Servidor 6] Se ha respondido al cliente con el mensaje: {}'.format(respuesta_en_str))
                if "@**@2" in dato_recibido_en_str:
                    db = DataBase()

                    print(dato_recibido_en_str)
                    logging.info('*****************Desde Server')
                    logging.info(dato_recibido_en_str)
                    split_data = dato_recibido_en_str.split('|');
                    print(split_data)
                    logging.info('*****************Desde Server')
                    logging.info(split_data)
                    data_folios = db.select('folios', 'used_id', '0')
                    update_folios = db.update('folios', 'used_id', '1', 'folio', data_folios['folio'])
                    today = date.today()
                    computer_date = today.strftime("%Y/%m/%d")
                    time = today.strftime("%H:%M:%S")
                    folio = data_folios['folio']
                    superior_range = data_folios['superior_range']
                    inferior_range = data_folios['inferior_range']
                    caf_date = data_folios['date']
                    rsapk_m = data_folios['rsapk_m']
                    rsapk_e = data_folios['rsapk_e']
                    idk = data_folios['idk']
                    frma = data_folios['frma']

                    data_settings = db.select('settings')
                    branch_office_id = data_settings['branch_office_id']
                    cashier_id = data_settings['cashier_id']
                    dte_code = data_settings['dte_code']
                    rut = data_settings['rut']
                    print(split_data[137])
                    logging.info('*****************Desde Server')
                    logging.info(split_data[138])
                    cash_amount = split_data[138]
                    cash_net_amount = round((float(cash_amount)/1.19))

                    """ 
                        amount_split = split_data[145].split(" ")
                        amount_split = amount_split[10]

                        if amount_split == 0:}
                            cash_amount = 0
                            cash_net_amount = 0
                            card_amount = split_data[137]
                            card_net_amount = round((float(cash_amount)/1.19))
                        else:
                            card_amount = 0
                            card_net_amount = 0
                            cash_amount = split_data[137]
                            cash_net_amount = round((float(cash_amount)/1.19))
                    """ 

                    #Se guarda los datos de la boleta en la tabla local processed_tickets.

                    describe_fields = db.describe('electronic_ticket_system', 'stored_tickets', 'COLUMN_NAME')
                    length = len(describe_fields)
                    fields = ""

                    entrance_hour_exit_hour = split_data[130].split(' ')
                    print(entrance_hour_exit_hour)
                    entrance_hour = entrance_hour_exit_hour[6].split('@')
                    print(entrance_hour)
                    exit_hour = entrance_hour_exit_hour[12].split('@')
                    print(exit_hour)

                    ticket_serial_number = split_data[156]
                    ticket_hour = split_data[155]
                    ticket_transaction_number = ''
                    ticket_dispenser_number = ''
                    ticket_number = ''
                    ticket_station_number = ''
                    ticket_sa = ''
                    ticket_correlative = ''
                    entrance_hour = entrance_hour[0]
                    exit_hour = exit_hour[0]
                    sii_status = ''
                    rcof_status = ''
                    ticket_date = today.strftime("%Y-%m-%d")

                    fields = "branch_office_id, cashier_id, dte_code, folio, cash_gross_amount, cash_net_amount, card_gross_amount, card_net_amount, ticket_serial_number, ticket_hour, ticket_transaction_number, ticket_dispenser_number, ticket_number, ticket_station_number, ticket_sa, ticket_correlative, entrance_hour, exit_hour, item_quantity, sii_status, date"

                    values = ""+ str(branch_office_id) +", "+ str(cashier_id) + ", '"+ str(dte_code) +"', '"+ str(folio) +"', "+ str(cash_amount) +", "+ str(cash_net_amount) +", 0, 0, '"+ str(ticket_serial_number) +"', '"+ str(ticket_hour) +"', '"+ str(ticket_transaction_number) +"', '"+ str(ticket_dispenser_number) +"', '"+ str(ticket_number) +"', '"+ str(ticket_station_number) +"', '"+ str(ticket_sa) +"', '"+ str(ticket_correlative) +"', '"+ str(entrance_hour) +"', '"+ str(exit_hour) +"', '1', '"+ str(sii_status) +"', '"+ str(ticket_date) +"'"
                    db.insert('stored_tickets', fields, values)

                    #Se crea el TED para mostrar en la boleta.

                    ted = '<TED version="1.0"><DD><RE>' + str(rut) + '</RE><TD>39</TD><F>'+ str(folio) +'</F><FE>' + str(computer_date) + '</FE><RR>66666666-6</RR><RSR>N/A</RSR><MNT>'+ str(cash_amount) + '</MNT><IT1>PRESTACION DE ESTACIONAMIENTO.</IT1><CAF version="1.0"><DA><RE>'+ str(rut) +'</RE><RS>J I S PARKING SPA</RS><TD>39</TD><RNG><D>' + str(superior_range) + '</D><H>' + str(inferior_range) + '</H></RNG><FA>'+ str(caf_date) + ' 0:00:00 </FA><RSAPK><M>'+ str(rsapk_m) +'</M><E>'+ str(rsapk_e) +'</E></RSAPK><IDK>'+ str(idk) +'</IDK></DA><FRMA algoritmo="SHA1withRSA">' + str(frma) + '</FRMA></CAF><TSTED>'+ str(computer_date) +'T'+ str(time) +'</TSTED></DD><FRMT algoritmo="SHA1withRSA">lNK147l1YdQTlofH/bDrxBnOX9TPdT1JoORnvvP5o9CxoKw96jmFfX4Cc9d2MQQszy7gOFXaDNo16BqZ0vd0QQ==</FRMT></TED>'

                    respuesta_en_str = chr(2)  + '0' + chr(9)  + 'OK' + chr(9) + str(folio) + chr(9) + str(ted) + chr(3)

                    self.request.sendall(bytes(respuesta_en_str, encoding='utf8'))
                    print('[Servidor 6.1] Se ha respondido al cliente con el mensaje: {}'.format(respuesta_en_str))
                if "@**@3" in dato_recibido_en_str:
                    respuesta_en_str = chr(2) + "0" + chr(9) + "OK" + chr(3) .format(dato_recibido_en_str)
                
                    self.request.sendall(bytes(respuesta_en_str, encoding='utf8'))
                    print('[Servidor 6.2] Se ha respondido al cliente con el mensaje: {}'.format(respuesta_en_str))
                    logging.info('*****************Desde Server')
                    logging.info('[Servidor 6.2] Se ha respondido al cliente con el mensaje: {}'.format(respuesta_en_str))
            else:
                print('[Servidor 7] El cliente ha cerrado el Socket desde su lado, cerrando socket desde el Servidor...')
                logging.info('[Servidor 7] El cliente ha cerrado el Socket desde su lado, cerrando socket desde el Servidor...')
                socket_abierto = False


if __name__ == "__main__":
    tupla_para_el_enlace = (HOST, PORT)

    try:
        print('[Servidor 1] Enlazando Socket en: {}'.format(tupla_para_el_enlace))
        with socketserver.TCPServer(tupla_para_el_enlace, Server) as servidor:
            print('[Servidor 2] Iniciando bucle del servidor. Para interrumpir pulsar a la vez las teclas: [Ctrl]+[C]')
            logging.info('*****************Desde Server')
            logging.info('[Servidor 2] Iniciando bucle del servidor. Para interrumpir pulsar a la vez las teclas: [Ctrl]+[C]')
            servidor.serve_forever()
    except KeyboardInterrupt:
        print('[Servidor 8] Interrupción por teclado')
        logging.info('*****************Desde Server')
        logging.info('[Servidor 8] Interrupción por teclado')
    finally:        
        if servidor is not None:
            servidor.shutdown()
        print('[Servidor 9] Servidor Cerrado')
        logging.info('*****************Desde Server')
        logging.info('[Servidor 9] Servidor Cerrado')
