# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    __init__.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: zytrams <zytrams@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/08 20:39:00 by zytrams           #+#    #+#              #
#    Updated: 2020/01/05 01:07:34 by zytrams          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from flask import Flask
import os

qr_app = Flask(__name__)

from qr_app import qr_routes


if 'QR_URL' in os.environ:
	if 'QR_PORT' in os.environ:
		app.run(os.environ['QR_URL'], port=os.environ['QR_PORT'])
	else:
		app.run(os.environ['QR_URL'], port=8081)
else:
	if 'URL' in os.environ:
		if 'PORT' in os.environ:
			app.run(os.environ['URL'], port=str(int(os.environ['PORT']) + 1))
		else:
			app.run(os.environ['URL'], port=8081)
	else:
		app.run()
