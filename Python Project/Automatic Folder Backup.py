#automatic folder backup

import os
import shutil
import daytime
import schedule
import time

source_dir = ""
destination_dir = ""

def copy_folder_to_directory(source, dest):
    today = daytime.date.today()
    dest_dir = os.path.join(dest, str(today))

    try:
        shutil.copytree(source, dest_dir)
        print(f'Folder copied to: {dest_dir}')
    except FileExistsError:
        print(f'Folder already exists in: {dest}')

#Call the function on a specified time on behalf of me
schedule.every().day.at("18:57").do(lambda: copy_folder_to_directory(source_dir, destination_dir))

while True:
    schedule.run_pending()
    time.sleep(60)



