import os
import codecs

'''
bot_dict = {
    '板金': '金属の板を塑性変形させて各種の形に作ること。',
    '塗装': 'スル ものの表面に，装飾・保護などの目的で 塗料を塗ったり吹きつけたりして被膜をつくること。',
    'さようなら': 'サヨウナラ',
    }
'''

bot_dict = {}
with codecs.open('web/dic.txt', encoding='utf-8') as file:
    for line in file:
        line = line.rstrip('\r\n')
        word_list = line.split()
        bot_dict[word_list[0]] = word_list[1]

bot_dict['さようなら'] = 'サヨウナラ'

print('Kado AI')
while True:
    print('何か聞きたいことは、ありますか？')
    question = input('>> ')
    question = '質問：' + question
    print(question)
    answer = ''

    for key in bot_dict:
        if key in question:
            answer = bot_dict[key]
            break

    if not answer:
        answer = '何ヲ言ッテイルカ、ワカラナイ'
    print('答え：' + answer.replace('/**/', os.linesep) + '\n')

    if 'さようなら' in question:
        break


    '''
    if '板金' in question:
        answer += '金属の板を塑性変形させて各種の形に作ること。\n'
    elif '塗装' in question:
        answer += 'スル ものの表面に，装飾・保護などの目的で 塗料を塗ったり吹きつけたりして被膜をつくること。\n'
    elif 'さようなら' in question:
        print('サヨウナラ')
        break
    else:
        answer += '何ヲ言ッテイルカ、ワカラナイ\n'
    print(answer)
   '''
