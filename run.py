# Programme By Mr Beta
from os import system
from urllib.request import urlretrieve as download
system("clear")
while True:
    try:import replicate;break
    except:system('pip install replicate')

while True:
    try:
        mod = replicate.models.get("tencentarc/gfpgan")
        version = model.versions.get("9283608cc6b7be6b65a8e44983db012355fde4132009bf99d976b2f0896856a3")
        break
    except:
        print("Get Auth Token : https://replicate.com/docs/reference/http#authentication ")
        auth = input("Enter Auth Token : ")
        system("export REPLICATE_API_TOKEN="+auth)

name = input("Enter Path : ")
save = name.split('.')[0]+'_mrbeta'+'.jpg'
file = open(name,'rb').read()

print("Wait....")

link = version.predict(img=file)

download(link, save)

print(f"File Saved To : {save}")

