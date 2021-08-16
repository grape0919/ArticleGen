from MeCab import Tagger

m = Tagger("C:\\mecab\\mecab-ko-dic")

result = m.parse("안녕하세요. 저는 까비입니다. 세종시에 있는 구글에 다니고 있지요.")
# result = m.parse("저는 세종시에서 태어났습니다.")
for elem in result.splitlines()[:-1]:
    word, morph_info = elem.split("\t")
    morph_info = morph_info.split(",")
    print(word, " : ", morph_info)
# result = m.morphs


# print(result)