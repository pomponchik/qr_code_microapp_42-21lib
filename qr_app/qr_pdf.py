# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    qr_pdf.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: zytrams <zytrams@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/09 09:51:59 by zytrams           #+#    #+#              #
#    Updated: 2019/11/10 09:53:35 by zytrams          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import labels
from reportlab.graphics import shapes
from reportlab.lib import colors
import os.path

# A class for pdf file creation
class QrPdfSheet():
	A4_WIDTH = 2481
	A4_HEIGHT = 3508
	dirname = os.path.dirname(__file__)
	bgname = os.path.join(dirname, "qr_image_a4.png")
	pdfname = "libqrcodes.pdf"

	def __init__(self, bgname, pdfname, x_times, y_times):
		if bgname:
			self.bgname = bgname
		if pdfname:
			self.pdfname = pdfname
		self.bgimg = shapes.Image(0, 0, 750, 1055, bgname)
		self.specs = labels.Specification(210, 297, x_times, y_times,
		int(A4_WIDTH / x_times), int(A4_HEIGHT / y_times), background_image=self.bgimg)

	#def add_bg_on_page(self, bgimg):
	# Paths to the images used for backgrounds.
	# Create a function to draw each label. This will be given the ReportLab drawing
	# object to draw on, the dimensions (NB. these will be in points, the unit
	# ReportLab uses) of the label, and the object to render.
	def draw_label(self, label, width, height, obj):
		# Just convert the object to a string and print this at the bottom left of
		# the label.
		label.add(shapes.String(2, 2, str(obj), font_name="Helvetica", font_size = 2))

	def create_pdf(self):
		# Create the sheet.
		sheet = labels.Sheet(specs, draw_label)
		# Add costil first label.
		sheet.add_label("")
		# Save the file and we are done.
		sheet.save(self.filename)
		print("{0:s}: {1:d} label(s) output on {2:d} page(s).".format(self.filename, sheet.label_count, sheet.page_count))

	def set_bgimg:


