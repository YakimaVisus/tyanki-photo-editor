from PIL import Image, ImageDraw, ImageFont
import sys
import requests
import random
import os
print("""
⣿⠿⠿⠶⠿⢿⣿⣿⣿⣿⣦⣤⣄⢀⡅⢠⣾⣛⡉⠄⠄⠄⠸⣿ 
⣡⣴⣶⣶⡀⠄⠄⠙⢿⣿⣿⣿⣿⣿⣴⣿⣿⣿⢃⣤⣄⣀⣥⣿ 
⠻⣿⣿⣿⣧⣀⢀⣠⡌⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⣿⣿ 
⣷⣤⣤⣤⣬⣙⣛⢿⣿⣿⣿⣿⣿⣿⡿⣿⣿⡍⠄⠄⢀⣤⣄⠋ 
⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⢇⣿⣿⡷⠶⠶⢿⣿⣿⢀ 
⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⣿⣿⡇⣿⣿⣿⣿⣿⣿⣷⣶⣥⣴ 
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟ 
⣛⣻⣿⣿⣧⠙⠛⠛⡭⠅⠒⠦⠭⣭⡻⣿⣿⣿⣿⣿⣿⣿⣿⠃ 
⣿⣿⣿⣿⣿⡆⠄ Yakima⠹⠈⢋⣽⣿⣿⣿⣿⣵⠃ 
⣿⣿⣿⣿⣿⣿⠄⣴⣿⣶⣄⠄⣴⣶⠄⢀⣾⣿⣿⣿⣿⣿⣿⠄ 
⣿⣿⣿⣿⣿⡄⢻⣿⣿⣿⠄⣿⣿⡀⣾⣿⣿⣿⣿⣛⠛⠁ 
⠈⠛⢿⣿⣿⣿⠁⠞⢿⣿⣿⡄⢿⣿⡇⣸⣿⣿⠿⠛⠁ 
⠄⠄⠄⠉⠻⣿⣿⣾⣦⡙⠻⣷⣾⣿⠃⠿⠋⠁ 
⣶⣮⣥⣒⠲⢮⣝⡿⣿⣿⡆⣿⡿⠃ 
 
My Github: https://github.com/YakimaVisus
""")
number_list = ["https://share-cdn.picrew.me/shareImg/org/202201/463977_tiLhbrrj.png","https://share-cdn.picrew.me/shareImg/org/202201/463977_M8GM02mx.png","https://share-cdn.picrew.me/shareImg/org/202201/463977_qQBIuY71.png","https://share-cdn.picrew.me/shareImg/org/202201/463977_p24Y2Btc.png","https://share-cdn.picrew.me/shareImg/org/202201/463977_CbggWqDZ.png","https://share-cdn.picrew.me/shareImg/org/202201/463977_awNtsMal.png","https://share-cdn.picrew.me/shareImg/org/202201/463977_BY7NeNel.png","https://share-cdn.picrew.me/shareImg/org/202201/463977_AaEY5TAF.png","https://share-cdn.picrew.me/shareImg/org/202201/463977_7Gu8tn40.png","https://share-cdn.picrew.me/shareImg/org/202201/463977_s8cAmaHE.png","https://share-cdn.picrew.me/shareImg/org/202201/463977_t9ONlivW.png","https://share-cdn.picrew.me/shareImg/org/202201/463977_zbFN8oHV.png","https://share-cdn.picrew.me/shareImg/org/202201/463977_ng8vdSL1.png"]
image_url = random.choice(number_list)
img_data = requests.get(image_url).content #если в (image_url) сунуть ссылку на фотку то обрабатывать будет ее также и скачает Пример; img_data = requests.get("https://share-cdn.picrew.me/shareImg/org/202201/463977_M8GM02mx.png").content
print('Рандомная Тян Загружена /text_tyn.png')

