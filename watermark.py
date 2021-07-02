from PIL import ImageFont, ImageDraw, Image
import sys
import time

print('添加水印中，请稍后......')

# 获取参数
'''
print(sys.argv[1:])
'''
c = 0
Input_path = 'tip.png'

for i in sys.argv[1:]:
    if c == 0:
        Input_path = i
    else:
        Input_path = Input_path + i
    c += 1

out_path = Input_path
'''
print(Input_path, out_path)
'''
# 获取图形长宽

img = Image.open(Input_path)
Picture_length = img.width
Picture_high = img.height

# 添加水印

if Picture_high < 128 or Picture_length < 64:  # 如果图像宽高一个小于128px则不添加水印
    print('图片太小')
    exit()

# noinspection PyArgumentList
now_time = time.strftime("%y-%m-%d %H:%M:%S", time.localtime())
font = ImageFont.truetype(r'C:\WINDOWS\FONTS\FUTURA-LIGHT-3.TTF', 10)
draw = ImageDraw.Draw(img)

high = Picture_high - 50
position = (50, high)
draw.text(position, now_time, (0, 0, 0, 64), font=font)

high = Picture_high - 40
position = (50, high)
draw.text(position, 'by cool-gk', (0, 0, 0, 196), font=font)

img.save(out_path)
# img.show()
