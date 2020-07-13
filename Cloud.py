# 导入wordcloud模块和matplotlib模块
import imageio
from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt


# 读取一个txt文件

text = open('/Users/zbx/Desktop/Key'+str(i)+'.txt', 'r').read()

# 读入背景图片

bg_pic = imageio.imread('/Users/zbx/Desktop/stars.png')

# 生成词云

wordcloud = WordCloud(mask=bg_pic, background_color='white', scale=1.5).generate(text)

image_colors = ImageColorGenerator(bg_pic)
# 显示词云图片

plt.imshow(wordcloud)
plt.axis('off')
plt.show()

# 保存图片

wordcloud.to_file('/Users/zbx/Desktop/test'+'.jpg')

