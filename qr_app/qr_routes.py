# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    qr_routes.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: zytrams <zytrams@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/08 21:37:59 by zytrams           #+#    #+#              #
#    Updated: 2019/11/10 10:26:32 by zytrams          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from qr_app import qr_app as QrApp
from os import environ as Env
import requests as Reqst

# QR_CODE -> потом ссылка простым текстом под qrcode потом называние книги

def get_url():
	if Env.get('URL_IP') and Env.get('URL_PORT') and Env.get('URL_ROUTE'):
		url = 'http://' + Env.get('URL_IP') + ':' + Env.get('URL_PORT') + Env.get('URL_ROUTE')
	else:
		url = 'http://127.0.0.1:80/all'
	return url

@QrApp.route('/')
def index():
	return "What.. GET OUT OF HERE"

@QrApp.route('/download/qr_all')
def get_qrs_all():
	return "QRS_ALL"

@QrApp.route('/download/qr')
def get_qr():
	url = get_url()
	return Reqst.get(url).content
