#政府工作报告词云
import jieba
import wordcloud
f1 = open("中共中央 国务院关于实施乡村振兴战略的意见.txt","rt",encoding="utf-8")
f2 = open("决胜全面建成小康社会 夺取新时代中国特色社会主义伟大胜利.txt","rt",encoding="utf-8")
t1 = f1.read()
t2 = f2.read()
t = t1 + t2
f1.close()
f2.close()
ls = jieba.lcut(t)
txt = " ".join(ls)
w = wordcloud.WordCloud(font_path="msyh.ttc",\
                        width=1000,height=1000,\
                        background_color="white",)
w.generate(txt)
w.to_file("政府工作报告词云1.png")