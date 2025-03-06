import datetime
import shutil
import os
import schedule
import time



source_dir = "C:/Users/satye/OneDrive/Pictures/Screenshots 1"
destination_dir = "G:/ScreenShotsBackup/Backup"



def backup_data(source,dest):
    
    today = datetime.date.today()
    dest_dir = os.path.join(dest,str(today))
    now = str(datetime.datetime.now())

    try:
        shutil.copytree(source,dest)
        print(f"BackUp Secured At {now} in {dest_dir} Folder.")

    except FileExistsError:
        print(f"Folder already exists in: {dest} Folder.")



schedule.every().day.at("03:39").do(lambda : backup_data(source_dir,destination_dir))



while True:
    schedule.run_pending()
    time.sleep(60)



