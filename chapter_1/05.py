# -*- coding: utf-8 -*-


# 出題内容
#
# 05. n-gram
# 与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．


                            
def ngram_term_tokenizer(chars,ngram = 2):
    token_list = chars.split()
    last = len(token_list) - (ngram - 1)
    for i in range(last):
        print(token_list[i:i+ngram])

    for i in range(len(chars) - 1):
        print(chars[i:i+ngram])
                                                


ngram_term_tokenizer("I am an NLPer")
