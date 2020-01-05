# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    qr_pdf.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: zytrams <zytrams@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/09 09:51:59 by zytrams           #+#    #+#              #
#    Updated: 2020/01/05 04:43:31 by zytrams          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from fpdf import FPDF
import os

# A class for pdf file creation
class PdfDecorator():
	A4_WIDTH = 210
	A4_HEIGHT = 297

	def __init__(self, pdfname):
		self.pdf = FPDF(unit='pt')
		self.pdf.add_font('DejaVu', '', '/Users/zytrams/qr/font/dejavu-sans-mono.ttf', uni=True)
		self.pdf.set_font("DejaVu", size = 5)
		if pdfname:
			self.pdfname = pdfname
		else:
			self.pdfname = "libqrcodes.pdf"

	def new_page(self):
		self.pdf.add_page()

	def put_label(self, x, y, string):
		while string:
			s = string[:30]
			self.pdf.text(x, y, s)
			y = y + 5
			string = string[30:]

	def put_image(self, x, y, w, h, img):
		img.save('uga.png', 'PNG')
		self.pdf.image('uga.png', x, y, w=w, h=h)
		os.remove('uga.png')

	def save_pdf(self):
		self.pdf.output(self.pdfname)
