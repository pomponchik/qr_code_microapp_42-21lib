# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    qr_composer.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: zytrams <zytrams@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/10 09:08:13 by zytrams           #+#    #+#              #
#    Updated: 2019/11/10 10:27:22 by zytrams          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from PIL import Image as I, ImageColor as IC
from qr_app.qr_image import QrImage

class QrComposer():
	A4_W = 2481
	A4_H = 3508

	def __init__(self, x_times, y_times):
		self.xchunksize = int(self.A4_W / x_times)
		self.ychunksize = int(self.A4_H / y_times)
		self.xoffset = 0
		self.yoffset = 0

	def a4_resize_image(self, x_times, y_times):
		self.a4_img = I.new('RGB', (self.A4_WIDTH, self.A4_HEIGHT), color=IC.getrgb('white'))
		new_w = int(self.A4_WIDTH / x_times)
		new_h = int(self.A4_HEIGHT / y_times)
		self.resized_img = self.img.resize((new_w, new_h))

	# Static method
	@staticmethod
	def create_image_filled(qr_img, x_times, y_times, A4_W = 2481, A4_H = 3508):
		a4_img = I.new('RGB', (A4_W, A4_H), color=IC.getrgb('white'))
		new_w = int(A4_W / x_times)
		new_h = int(A4_H / y_times)
		resized_img = qr_img.img.resize((new_w, new_h))
		x_offset = 0
		for x in range(0, x_times):
			y_offset = 0
			for y in range (0, y_times):
				a4_img.paste(resized_img, (x_offset, y_offset))
				y_offset += new_h
			x_offset += new_w
		return a4_img

	@staticmethod
	def save(img, fname):
		img.save(fname, 'PNG')
