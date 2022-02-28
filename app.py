import os
import shutil
import datetime
from datetime import date

req_path = input("Enter your path")
age = 30

if not os.path.exists(req_path):
    print("Enter a valid path")

if os.path.isfile(req_path):
    print("Please provide directory path")

today = datetime.datetime.now()
for each_file in os.listdir(req_path):
    each_file_path = os.path.join(req_path, each_file)
    if os.path.isfile(each_file_path):
        file_cre_date = datetime.datetime.fromtimestamp(os.path.getctime(each_file_path))
        Days = (today-file_cre_date).days
        if Days > age:
           os.remove(each_file_path)