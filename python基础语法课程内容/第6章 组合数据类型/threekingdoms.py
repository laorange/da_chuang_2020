#三国演义人物出场顺序统计
import jieba
txt = open("threekingdons.txt","r",encoding="utf-8").read()
excludes = {"将军","却说","荆州","二人","不可","不能","如此","商议"\
    ,"如何","主公","军士","左右","军马","引兵","次日","大喜","天下",\
    "东吴","于是","今日","不敢","魏兵","陛下","一人","都督","人马",\
    "不知","汉中","只见","众将","后主","蜀兵","上马","大叫","太守",\
    "此人","后人","背后","城中","天子","一面","夫人","何不","大军", \
    "忽报","先生","百姓","何故","然后","先锋","不如","赶来"}
words = jieba.lcut(txt)
counts = {}
for word in words:
    if len(word)==1:
        continue
    elif word =='诸葛亮' or word == '孔明曰':
        rword ="孔明"
    elif word =='关公' or word == '云长':
        rword = '关羽'
    elif word =='玄德' or word == '玄德曰' or word == '先主':
        rword = '刘备'
    elif word =='孟德' or word == '丞相':
        rword = '曹操'
    #elif word =='' or word == '':
    #    rword = ''
    else:
        rword = word
    counts[rword] = counts.get(rword,0)+1
for word in excludes:
    del counts[word]
items = list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(15):
    word, count = items[i]
    print("{0}\t{1:>10}".format(word,count))