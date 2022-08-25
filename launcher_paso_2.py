from sql import DataBase

import os

import shutil

import subprocess

db = DataBase()

#########################

subprocess.Popen("pip install -r C:\\boleta_v1\\requirements.txt", stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

#########################

sqlStatement = "C:\\boleta_v1\\dump.sql"

db.executeScriptsFromFile(sqlStatement)

#########################

f = open ('C:\\boleta_v1\\settings_ini.txt','r')
settings = f.read()

settings = settings.split('\n')
setting_0 = settings[0].split('=')
setting_1 = settings[1].split('=')
setting_2 = settings[2].split('=')
setting_3 = settings[3].split('=')
setting_4 = settings[4].split('=')

update_branch_office_id = db.update('settings', 'branch_office_id', setting_0[1], 'setting_id', 1)
update_branch_office_id = db.update('settings', 'cashier_id', setting_1[1], 'setting_id', 1)
update_branch_office_id = db.update('settings', 'dte_code', setting_2[1], 'setting_id', 1)
update_branch_office_id = db.update('settings', 'description', setting_3[1], 'setting_id', 1)
update_branch_office_id = db.update('settings', 'folio_quantity', setting_4[1], 'setting_id', 1)

#folder_name = str(setting_0[1]) + "_" + str(setting_1[1])

#os.mkdir(folder_name)

#source = "C:\\boleta_v1\\files"
#target = "C:\\boleta_v1\\" + folder_name

#utput = os.system ("""xcopy "%s" "%s" """ % (source, target))

#source = "C:\\boleta_v1\\bd"
#target = "C:\\boleta_v1\\" + folder_name +"\\bd"

#shutil.copytree(source, target)

f.close()