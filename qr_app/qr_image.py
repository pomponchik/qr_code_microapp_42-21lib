# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    qr_image.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: zytrams <zytrams@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/08 20:51:19 by zytrams           #+#    #+#              #
#    Updated: 2019/11/10 09:47:24 by zytrams          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from PIL import Image as I, ImageColor as IC
import qrcode as QR

# Class for qr image and
class	QrImage():

	def __init__(self, url = None):
		if (string):
			self.surl = url
		else:
			self.surl = 'https://ya.ru'
		self.img = QR.make(self.s)
		self.x_offset = 0

	def save(self):
		self.img.save(self.surl, 'PNG')
