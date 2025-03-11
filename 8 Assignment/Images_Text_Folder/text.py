import random
import string


# To Create Text files (To generate passwords)
for i in range(10):
    with open(f"{i}.txt","w") as file:
        file.writelines(random.choices(string.ascii_lowercase+string.ascii_uppercase+string.punctuation,k=125))
  
  
  
        
