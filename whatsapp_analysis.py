import os,re
from collections import Counter


file = open('./Files/WhatsApp_Chat.txt', encoding="utf8")    
chat_text = file.read()
file.close()

# Create a Regular Expression and extract member name or number from the chat text file
members_regex = re.compile(r'M - .*?:')
members = members_regex.findall(chat_text)

# Clean the names and numbers prefeix and suffix
members = [str(i).lstrip('M - ').rstrip(':') for i in members]

# Count the repetition for each member
members_count = Counter(members)


# Print to a file list of members with number of repetition ordered descendingly
count_output = open('./Files/whatsapp_count.txt','w',encoding = 'utf-16')

for member,count in members_count.most_common():
    line = f'{member} : {count}'
    count_output.write(line + '\n')
    print(line)

count_output.close()
print('List writen to ./Files/file whatsapp_count.txt')
