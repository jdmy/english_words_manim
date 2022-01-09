import os

from pydub import AudioSegment
base_path = os.path.dirname(os.path.abspath(__file__))

# 单词map
words_map = {}
# 原始单词顺序表
raw_order_words = []
# 单词顺序列表
result = []
# 单词文件地址索引表
result_words = {}
# 单词时长表
words_duration = {}

class Voice:
    def find_word(self, s):
        return s[0:4]

    def copy_all(self):
        import os
        with open('C:/Users/Administrator/PycharmProjects/lc/manimspace/en_word_4c.txt', encoding='utf8') as f:
            lines = f.readlines()
        for line in lines:
            if self.find_word(line) in words_map:
                print(self.find_word(line))
            words_map[self.find_word(line)] = 1;
            raw_order_words.append(self.find_word(line))
        # for fpathe, dirs, fs in os.walk('C:/Users/Administrator/PycharmProjects/lc/goolge_translate/output'):
        for fpathe, dirs, fs in os.walk('E:/4字单词/voice'):
            for f in fs:
                word_name,ext = os.path.splitext(f)
                if word_name in words_map:
                    result_words[word_name] = os.path.join(fpathe, f)
                    result.append(word_name)
        print(len(result_words))
        print(len(words_map))
        for word in words_map:
            if word not in result_words:
                print(word)

    def find_all_duration_and_padding(self):
        dbs = 0
        for r in result:
            print(r, result_words[r], end=' ')

            if 'wav' in result_words[r]:
                voice = AudioSegment.from_wav(result_words[r])
            else:
                voice = AudioSegment.from_mp3(result_words[r])
            voice_db = voice.dBFS
            voice_duration = len(voice)
            silence = AudioSegment.silent(duration=2000 - voice_duration + 1)
            padded = voice + silence
            words_duration[r] = voice_duration
            dbs = dbs +voice_db
            print(r, result_words[r], voice_db, end=' ')
            print(voice_duration)

            padded.export( './output/' + r + ".wav", format='wav')

    def join_all_voice(self):
        output = None
        print('start')
        for r in raw_order_words:
            print(r)
            cur = AudioSegment.from_wav(os.path.join(base_path, 'output', r+'.wav'))
            if output is None:
                output = cur
            else:
                output = output + cur
        output.export('./release/output.wav', format='wav')


if __name__ == '__main__':
    v = Voice()
    v.copy_all()
    # v.find_all_duration_and_padding()
    v.join_all_voice()
