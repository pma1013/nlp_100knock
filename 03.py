# -*- coding: utf-8 -*-


# 出題内容
#
# 03. 円周率
# "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."という文を単語に分解し，各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．

import re
pattern = re.compile('[A-z]*')

chars = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
for token in chars.split():
        print(len(re.match(pattern, token).group()))
