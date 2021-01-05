#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os

os.system("sudo apt-get install figlet")
os.system("clear")
os.system("figlet IP Diversion")

def download():
	os.system("sudo git clone https://github.com/ruped24/toriptables2.git")
	os.system("sudo git clone https://github.com/ruped24/tor_ip_switcher.git")	
def setup():
	os.chdir("/opt/")
	os.system("sudo apt-get install tor -y")
	os.system("sudo service tor start")
	os.system("apt install tor python-tk")
	os.chdir("/opt/toriptables2")
	os.system("sudo python toriptables2.py -l")
	os.chdir("/opt/tor_ip_switcher")
	password=int(input("Please enter password for tor: "))
	os.system("sudo python tips_setup.py "+str(password))
	os.system("clear")
	os.system("sudo python tor_ip_switcher.py")	
def iptables_ipswitcher():
	os.chdir("/opt/")
	download()
	setup()

question=input("Have you installed before Y/N: ")
if question=="Y" or question=="y":
	setup()
		
elif question=="N" or question=="n":
	iptables_ipswitcher()
	
else:
	print("You made a wrong choice! ")
