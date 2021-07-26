import os,re

def remove_prepostfix(text, prefix):
    return text[text.startswith(prefix) and len(prefix):len(text) - 1]

file = open('/Users/elfatihsaeed/Documents/GoogleDrive/DataScience/PythonProg/WhatsApp Chat with إخواناً في الجنة متحابين❤️.txt', encoding="utf8")    
text = file.read()
file.close()

nameRegex = re.compile(r'M - .*?:')
mo = nameRegex.findall(text)

count = {}
for i in mo:
    i = remove_prepostfix(i,'M - ')
    count.setdefault(i,0)
    count[i] = count[i] + 1
sortedCount = sorted(count.items(),key=lambda x:x[1],reverse=True)
count_output = open('/Users/elfatihsaeed/Desktop/whatsappCount_akhwan.txt','w',encoding = 'utf-16')

for i in sortedCount:
    line = i[0] + " : " + str(i[1])
    count_output.write(line + '\n')
    print(line)

count_output.close()
print('List writen to file whatsappCount_akhwan.txt')
