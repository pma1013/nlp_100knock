# -*- coding: utf-8 -*-

# 09. Typoglycemia
# スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，
# それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．
# ただし，長さが４以下の単語は並び替えないこととする．
# 適当な英語の文（例えば"I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."）を与え，その実行結果を確認せよ．
import random

def shuffle_char(chars):
    last = len(chars) - 1
    # 先頭1文字
    head_char = chars[:1:]
                   
    # シャッフル対象文字
    shuffle_char = list(chars[1:last])
                               
    # 末尾1文字
    tail_char = chars[-1::]

    # これだとなぜかシャッフルが効かない
    #random.shuffle(char_list[1:last])

    random.shuffle(shuffle_char)
                                                       
    shuffle_char.insert(0,head_char)
    shuffle_char.append(tail_char)
    return "".join(shuffle_char)



chars_list = []    
chars = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
for c in chars.split():
    if len(c) <= 4:
        chars_list.append(c)
    else:
        chars_list.append(shuffle_char(c))


print(" ".join(chars_list))
