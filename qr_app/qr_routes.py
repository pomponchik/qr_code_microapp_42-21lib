# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    qr_routes.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: zytrams <zytrams@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/08 21:37:59 by zytrams           #+#    #+#              #
#    Updated: 2019/11/09 09:44:08 by zytrams          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from qr_app import qr_app
from os import environ as env
import requests as reqst

# QR_CODE -> потом ссылка простым текстом под qrcode потом называние книги

def get_url():
	if env.get('URL_IP') and env.get('URL_PORT') and env.get('URL_ROUTE'):
		url = 'http://' + env.get('URL_IP') + ':' + env.get('URL_PORT') + env.get('URL_ROUTE')
	else:
		url = 'http://127.0.0.1:80/all'
	return url

@qr_app.route('/')
def index():
	return "What.. GET OUT OF HERE"

@qr_app.route('/download/qr_all')
def get_qrs_all():
	return "QRS_ALL"

@qr_app.route('/download/qr')
def get_qr():
	url = get_url()
	return reqst.get(url).content
