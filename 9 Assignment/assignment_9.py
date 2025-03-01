import random

# for i in range(50): 
#     with open (f"{i}.txt","w") as file:
#      for _ in range(20):
#          file.writelines(f"{random.randint(1,81)} {random.random():.6f} {random.random():.6f} {random.random():.6f} {random.random():.6f}\n")  
         
extra = []
with open (r"C:\Users\91887\OneDrive\Desktop\Assignment\Assignment_9\0.txt", "r") as file:
    # print(file)
    for line in file:
        val = int(line.split()[0])
        if val <= 16:
            print(val)
        
            

    
          
         
    
    
    
    
# random_values = print(f"{random.randint(1,81)} {random.random():.6f} {random.random():.6f} {random.random():.6f} {random.random():.6f}")  
    

      
        
