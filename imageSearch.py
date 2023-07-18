#importing useful modules
import requests,os
from bs4 import BeautifulSoup

url = 'https://imgur.com/search?q='
inquiry = input('What kind of images are you looking for?: ')
result = requests.get(url + inquiry)
result.raise_for_status()
page = BeautifulSoup(result.text)

images = page.select('img')
if images == []:
    print('No images found for your inquiry')
else:
    #creating a folder where downloaded images will appear
    os.makedirs('images\\' + inquiry,exist_ok = True)
    
    for i in range(3,len(images)):
        #downloading each image
        imageUrl = 'https:' + images[i].get('src')
        print(imageUrl)
        image = requests.get(imageUrl)
        image.raise_for_status()
        
        #correct the path 
        imagePath = list('images\\' + inquiry)
        
        for c in imagePath:
            if c == '/':
                c = '\\'
                
        #saving each image
        imageFile = open(os.path.join(''.join(imagePath),os.path.basename(imageUrl)),'wb')
        
        for chunk in image.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()
            
        