with open('text_tyn.png', 'wb') as handler:
    handler.write(img_data)
    tatras = Image.open("text_tyn.png")
    idraw = ImageDraw.Draw(tatras)
    text = input ("Буковки на вашей тян: ")
    font = ImageFont.truetype("17634.ttf", size=34)
    idraw.text((10, 10),  text, font=font, fill=(199, 21, 133) )
    tatras.save('text_tyn.png')
    
    print ("Тянка с текстом  <",text,">  готова! /text_tyn.png")
    a = input ("Поставить фон? y/n: ")
    if a == 'n':
        print('Завершение программы...')
        sys.exit()
    phon = input("Введите url фотки на фон, можно использовать piska.jpg: ")
    im = Image.open(phon)
    im2 = Image.open('text_tyn.png')
    position = (im.width - im2.width,
                    im.height - im2.height)
    im.paste(im2, position, im2)

    im.save('text_tyn.png', quality=95)
    a = input ("Продолжить настройку? y/n: ")
    if a == 'n':
        print('Завершение программы...')
        sys.exit()
print ('''
0 = Оттенки серого
1 = Сепия
2 = Негатив
3 = Добавление шумов
4 = Яркость
5 = Чёрно — белое изображение
Хуита взята с хабра ибо лень было все самому писать не злитесь пж
''')
mode = int(input('режим:'))  
image = Image.open("text_tyn.png")  
draw = ImageDraw.Draw(image)  
width = image.size[0]  
height = image.size[1]  	
pix = image.load() 
if (mode == 0):
	for i in range(width):
		for j in range(height):
			a = pix[i, j][0]
			b = pix[i, j][1]
			c = pix[i, j][2]
			S = (a + b + c) // 3
			draw.point((i, j), (S, S, S))
if (mode == 1):
	depth = int(input('depth:'))
	for i in range(width):
		for j in range(height):
			a = pix[i, j][0]
			b = pix[i, j][1]
			c = pix[i, j][2]
			S = (a + b + c) // 3
			a = S + depth * 2
			b = S + depth
			c = S
			if (a > 255):
				a = 255
			if (b > 255):
				b = 255
			if (c > 255):
				c = 255
			draw.point((i, j), (a, b, c))
if (mode == 2):
	for i in range(width):
		for j in range(height):
			a = pix[i, j][0]
			b = pix[i, j][1]
			c = pix[i, j][2]
			draw.point((i, j), (255 - a, 255 - b, 255 - c))
if (mode == 3):
	factor = int(input('factor:'))
	for i in range(width):
		for j in range(height):
			rand = random.randint(-factor, factor)
			a = pix[i, j][0] + rand
			b = pix[i, j][1] + rand
			c = pix[i, j][2] + rand
			if (a < 0):
				a = 0
			if (b < 0):
				b = 0
			if (c < 0):
				c = 0
			if (a > 255):
				a = 255
			if (b > 255):
				b = 255
			if (c > 255):
				c = 255
			draw.point((i, j), (a, b, c))
if (mode == 4):
	factor = int(input('factor:'))
	for i in range(width):
		for j in range(height):
			a = pix[i, j][0] + factor
			b = pix[i, j][1] + factor
			c = pix[i, j][2] + factor
			if (a < 0):
				a = 0
			if (b < 0):
				b = 0
			if (c < 0):
				c = 0
			if (a > 255):
				a = 255
			if (b > 255):
				b = 255
			if (c > 255):
				c = 255
			draw.point((i, j), (a, b, c))
if (mode == 5):
	factor = int(input('factor:'))
	for i in range(width):
		for j in range(height):
			a = pix[i, j][0]
			b = pix[i, j][1]
			c = pix[i, j][2]
			S = a + b + c
			if (S > (((255 + factor) // 2) * 3)):
				a, b, c = 255, 255, 255
			else:
				a, b, c = 0, 0, 0
			draw.point((i, j), (a, b, c))
print('Все готово /text_tyn.png')
image.save("text_tyn.png")
del draw