# -*- coding: utf-8 -*-


# 08. 暗号文
# 与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．

# 英小文字ならば(219 - 文字コード)の文字に置換
# その他の文字はそのまま出力
# この関数を用い，英語のメッセージを暗号化・復号化せよ．

# 参考
# http://python.civic-apps.com/char-ord/




def cipher(chars,method):
    if method == "encryption":
        return [chr(219 - ord(c)) if 97 <= ord(c) <= 122 else c for c in chars]
    else:
        return [chr(219 - ord(c)) if (219 - 122) <= ord(c) <= (219 - 97) else c for c in chars]


print("".join(cipher("ABCabc123","encryption")))
print("".join(cipher("ABCzyx123","decryption")))

