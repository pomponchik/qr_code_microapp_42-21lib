# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    qr_routes.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: zytrams <zytrams@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/08 21:37:59 by zytrams           #+#    #+#              #
#    Updated: 2020/01/07 15:29:07 by zytrams          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from qr_app import qr_app
from os import environ as Env
from qr_app.qr_composer import QrComposer
from qr_app.qr_image import QrImage
from flask import send_file
import json
import os
import requests as Reqst

qr_compo = QrComposer(3, 8)

# QR_CODE -> потом ссылка простым текстом под qrcode потом название книги
def get_url():
	url = 'https://library.21-school.ru/'
	if Env.get('SITE_URL'):
		#изменил название старой переменной окружения, т.к. уже используется
		url = 'http://' + Env.get('SITE_URL')
	if Env.get('SITE_IP') and Env.get('SITE_PORT') and Env.get('SITE_ROUTE'):
		url = 'http://' + Env.get('SITE_IP') + ':' + Env.get('SITE_PORT') + Env.get('SITE_ROUTE')
	return url

@qr_app.route('/')
def index():
	return "ВЫ КТО ТАКИЕ?!! Я ВАС НЕ ЗВАЛ!!! ИДИТЕ ***!!!"

@qr_app.route('/api/get/all')
def get_qrs_all():
	#os.remove('libqrcodes.pdf')
	url = get_url() + '/api/get_all_books'
	try:
		books = json.loads(Reqst.get(url).content)
	except Exception as e:
		return str(e)
	qr_books = []
	for book in books:
		qr_books.append(QrImage(f'{get_url()}/book' + book['id'], book['name']))
	qr_compo.put_qrs(qr_books)
	try:
		return send_file(os.path.dirname(os.path.realpath(__file__)) + '/../libqrcodes.pdf', attachment_filename='libqrcodes.pdf')
	except Exception as e:
		return str(e)
