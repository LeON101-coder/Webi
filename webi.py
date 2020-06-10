#!/bin/usr/Python3.7.x | 3.8 x
# coding=utf-8

# Webi tools simple Website Information and File Uploader
# Just for Penetration Testing

import os, sys
from time import sleep
try:
	import requests
except:
	os.system('pip install requests')


class Main: # Main
	def __init__(self):
		self.Webi()
	
	def Webi(self):
		os.system('clear') # Clear Screen
		print("""

  ___ ___         __     __
 |   Y   |.-----.|  |--.|__|
 |.  |   ||  -__||  _  ||  |
 |. / \  ||_____||_____||__|
 |:      |
 |::.|:. | /Coded by : HurtSec
 `--- ---'""")
		print("""
 01. Whois
 02. Subnet Calculator
 03. Nmap Scan Port
 04. GeoIP lookup
 05. DNS Lookup
 06. Ping
 07. Admin Login Finder
 08. Shell Uploader Finder
 09. Scan Subdomain
 10. File Uploader
 11. Check vuln Upload File
 12. Exit the programs
		""")
		while True:
			try:
				self.WeBi = input("@wEBi > ")
				if self.WeBi in ['01', '1']:
					try:
						print("")
						self.Target = input("• Target Domain > ")
						self.Res = requests.get('http://api.hackertarget.com/whois/?q={}'.format(self.Target)).text
						print(58*"-")
						print("Result Whois Lookup : {}\n\n{}".format(self.Target, self.Res))
						print(58*"-")
					except requests.exceptions.ConnectionError:
						exit("No Connection")
				elif self.WeBi in ['02', '2']:
					try:
						print("")
						self.Target("• Target Domain > ")
						self.Res = requests.get('http://api.hackertarget.com/subnetcalc/?q={}'.format(self.Target)).text
						print(58*"-")
						print("Result Subnet Calculator : {}\n\n{}".format(self.Target, self.Res))
						print(58*"-")
					except requests.exceptions.ConnectionError:
						exit("No Connection")
				elif self.WeBi in ['03', '3']:
					try:
						print("")
						self.Target("• Target Domain > ")
						self.Res = requests.get('http://api.hackertarget.com/nmap/?q={}'.format(self.Target)).text
						print(58*"-")
						print("Result Nmap Port Scanner : {}\n\n{}".format(self.Target, self.Res))
						print(58*"-")
					except requests.exceptions.ConnectionError:
						exit("No Connection")
				elif self.WeBi in ['04', '4']:
					try:
						print("")
						self.Target("• Target Domain > ")
						self.Res = requests.get('http://api.hackertarget.com/geoip/?q={}'.format(self.Target)).text
						print(58*"-")
						print("Result Geo IP Lookup : {}\n\n{}".format(self.Target, self.Res))
						print(58*"-")
					except requests.exceptions.ConnectionError:
						exit("No Connection")
				elif self.WeBi in ['05', '5']:
					try:
						print("")
						self.Target("• Target Domain > ")
						self.Res = requests.get('http://api.hackertarget.com/dnslookup/?q={}'.format(self.Target)).text
						print(58*"-")
						print("Result DNS Lookup : {}\n\n{}".format(self.Target, self.Res))
						print(58*"-")
					except requests.exceptions.ConnectionError:
						exit("No Connection")
				elif self.WeBi in ['06', '6']:
					try:
						print("")
						self.Target("• Target Domain > ")
						self.Res = requests.get('http://api.hackertarget.com/nping/?q={}'.format(self.Target)).text
						print(58*"-")
						print("Result Ping : {}\n\n{}".format(self.Target, self.Res))
						print(58*"-")
					except requests.exceptions.ConnectionError:
						exit("No Connection")
				elif self.WeBi in ['07', '7']:
					Ask = input("\n• Target Domain > ")
					Asks = input("• A for 'https' B for 'http' > ")
					print("")
					if Asks in ['A', 'a']:
						site = 'https://{}'.format(Ask)
					elif Asks in ['B', 'b']:
						site = 'http://{}'.format(Ask)
					self.Admin_Panel = ['/login',
										'/login.php',
										'/admin',
										'/admin.php',
										'/administrator',
										'/administrator.php',
										'/admin/login',
										'/masuk',
										'/masuk.php',
										'/html/admin',
										'/html/admin.php',
										'/html/administrator',
										'/html/administrator.php',
										]
					try:
						for Admin in self.Admin_Panel:
							self.Res = requests.get(site+Admin)
							if self.Res.status_code == 404:
								print(":404 ---> {}{}".format(site,Admin))
							elif self.Res.status_code == 200:
								print(":Found ---> {}{}".format(site,Admin))
						
						print("\nFinish")
						input("Enter")
						Main()
					except (EOFError, KeyboardInterrupt):
						exit("Stopped")
				elif self.WeBi in ['08', '8']:
					Ask = input("\n• Target Domain > ")
					Asks = input("• A for 'https' B for 'http' > ")
					print("")
					if Asks in ['A', 'a']:
						site = 'https://{}'.format(Ask)
					elif Asks in ['B', 'b']:
						site = 'http://{}'.format(Ask)
					
					ShellList = ['/up.php',
									'/upload.php',
									'/up',
									'/upload',
									'/site/upload',
									'/site/up',
									'/site/upload.php',
									'/uploader',
									'/uploader.php',
								]
					try:
						for shell in ShellList:
							self.Res = requests.get(site,shell)
							if self.Res.status_code == 404:
								print(":404 ---> {}{}".format(site,shell))
							elif self.Res.status_code == 200:
								print("Found ---> {}{}".format(site,shell))
						
						print("Finish")
						input("Enter")
						Main()
					except (KeyboardInterrupt, EOFError):
						exit("Stopped")
				elif self.WeBi in ['09', '9']:
					try:
						print("")
						self.Target = input("• Target Domain > ")
						self.Res = requests.get('http://api.hackertarget.com/hostsearch/?q={}'.format(self.Target)).text
						print(58*"-")
						print("Result Subdomain Scanner : {}\n\n{}".format(self.Target, self.Res))
						print(58*"-")
					except requests.exceptions.ConnectionError:
						exit("No Connection")
				elif self.WeBi in ['10']:
					try:
						print("")
						self.Target = input("• Target Domain > ")
						self.Ask = input("• A for 'https' B for 'http' > ")
						if self.Ask in ['A', 'a']:
							site = 'https://{}'.format(self.Target)
						elif self.Ask in ['B', 'b']:
							site = 'http://{}'.format(self.Target)
						self.Shell = input("• File Upload (Ex.: shell.html) > ")
						Op = open(self.Shell).read()
						self.Up = requests.put("{}/{}, data={}".format(site, self.Shell, Op))
						if self.Up.status_code < 200 or self.Up.status_code >= 250:
							print("\nCan't Upload file, be the target not Vuln")
						else:
							print("\nSuccess ---> {}/{}".format(site,self.Shell))
							input("Enter")
							Main()
					except IOError:
						print("Shell file '{}' not found".format(self.Shell))
				elif self.WeBi in ['11']:
					try:
						print("")
						self.Target = input("• Target Domain > ")
						self.Ask = input("• A for 'https' B for 'http' > ")
						if self.Ask in ['A', 'a']:
							site = 'https://{}'.format(self.Target)
						elif self.Ask in ['B', 'b']:
							site = 'http://{}'.format(self.Target)
						Op = 'sample.html'
						Ops = open(Op).read()
						self.Res = requests.put('{}/{}, data={}'.format(site,Op,Ops))
						if self.Res.status_code < 200 or self.Res.status_code >= 250:
							print("\nNot Vuln File Uploader")
						else:
							print("\nThe website '{}' vuln file Uploader".format(site))
					except IOError:
						exit("404")
				elif self.WeBi in ['12']:
					exit("\nExit the programs")
				else:
					print("Enter the number please")
					
			except (KeyboardInterrupt, EOFError):
				exit("Stopped")

if __name__=='__main__':
	if sys.version[0] in '2':
		exit("Please using python3.x.x")
	
	Main()
