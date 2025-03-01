with open('./data_test.csv','r',encoding='utf-8') as f:
    data= f.read()

list_of_words = data.split('\n')
enter_word = input("Enter word: ").capitalize().strip()

#english to punjabi
for i in list_of_words:
    list_csv = i.split(',')
    if enter_word in list_csv[0]:
     print(list_csv[1:])
if enter_word not in list_csv[0]:
        print("Please provide a valid input or an english word..") 
          
#punjabi to english
enter_word = input("Enter word: ").strip()  
for i in list_of_words:
    list_csv = i.split(',')
    if enter_word in list_csv[1:]:
     print(list_csv[0])
     break
#else:
if enter_word not in list_csv[1:]:
    print("Please provide a valid input or a Punjabi word..") 
      



























