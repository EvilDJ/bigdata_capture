import jieba
import jieba.analyse as pos
import codecs
import jieba.posseg as psg


text = '请问老公的生育险老婆能报吗;老婆没有工作也没买社保;老公的社保已经连续买了4年'

seg_list = psg.cut(text)#获得子的词性
# seg_list = pos.textrank(text)#提取关键字
# seg_list = pos.extract_tags(text)
for i in seg_list:
    print(i)
