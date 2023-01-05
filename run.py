# Programme By Mr Beta
from os import system
from urllib.request import urlretrieve as download
system("clear")
while True:
    try:import replicate;break
    except:system('pip install replicate');system("clear")


try:
    tools = replicate.models.get("tencentarc/gfpgan")
    version = tools.versions.get("9283608cc6b7be6b65a8e44983db012355fde4132009bf99d976b2f0896856a3")
except:
    system("bash token.sh");exit()

name = input("Enter Path : ")
try:file = open(name,'rb')
except:exit("File Not Found")
save = name.split('.')[0]+'_mrbeta'+'.jpg'

print("Wait....")

link = version.predict(img=file)

download(link, save)

print(f"File Saved To : {save}")

