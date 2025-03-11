import os
import shutil

images_extensions = (".jpg", ".png", ".jpeg", ".gif", ".tiff", ".bmp")

list_files = (os.listdir('./Assignment_8/Images_Text_Folder'))

for filename in list_files:
    if filename.endswith('.txt'):
        print(filename)
        shutil.move('./Images_Text_Folder/'+ filename,"./Train/text/"+filename )
        
    elif filename.endswith(images_extensions):
        print(filename)
        shutil.move('./Images_Text_Folder/'+filename, './Train/images/'+filename) 
   
    
    







           