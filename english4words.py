from manim import *
import re

NUM = 824
"""
n. 名词 ,noun的缩写
v. 动词 , verb的缩写
pron. 代词 , pronoun的缩写
adj. 形容词, adjective的缩写
adv. 副词, adverb的缩写
num.数词 , numeral的缩写
art. 冠词, article的缩写
prep. 介词 ,前置词,preposition的缩写
conj. 连词 , conjunction的缩写
interj. 感叹词 , interjection的缩写
u = 不可数名词,uncountable noun的缩写
c = 可数名词,countable noun的缩写
pl = 复数,plural的缩写
"""

colors = {
    'v.': BLUE_A,
    'vt.': BLUE_B,
    'vi.': BLUE_C,
    'aux.': BLUE_D,
    'n.': ORANGE,
    'a.': YELLOW,
    'ad.': PINK,
    'pron.': GOLD_A,
    'prep.': GOLD_B,
    'num.': GOLD_C,
    'conj.': GOLD_D
}

class English4Words(Scene):
    def find_word(self, s):
        return s[0:4]

    def find_word_meta(self, s):
        r = re.finditer('((?<!\/)(([a-z]+\.)\/)*([a-z]+\.))', s)
        try:
            item = next(r)
        except StopIteration:
            return [('', s)]
        result = []
        while (True):
            begin, end = item.span()
            try:
                nitem = next(r)
            except StopIteration:
                nitem = None
            if nitem is None:
                result.append((s[begin: end], s[begin:]))
                break
            else:
                nbegin, nend = nitem.span()
                result.append((s[begin: end], s[begin:nbegin]))
            item = nitem
        return result

    def find_word_meta_TEXT(self, words):
        return [Text(str, font="sans-serif", color=colors[characteristic] if characteristic in colors else GREY) for characteristic, str  in words]

    def construct(self):
        p = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(p, "en_word_4c.txt"), encoding='utf8') as f:
            lines = f.readlines()

        raws = []
        for line in lines[0:]:
            one = Text(self.find_word(line), slant=ITALIC)
            word_meta = self.find_word_meta(line[4:])
            two = self.find_word_meta_TEXT(word_meta)
            lt = VGroup(*two).arrange(DOWN, buff=0.2)
            group_duo = VGroup(one, lt).arrange(DOWN, buff=0.5)
            raws.append((one, lt, group_duo))
        for one, two, group_duo in raws:
            self.play(Write(one, run_time=0.5))
            self.play(Write(two, run_time=1))
            self.play(
                FadeOut(group_duo, run_time=0.5),
            )