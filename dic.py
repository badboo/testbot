import codecs

bot_dict = {}
with codecs.open('dic.txt', encoding='utf-8') as file:
    for line in file:
        line = line.rstrip('\r\n')
        word_list = line.split()
        bot_dict[word_list[0]] = word_list[1]

i = input('曜日の英訳 > ')

if i in bot_dict :
    print('{}'.format(bot_dict[i]))
else :
    print('単語が見つかりません\n※月曜日から日曜日までの曜日を入力してください')

'''
command_file = codecs.open ('dic.txt', 'r', encoding='utf8')
data = command_file.read()
command_file.close()
lines = data.splitlines()
for row in lines:
    print(row)
'''




