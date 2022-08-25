
import sys
import dropbox
import os
from datetime import date
import subprocess

from dropbox.files import WriteMode
from dropbox.exceptions import ApiError, AuthError

# Access token
TOKEN = 'wBwpv76XAJAAAAAAAADk5yOnKPEEq1U4HeFsStaRshe3zdzRksdMYdWpg7b-SKII'

# Uploads contents of LOCALFILE to Dropbox
def backup(localfile, backup_data):
    with open(localfile, 'rb') as f:
        # We use WriteMode=overwrite to make sure that the settings in the file
        # are changed on upload
        print("Uploading " + localfile + " to Dropbox as " + backup_data + "...")
        try:
            dbx.files_upload(f.read(), backup_data, mode=WriteMode('overwrite'))
        except ApiError as err:
            # This checks for the specific error where a user doesn't have enough Dropbox space quota to upload this file
            if (err.error.is_path() and
                    err.error.get_path().error.is_insufficient_space()):
                sys.exit("ERROR: Cannot back up; insufficient space.")
            elif err.user_message_text:
                print(err.user_message_text)
                sys.exit()
            else:
                print(err)
                sys.exit()


# Adding few functions to check file details
def checkFileDetails():
    print("Checking file details")

    for entry in dbx.files_list_folder('').entries:
        print("File list is : ")
        print(entry.name)


# Run this script independently
if __name__ == '__main__':
    today = date.today()
    folder_name = "C:\\boleta_v1\\bd\\" + today.strftime("%Y-%m-%d")

    os.mkdir(folder_name)

    f = open ('C:\\boleta_v1\\settings_ini.txt','r')
    settings = f.read()

    settings = settings.split('\n')
    setting_0 = settings[0].split('=')
    setting_1 = settings[1].split('=')

    key = str(setting_0[1]) + "_" + str(setting_1[1])

    subprocess.Popen('"C:\\Program Files\\MySQL\\MySQL Server 8.0\\bin\\mysqldump.exe" -uroot -pJis2022. electronic_ticket_system > C:\\boleta_v1\\bd\\'+ today.strftime("%Y-%m-%d") + "\\"+ str(key) + "_" + today.strftime("%Y-%m-%d") +".sql", shell=True)
    
    f.close()

    # Check for an access token
    if (len(TOKEN) == 0):
        sys.exit("ERROR: Looks like you didn't add your access token. Open up backup-and-restore-example.py in a text editor and paste in your token in line 14.")

    # Create an instance of a Dropbox class, which can make requests to the API.
    print("Creating a Dropbox object...")
    dbx = dropbox.Dropbox(TOKEN)

    # Check that the access token is valid
    try:
        dbx.users_get_current_account()
    except AuthError as err:
        sys.exit(
            "ERROR: Invalid access token; try re-generating an access token from the app console on the web.")

    try:
        checkFileDetails()
    except Error as err:
        sys.exit("Error while checking file details")

    print("Creating backup...")
    # Create a backup of the current settings file

    localfile = "C:\\boleta_v1\\bd\\"+ today.strftime("%Y-%m-%d") + "\\"+ str(key) + "_" + today.strftime("%Y-%m-%d") +".sql"
    backup_data = "/respaldo_db_facturador/"+ str(key) + "_" + today.strftime("%Y-%m-%d") +".sql" # Keep the forward slash before destination filename

    backup(localfile, backup_data)

    print("Done!")