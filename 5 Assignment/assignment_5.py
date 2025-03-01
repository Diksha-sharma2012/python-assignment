import os
import string
from collections import Counter

file_path = "Assignment_5/demo.txt"

with open(file_path, "r", encoding='utf-8') as file:
    data: str = file.read()


# 1. Add the top 5 most common words to the analysis message
counter = Counter(data.split())
frequency = counter.most_common(5)
print("1. The top 5 most common words in the file are: ", frequency)


# 2.To count Total number of spaces     
count = 0
for line in data:
        wordslist = line.split()
        count += line.count(' ')
print("2. Total number of spaces: ", count)

# 3.To calculate total number of characters (including spaces)  
characters = 0
for line in data:  
    characters = characters + len(line) 
print("3. Total number of characters (including spaces): ", characters)  
   
# 4.To count number of characters (excluding spaces)    
num_char = 0
for line in data:
     excluding_space = characters - count    
print("4. Total Number of Characters (excluding spaces): ", excluding_space)

# 5.To count Number of words
count_word = 0
for line in data:    
        lines = data.split()  #split data into lines
        count_word += len(lines)  # count the number of words in lines that are splited by split()
print("5. Total Number of words in text file: ", count_word)

# 6.To count lines in the text file
count_lines = len(data.splitlines())
print("6. Total Number of lines in the file: ", count_lines)   
        
# 7.Display the file name and list of directories containing the file
file_name = os.path.basename(file_path)
directories = os.path.dirname(file_path)
print("7. The file name is: ", file_name)
print("   The file is located in: ",directories)

# 8. Calculate the average word length in the file
word_len = 0
for word in data.split():
    word_len+= len(word)
size = len( data.split())
# print(word_len,size)
# print(word_len/size)
total_word_seum_len = len(data.replace(" ",''))
total_word_len = len(data.split())
print("8. Average word length in file: ", total_word_len)

# 9.Find the number of unique words in the file
frequency = counter.total()  
print("9. The number of unique words in the file: ",frequency)     
 
# 10. Count the frequency of a specific word provided by the user
entered_word = input("\n    Enter a word to find its frequency: ").lower()  
frequency_word = counter.get(entered_word, 0)  
print("10. The frequency of word is:", frequency_word)
                
# 11. Identify and display all unique punctuation marks in the file                
punctuation_marks = set(ch for ch in data if ch in string.punctuation)
print("11. Unique punctuation marks in the file:", punctuation_marks)

# 12. Check if the file contains any numerical digits and count them
digit_count = 0
for char in data:
    if char.isdigit():
        digit_count += 1
print("12. Total number of numerical digits in the file: ", digit_count)

# 13. Find the longest word in the file
longest_word = len(max(lines, key=len))
print("13. The longest word in the file: ", longest_word)

#14. Find the shortest word in the file
shortest_word = len(min(lines, key=len))
print("14. The shortest word in the file: ", shortest_word)

# 15. Sort all the words alphabetically and display them
sorted_words = sorted(lines)
print("15. The alphabetically sorted words in the file: ", sorted_words)






