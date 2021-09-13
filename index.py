mport os
from urllib import request
import json
import sys

if(len(sys.argv) < 2):
    print("expected : [https] [folder_name]")
    exit(1)


a_file = open("tutorial/tutorial/spiders/quotes_spider.py", "r")
list_of_lines = a_file.readlines()
list_of_lines[8] = f'\"{sys.argv[1]}\"\n'

a_file = open("tutorial/tutorial/spiders/quotes_spider.py", "w")
a_file.writelines(list_of_lines)
a_file.close()


    
os.chdir("tutorial")
os.system("scrapy crawl quotes -o files.json")
os.chdir("..")

if not os.path.isdir(sys.argv[2]):
    os.mkdir(sys.argv[2])

with open("tutorial/files.json", "r") as jsonFile:
    read = jsonFile.read()
    data = json.loads(read)
    
    for info in data:
        icon_name = info["icon_name"]
        filename = info["filename"]
        url = info["url"]
        date = info["date"]
        desc = info["desc"]
    
        if "image" in icon_name or "text" in icon_name or "compressed" in icon_name: 
            request.urlretrieve(url, os.path.join( sys.argv[2], filename))

print("writting finished.")
os.system(" mv tutorial/files.json " + sys.argv[2])

