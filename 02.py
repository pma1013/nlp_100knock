# -*- coding: utf-8 -*-


# 出題内容
#
# 02. 「パトカー」＋「タクシー」＝「パタトクカシーー」
# 「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．


# 参考
# http://qiita.com/y__sama/items/a2c458de97c4aa5a98e7

chars1 = "パトカー"
chars2 = "タクシー"
    
patato=[]
for i in zip(chars1,chars2):
    for j in i:
        patato.append("".join(j))
print("".join(patato))

print("内包表記で書くと")
print("".join(["".join(j) for i in zip(chars1,chars2) for j in i]))


print("インデントすると")
print("".join(
  [
  "".join(j)
  for i in zip(chars1,chars2)
    for j in i
  ]
)
)
print("外のjoinなくすと")
print(
  [
  "".join(j)
  for i in zip(chars1,chars2)
    for j in i
  ]
)

