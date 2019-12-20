import os
import time,datetime,shutil
import traceback
BACK_PATH='/home/python/backdata/'
DATETIME = time.strftime('%Y%m%d')
TODAY_PATH = BACK_PATH+DATETIME
today = datetime.datetime.now()
if not os.path.exists(TODAY_PATH):
    os.makedirs(TODAY_PATH)
for item in os.listdir(BACK_PATH):
        try:
            foldername = os.path.split(item)[1]
            day = datetime.datetime.strptime(foldername, "%Y%m%d")
            #diff = int(DATETIME) - int(foldername)
            diff = today-day
            if diff.days>=3:
                print('- - - del folder 3 days ago: ' + BACK_PATH + item)
                shutil.rmtree(BACK_PATH + item)
        except:
            traceback.print_exc()
            pass
def back(DB_NAME):
    DB_PATH = TODAY_PATH + "/" + DB_NAME + ".sql.gz"
    print("- - - baking '" + DB_NAME + ".sql'")
    dumpcmd  = 'mysqldump -h192.168.3.126 -uroot -pReedsec888 --compact data_base '+DB_NAME+'|gzip>'+DB_PATH
    os.system(dumpcmd)
    print("- - - Your backups has been created in '" + TODAY_PATH + "' directory")
try:
    back('t_stock2')
    back('t_stock_A')
    back('t_stock_HK')
    back('t_stock_US')
except:
    traceback.print_exc()
    pass