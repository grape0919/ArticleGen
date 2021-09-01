

from markovify import text
from konlpy.tag import Mecab

class POSifiedText(text.Text):

    tagger = Mecab(dicpath="C:\\mecab\\mecab-ko-dic")

    space_tag_list = ("J", "EF", "EC", "ET", "SF", "SE", "NNBC", "SC", "M")
    add_space_tag_list = [ "+"+tag for tag in space_tag_list ]

    def word_split(self, sentence):

        morphs = [ "::".join(tag) for tag in self.tagger.pos(sentence) ]
        return morphs

    def word_join(self, words):

        sentence = ""
        pre_tag = ""
        for word_pos in words:
            if isinstance(word_pos, tuple):
                sentence += "{"
                for tp in list(word_pos):
                    if tp.startswith("__"):
                        continue
                    word, tag = tp.split("::")

                    if len(sentence) > 0:
                        # 이전 띄어쓰기를 제거하는 경우
                        if (tag.startswith("J") or tag.startswith("SF") or\
                            tag.startswith("SE") or tag.startswith("SY"))\
                            and sentence[-1] == " ":
                            sentence = sentence[:-1]

                        # 현재 형태소로 인해 이전 띄어쓰기를 추가하는 경우
                        if (pre_tag == "XSN" and tag == "NNG") or\
                            (sentence[-1] != " " and tag == "MAG"):
                            sentence += " "

                    sentence += word + "|"

                if sentence.endswith("|"):
                    sentence = sentence[:-1]
                sentence += "}"
                if tag.startswith(self.space_tag_list) and not "+" in tag:
                    sentence += " "
                elif any(map(tag.__contains__, self.add_space_tag_list)):
                    sentence += " "
                
                pre_tag = tag.split("+")[-1] if "+" in tag else tag
            else:
                if "::" not in word_pos:
                        continue
                
                word, tag = word_pos.split("::")

                if len(sentence) > 0:
                    # 이전 띄어쓰기를 제거하는 경우
                    if (tag.startswith("J") or tag.startswith("SF") or\
                        tag.startswith("SE") or tag.startswith("SY"))\
                        and sentence[-1] == " ":
                        sentence = sentence[:-1]

                    # 현재 형태소로 인해 이전 띄어쓰기를 추가하는 경우
                    if (pre_tag == "XSN" and tag == "NNG") or\
                        (sentence[-1] != " " and tag == "MAG"):
                        sentence += " "

                sentence += word
                if tag.startswith(self.space_tag_list) and not "+" in tag:
                    sentence += " "
                elif any(map(tag.__contains__, self.add_space_tag_list)):
                    sentence += " "
                
                pre_tag = tag.split("+")[-1] if "+" in tag else tag

        return sentence

    def compile(self, inplace=False):
        if inplace:
            self.chain.compile(inplace=True)
            return self
        cchain = self.chain.compile(inplace=False)
        psent = None
        if hasattr(self, "parsed_sentences"):
            psent = self.parsed_sentences
        return POSifiedText(
            None,
            state_size=self.state_size,
            chain=cchain,
            parsed_sentences=psent,
            retain_original=self.retain_original,
            well_formed=self.well_formed,
            reject_reg=self.reject_pat,
        )
