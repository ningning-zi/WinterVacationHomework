import requests
import re
if __name__ == "__main__":
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36 Edg/88.0.705.74'
    }
    for i in range(0,220,20):
          url = 'https://movie.douban.com/subject/34841067/comments?start=%d'%i+'&limit=20&status=P&sort=new_score'
          page_text = requests.get(url=url,headers=headers).text#使用通用爬虫对url对应的一整张页面进行爬取
          ex = '<span class="short">(.*?)</span>'
          text_list = re.findall(ex,page_text)#使用正则解析得到目标数据
          print(text_list)
          text_list = '\n'.join(text_list)
          file = open("hello,mom.txt", "a+",encoding='UTF-8')#保存目标数据至hello,mom.txt
          file.write(text_list + "\n")
          file.close()
import jieba
import wordcloud
import imageio
f = open('hello,mom.txt',mode="r", encoding='utf-8')
txt = f.read()
txt_list = jieba.lcut(txt)
# print(txt_list)
string1= ' '.join((txt_list))
print(string1)

img = imageio.imread("龙卷风.png")

w = wordcloud.WordCloud(width=250,
                        height=300,
                        background_color='black',
                        mask=img,
                        font_path='msyh.ttc',
                        scale=15,
                        stopwords=set([line.strip()for line in open("stopwords.txt",mode="r",encoding="utf-8").readlines()]),
                        contour_width=5,
                        contour_color='white'
                        )
w.generate(string1)
w.to_file('hello,mom.png')




