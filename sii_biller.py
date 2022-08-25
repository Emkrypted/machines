from sql import DataBase
import requests
import subprocess
import json
import logging
logging.basicConfig(filename='log/siiBillerLog.txt', level=logging.DEBUG, format='%(asctime)s -  %(levelname)s -  %(message)s')

db = DataBase()

processed_tickets = db.select_all('processed_tickets', 'sii_status', '0')

for row in processed_tickets:
    data_settings = db.select('settings')

    url = 'https://libredte.cl'
    hash = 'JXou3uyrc7sNnP2ewOCX38tWZ6BTm4D1'

    data_folio = db.select('folios', 'folio', row["folio"])

    url = "https://apigateway.cl/api/v1/libredte/dte/documentos/generar?normalizar=1&formato=json&enviar_sii=0&gzip=0&retry=1"

    cert_data = data_settings["cert_data"]
    cert_data = cert_data.replace("\\n", "\n")

    pkey_data = data_settings["pkey_data"]
    pkey_data = pkey_data.replace("\\n", "\n")

    mydict = {
    "auth": {
        "cert": {
        "cert-data": str(cert_data),
        "pkey-data": str(pkey_data)
        }
    },
    "dte": {
        "Encabezado": {
        "IdDoc": {
            "TipoDTE": 39,
            "Folio": str(row["folio"])
        },
        "Emisor": {
            "RUTEmisor": str(data_settings["rut"]),
            "RznSoc": str(data_settings["CAFRS"]),
            "GiroEmis": str(data_settings["GiroEmis"]),
            "Acteco": str(data_settings["Acteco"]),
            "DirOrigen": str(data_settings["DirOrigen"]),
            "CmnaOrigen": str(data_settings["CmnaOrigen"])
        },
        "Receptor": {
            "RUTRecep": "66666666-6",
            "RznSocRecep": "Cliente Generico",
            "GiroRecep": "Particular",
            "DirRecep": "Santiago",
            "CmnaRecep": "Estacion Central"
        }
        },
        "Detalle": {
        "NmbItem": "Venta",
        "QtyItem": 1,
        "PrcItem": row["cash_gross_amount"]
        }
    },
    "resolucion": {
        "fecha": str(data_settings["resolution_date"]),
        "numero": str(data_settings["resolution_number"])
    },
    "caf": str(data_folio["caf"])
    }

    headers = {
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiYWIyYWUwOGVmYjI1Y2MwMWU5ODUzOWViMDRhNjJkYzEzN2UxMDQyODRmNjY5MTNjMTAxMWM3Yzg1N2Q0NmZmNzY1NGM4NGQzYzM0YzRhMTAiLCJpYXQiOjE2NDk1Mjg4ODMsIm5iZiI6MTY0OTUyODg4MywiZXhwIjo0ODA1MjAyNDgzLCJzdWIiOiI1NzYiLCJzY29wZXMiOltdfQ.K03TeHk5geCY4NARl9UiV8SeeR6Pe4YT1E_Z_z5VLhTJwI36_780NiwxlBIE58hlX9XdjBZiVgpW3FSEYvGQo-6pv6tp9r6Yh9LB6Hi1j5YirwWQgOgPE_2kXBjtXVS84r97unEhpCGA0mGpbIJH0YNNFLYgZauoLzGjmooOYbAT6buhOG5_xTX25VhgscoaPeh_-KnbJVxpMf0YxMkDC7nE5VsI8mMloR3pOyfXpLUH5f3yjl2F8QNPtjRB25MJZnhetMozPUoDX8h5Lh5gcbYItQYtzZrU-3Cs8JMG7bu3fH74a5bej_HmLfdAP-3HP0CxOOhAY4Oppamf8zGwkvzPSeXZdPW79pZ9JEkfRFOfwuYbJA79-nawo_UiKc73HIHgGMFoR9wvfla5JDKrzTh3xoa2JsZUbMZ93iYqsurVMJt-suaqM1Lqcqa1nGZ8HovGgYeVf6RbQH1TJT-ckeGwgfor0Pi_vhhUc9Coxd9qQOAyiY_jHUVy16CQ4BlFkgsOQ9mwBuL5k4xHwNd3VBa_ktLeW36rrXSsaGXwoVLO9Bi19_-fijvrNRmAez3NTiODrMLNNLqXIk9MbUy0PWYAV1Ylq_gdJhJXEED0_iTe6MwA_OrAwVN18U0DQopKwIDLqQoRTAPlcWR1PEO5sBs3jHFclc_BaoHqfG5_W2U',
    'Content-Type': 'application/json'
    }

    stud_json = json.dumps(mydict)
    response = requests.request("POST", url, headers=headers, data=stud_json)
    xml = response.text
    y = json.loads(xml)
    xml_sii = y['xml']['sii']
    logging.info('*****************Desde Sii Biller')
    logging.info(xml_sii)
    url = "https://apigateway.cl/api/v1/libredte/dte/envios/enviar?certificacion=1&gzip=0&retry=1"

    mydict = {
        "auth": {
            "cert": {
            "cert-data": str(cert_data),
            "pkey-data": str(pkey_data)
            }
        },
        "emisor": str(data_settings["rut"]),
        "xml": str(xml_sii)
    }

    headers = {
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiYWIyYWUwOGVmYjI1Y2MwMWU5ODUzOWViMDRhNjJkYzEzN2UxMDQyODRmNjY5MTNjMTAxMWM3Yzg1N2Q0NmZmNzY1NGM4NGQzYzM0YzRhMTAiLCJpYXQiOjE2NDk1Mjg4ODMsIm5iZiI6MTY0OTUyODg4MywiZXhwIjo0ODA1MjAyNDgzLCJzdWIiOiI1NzYiLCJzY29wZXMiOltdfQ.K03TeHk5geCY4NARl9UiV8SeeR6Pe4YT1E_Z_z5VLhTJwI36_780NiwxlBIE58hlX9XdjBZiVgpW3FSEYvGQo-6pv6tp9r6Yh9LB6Hi1j5YirwWQgOgPE_2kXBjtXVS84r97unEhpCGA0mGpbIJH0YNNFLYgZauoLzGjmooOYbAT6buhOG5_xTX25VhgscoaPeh_-KnbJVxpMf0YxMkDC7nE5VsI8mMloR3pOyfXpLUH5f3yjl2F8QNPtjRB25MJZnhetMozPUoDX8h5Lh5gcbYItQYtzZrU-3Cs8JMG7bu3fH74a5bej_HmLfdAP-3HP0CxOOhAY4Oppamf8zGwkvzPSeXZdPW79pZ9JEkfRFOfwuYbJA79-nawo_UiKc73HIHgGMFoR9wvfla5JDKrzTh3xoa2JsZUbMZ93iYqsurVMJt-suaqM1Lqcqa1nGZ8HovGgYeVf6RbQH1TJT-ckeGwgfor0Pi_vhhUc9Coxd9qQOAyiY_jHUVy16CQ4BlFkgsOQ9mwBuL5k4xHwNd3VBa_ktLeW36rrXSsaGXwoVLO9Bi19_-fijvrNRmAez3NTiODrMLNNLqXIk9MbUy0PWYAV1Ylq_gdJhJXEED0_iTe6MwA_OrAwVN18U0DQopKwIDLqQoRTAPlcWR1PEO5sBs3jHFclc_BaoHqfG5_W2U',
    'Content-Type': 'application/json'
    }

    stud_json = json.dumps(mydict)
    response = requests.request("POST", url, headers=headers, data=stud_json)
    y  = json.loads(response.text)

    # the result is a Python dictionary:
    track_id = y["track_id"]
    status_sii = y["estado"]
    if status_sii == "REC":
        data = {
            'folio': row["folio"]
           } 

        url = "https://jisparking.com/api/folio/sii?api_token=AtWYamNvDOfgDOEY6UbXgvGqDiRPR7QOt9Si1hbeMmat4g2Qfxzg7LlT5yzNz5LOozQbcA9uibaSTu4t"
        response = requests.post(url, data)
        if response.text == '1':
            db.update('processed_tickets', 'sii_status', response.text, 'folio', row["folio"])

subprocess.call([r'C:\boleta_v1\bd\database.bat'], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)