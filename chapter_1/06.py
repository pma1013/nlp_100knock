# -*- coding: utf-8 -*-


# 出題内容
# 06. 集合
# "paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．

def ngram_term_tokenizer(chars,ngram = 2):
    '''
    受け取った文字列をngramに変換
    '''
                    
    ngram_list = [chars[i:i+ngram] for i in range(len(chars) - 1)]
    return ngram_list

if __name__ == '__main__':    
    bigram_X = set(ngram_term_tokenizer("paraparaparadise"))
    bigram_Y = set(ngram_term_tokenizer("paragraph"))
                                
    # 和集合
    print(bigram_X.union(bigram_Y))
                                         
    # 積集合
    print(bigram_X.intersection(bigram_Y))


    # 差集合
    print(bigram_X.difference(bigram_Y))
            
    # 特定の文字列が含まれるかチェック
    intersec_X_Y = bigram_X.intersection(bigram_Y)
    if 'aa' in intersec_X_Y:
        print("included!")
    else:
        print("not included")

