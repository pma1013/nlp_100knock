# -*- coding: utf-8 -*-


# 出題内容
#
# 04. 元素記号
# "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，それ以外の単語は先頭に2文字を取り出し，取り出した文字列から単語の位置（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ．

unigram_idx = [1, 5, 6, 7, 8, 9, 15, 16, 19]
element_dict = {}

chars = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
for idx,token in enumerate(chars.split()):
        if idx+1 in unigram_idx:
            element_dict[token[0:1]] = idx + 1
        else:
            element_dict[token[0:2]] = idx + 1

