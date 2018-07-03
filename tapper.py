#!/usr/bin/python
# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw

_SIZE_WIDTH = 106
_SIZE_HEIGHT = 17

def welcome() -> None:
	print("Расшифровка числа по формуле Таппера")
	print("Mishin Dev Studio 2018 (c)")


def get_image() -> None:

	#---------------Subfunc-----------------#

	def get_k() -> int:
		return int(input("Введите k:"))


	def from_k_to_bin(k: int) -> list:
		k //= 17
		binary = bin(k)[2:]

		if len(binary) < 1802:
			new_binary = ""
			for i in range(1802-len(binary)):
				new_binary += "0"
			binary = new_binary + binary

		lists = [[] for x in range(17)]
		for x in range(1802):
			lists[x%17].append(binary[x])

		lists.reverse()
		return lists

	#---------------------------------------#

	k = get_k() #unsafe
	lists = from_k_to_bin(k)

	#-----Рисовашки!-----#
	image = Image.new("1", (106,17), (0))
	draw = image.load()
	for y in range(17):
		for x in range(106):
			image.putpixel(xy = (105-x,16-y), value = (int(lists[y][x]),))
	image.save("image.png")


def generate_image() -> None:

	#---------------Subfunc-----------------#

	def attention() -> None:
		print("Внимание! Изображение должно быть сторого разрешения 106х17 пикселей!")


	def get_image() -> Image:
		name = input("Введите название изображения (должно находится в одной папке со скриптом):")
		try:
			im = Image.open(name)
		except Exception:
			print("Неудача!")
			exit(0)

		return im

	#---------------------------------------#

	attention()
	image = get_image()
	width, height = image.size

	flag_okay = False
	if width == _SIZE_WIDTH and height == _SIZE_HEIGHT:
		flag_okay = True

	if not flag_okay:
		print("Недопустимый размер изображения")
		print(width, height)
		exit(0)

	print("Все ок!")
	image = image.convert('1')
	image.save('result.png')

	byteset = ""
	for x in range(105,-1,-1):
		for y in range(0,17):
			byte = str(image.getpixel((x,y)))
			if byte == "255":
				byteset += '1'
			else:
				byteset += '0'

	k = int(byteset,2)*17

	print("Все готово:")
	print(k)
	


def main():
	welcome()
	print("Из k получить изображение (0) или из изображения получить k (1) ?")
	choice = int(input())
	if choice > 1:
		main()
	else:
		if choice == 0:
			get_image()
		else:
			generate_image()


if __name__ == '__main__':
	main()