# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    __init__.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: zytrams <zytrams@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/08 20:39:00 by zytrams           #+#    #+#              #
#    Updated: 2019/11/09 02:50:40 by zytrams          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from flask import Flask

qr_app = Flask(__name__)

from qr_app import qr_routes

if __name__ == "__main__":
	qr_app.run('localhost', port = 80)
