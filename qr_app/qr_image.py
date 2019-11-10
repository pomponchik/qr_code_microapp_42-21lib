# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    qr_image.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: zytrams <zytrams@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/08 20:51:19 by zytrams           #+#    #+#              #
#    Updated: 2019/11/10 12:45:30 by zytrams          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import qrcode as QR

# Class for qr image and string url and label for book
# Field @img: PilImage instance for qr_code image
# Field @surl: Str for full which leads to book
# Field @label: Str for caption under qr code image
class	QrImage():

	def __init__(self, url = None, label = None):
		if (url):
			self.surl = url
		else:
			self.surl = 'http://lib.ru/POEZIQ/DANTE/comedy.txt' # default url for testing
		if (label):
			self.label = label
		else:
			self.label = 'La Divina Commedia, Dante Alighieri' # default label for testing
		self.img = QR.make(self.surl)

	# Save image nearby into file
	def save(self):
		self.img.save(self.surl, 'PNG')
