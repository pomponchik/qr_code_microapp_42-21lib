# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    qr_composer.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: zytrams <zytrams@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/10 09:08:13 by zytrams           #+#    #+#              #
#    Updated: 2019/11/10 09:38:59 by zytrams          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from PIL import Image as I, ImageColor as IC
import qrcode
from qr_app import qr_image


class QrComposer():

	def a4_resize_image(self, x_times, y_times):
		self.a4_img = I.new('RGB', (self.A4_WIDTH, self.A4_HEIGHT), color=IC.getrgb('white'))
		new_w = int(self.A4_WIDTH / x_times)
		new_h = int(self.A4_HEIGHT / y_times)
		self.resized_img = self.img.resize((new_w, new_h))
		self.x_offset = 0
		for x in range(0, x_times):
			y_offset = 0
			for y in range (0, y_times):
				self.a4_img.paste(resized_img, (x_offset, y_offset))
				y_offset += new_h
			x_offset += new_w

	def a4_fill_with_qr(self, x_times, y_times):
		self.x_offset = 0
		for x in range(0, x_times):
			y_offset = 0
			for y in range (0, y_times):
				self.a4_img.paste(self.resized_img, (x_offset, y_offset))
				y_offset += new_h
			x_offset += new_w
