try:
	import requests
	from bs4 import BeautifulSoup
	import threading
	import os
	import sys
	import time
	from colorama import Fore, Style
	from user_agent import *
	from asciistuff import Banner
except Exception as e:
	print(e)

os.system("clear")

print(Fore.BLUE + Style.BRIGHT + str(Banner("XSS FREAK")))

wlcm_msg = (Fore.RED + Style.BRIGHT + ">> [+] Give Me A Target To Destroy\n")

for char in wlcm_msg:
	time.sleep(0.06)
	sys.stdout.write(char)
	sys.stdout.flush()

links = []
special_links = []
special_links_2 = []
independent_links = []
directories = []
vulnerable_inputs = []
forms = []
inputs = []
host = input(Fore.CYAN + Style.BRIGHT + ">> [?] Enter Target: ")
try:
	file = input(Fore.CYAN + Style.BRIGHT + ">> [*] Enter File Containing XSS Payloads to Try: ")
	read_file = open(file, "r").readlines()
	pass
except Exception:
	print(Fore.RED + Style.BRIGHT + ">> [!] Selected File Doesn't Exist, Goodbye")
	sys.exit()

print(Fore.BLUE + Style.BRIGHT + ">> [*] Searching Target For Possible Links And Directories")

def find_directories():
	try:
		user_agent = generate_user_agent()
		headers = {
			"User-Agent" : user_agent
		}
		response = requests.get(host, headers=headers)
		content = response.text
		soup = BeautifulSoup(content, "html5lib")
		scrape_links = soup.find_all("a")
		for i in scrape_links:
			try:
				if(i['href'][0] == "/" and i['href'][-1] == "/" and i['href'].startswith("//") == False and i['href'].endswith("//") == False):
					directories.append(i['href'])
				else:
					pass
			except KeyError:
				pass
	except requests.exceptions.ConnectionError:
		pass

def find_links():
	try:
		user_agent = generate_user_agent()
		headers = {
			"User-Agent" : user_agent
		}
		response = requests.get(host, headers=headers)
		content = response.text
		soup = BeautifulSoup(content, "html5lib")
		scrape_links = soup.find_all("a")
		for i in scrape_links:
			try:
				if(host in i['href']):
					independent_links.append(i['href'])
					pass
				if(i['href'][0] != "/" and i['href'][-1] == "/" and i['href'].startswith("https") == False and i['href'].startswith("http") == False):
					special_links.append(i['href'])
					pass
				if(i['href'].startswith("//") == False and i['href'][0] == "/" and i['href'][-1] != "/" and i['href'].startswith("http") == False and i['href'].startswith("https") == False and i['href'].startswith("www.") == False and i['href'].startswith("mailto") == False):
					links.append(i['href'])
					pass
				if(i['href'].startswith("/") == False and i['href'].endswith("/") == False and i['href'].startswith("https") == False and i['href'].startswith("http") == False):
					special_links_2.append(i['href'])
					pass
				else:
					pass
			except KeyError:
				pass
	except requests.exceptions.ConnectionError:
		pass


find_directories()
find_links()

def navigate_directories():
	try:
		user_agent = generate_user_agent()
		headers = {
			"User-Agent" : user_agent
		}
		r = requests.get(str(host) + str(dir), headers=headers)
		content = r.text
		soup = BeautifulSoup(content, "html5lib")
		scrape_links = soup.find_all("a")
		for i in scrape_links:
			try:
				if(host in i['href']):
					independent_links.append(i['href'])
					pass
				if(i['href'][0] != "/" and i['href'][-1] == "/" and i['href'].startswith("https") == False and i['href'].startswith("http") == False):
					special_links.append(i['href'])
					pass
				if(i['href'].startswith("//") == False and i['href'][0] == "/" and i['href'][-1] != "/" and i['href'].startswith("http") == False and i['href'].startswith("https") == False and i['href'].startswith("www.") == False and i['href'].startswith("mailto") == False):
					links.append(i['href'])
					pass
				if(i['href'].startswith("/") == False and i['href'].endswith("/") == False and i['href'].startswith("https") == False and i['href'].startswith("http") == False):
					special_links_2.append(i['href'])
					pass
				else:
					pass
			except KeyError:
				pass
	except requests.exceptions.ConnectionError:
		pass


def search_inputs_links():
	try:
		user_agent = generate_user_agent()
		headers = {
			"User-Agent" : user_agent
		}
		r = requests.get(str(host) + str(link), headers=headers)
		content = r.text
		soup = BeautifulSoup(content, "html5lib")
		scrape_links = soup.find_all("input")
		for i in scrape_links:
			try:
				inputs.append(i['name'])
				pass
			except KeyError:
				pass
	except requests.exceptions.ConnectionError:
			pass

def search_inputs_special_links():
	try:
		user_agent = generate_user_agent()
		headers = {
			"User-Agent" : user_agent
		}
		r = requests.get(str(host) + "/" +  str(sl), headers=headers)
		content = r.text
		soup = BeautifulSoup(content, "html5lib")
		scrape_links = soup.find_all("input")
		for i in scrape_links:
			try:
				inputs.append(i['name'])
				pass
			except KeyError:
				pass
	except requests.exceptions.ConnectionError:
		pass

def search_inputs_special_links_2():
	try:
		user_agent = generate_user_agent()
		headers = {
			"User-Agent" : user_agent
		}
		r = requests.get(str(host) + "/" + str(sl2), headers=headers)
		content = r.text
		soup = BeautifulSoup(content, "html5lib")
		scrape_links = soup.find_all("input")
		for i in scrape_links:
			try:
				inputs.append(i['name'])
				pass
			except KeyError:
				pass
	except requests.exceptions.ConnectionError:
		pass

def search_inputs_independent_links():
	try:
		user_agent = generate_user_agent()
		headers = {
			"User-Agent" : user_agent
		}
		r = requests.get(str(il), headers=headers)
		content = r.text
		soup = BeautifulSoup(content, "html5lib")
		scrape_links = soup.find_all("input")
		for i in scrape_links:
			try:
				inputs.append(i['name'])
				pass
			except KeyError:
				pass
	except requests.exceptions.ConnectionError:
		pass

def asses_vulnerability_links():
	try:
		for input_set in inputs_set:
			for payload in read_file:
				user_agent = generate_user_agent()
				headers = {
					"User-Agent" : user_agent
				}
				response_object = requests.get(str(host) + str(link) + "?" + str(input_set) + "=" + str(payload), headers=headers)
				content = response_object.text
				if(payload in content):
					vulnerable_inputs.append(input_set)
					pass
				else:
					pass
	except requests.exceptions.ConnectionError:
		pass

def asses_vulnerability_special_links():
	try:
		for input_set in inputs_set:
			for payload in read_file:
				user_agent = generate_user_agent()
				headers = {
					"User-Agent" : user_agent
				}
				response_object = requests.get(str(host) + "/" +  str(special_link) + "?" + str(input_set) + "=" + str(payload), headers=headers)
				content = response_object.text
				if(payload in content):
					vulnerable_inputs.append(input_set)
				else:
					pass
	except requests.exceptions.ConnectionError:
		pass

def asses_vulnerability_special_links_2():
	try:
		for input_set in inputs_set:
			for payload in read_file:
				response_object = requests.get(str(host) + "/" +  str(special_link_2) + "?" + str(input_set) + "=" + str(payload))
				content = response_object.text
				if(payload in content):
					vulnerable_inputs.append(input_set)
					pass
				else:
					pass
	except requests.exceptions.ConnectionError:
		pass

def asses_vulnerability_independent_links():
        try:
                for input_set in inputs_set:
                        for payload in read_file:
                                response_object = requests.get(str(independent_link) + "?" + str(input_set) + "=" + str(payload))
                                content = response_object.text
                                if(payload in content):
                                        vulnerable_inputs.append(input_set)
                                        pass
                                else:
                                        pass
        except requests.exceptions.ConnectionError:
                pass


all_links = (links + special_links + special_links_2 + independent_links)


if(len(directories) == 0 and len(all_links) != 0):
	print(Fore.GREEN + Style.BRIGHT + ">> [+] " + str(len(all_links)) + " Links Have Been Found")
	print(Fore.RED + Style.BRIGHT + ">> [!] No Directories Have Been Found")
	print(Fore.BLUE + Style.BRIGHT + ">> [*] I Will Sleep For 5 Minutes And My Threads Will Initialize Now And Search Each Link For HTML Inputs. Cross Your Fingers")
	try:
		for link in links:
			t = threading.Thread(target=search_inputs_links)
			time.sleep(1)
			t.start()
		time.sleep(10)
		for sl in special_links:
			s = threading.Thread(target=search_inputs_special_links)
			time.sleep(1)
			s.start()
		time.sleep(10)
		for sl2 in special_links_2:
			c = threading.Thread(target=search_inputs_special_links_2)
			time.sleep(1)
			c.start()
		time.sleep(10)
		for il in independent_links:
			m = threading.Thread(target=search_inputs_independent_links)
			time.sleep(1)
			m.start()
	except Exception:
		pass
	time.sleep(60)
	inputs_set = set(inputs)
	print(Fore.GREEN + Style.BRIGHT + ">> [+] My Threads Have Done Working And The Total Amount Of Inputs Found On All Possible Webpages Is: " + str(len(inputs_set)))
	print(Fore.BLUE + Style.BRIGHT + ">> [*] I Will Launch A Bunch Of XSS Payloads Towards The Target With The Use Of Multithreading For Efficiency. Hope For The Best")
	print(Fore.BLUE + Style.BRIGHT + ">> [*] Note: It Might Take A Lot Of Time Depending On Your Internet Speed, Amount of Links and Inputs, And Your Processing Power")
	try:
		for link in links:
			o = threading.Thread(target=asses_vulnerability_links)
			o.start()
		time.sleep(60)
		for special_link in special_links:
			z = threading.Thread(target=asses_vulnerability_special_links)
			z.start()
		time.sleep(60)
		for special_link_2 in special_links_2:
			v = threading.Thread(target=asses_vulnerability_special_links_2)
			v.start()
		time.sleep(60)
		for independent_link in independent_links: #Corrected dependent_link to *independant_links* @XXSRAT You're awesome brother!
			q = threading.Thread(target=asses_vulnerability_independent_links)
			q.start()
		time.sleep(60)
		set_vulnerable_inputs = set(vulnerable_inputs)
		if(len(set_vulnerable_inputs) == 0):
			print(Fore.RED + Style.BRIGHT + ">> No INPUTS Are Vulnerable To XSS Attacks. Try Changing Your Payloads Or Choose Another Target. SEE YA")
		else:
			print(Fore.GREEN + Style.BRIGHT + ">> [+] Vulnerable Inputs Were Found Successfully")
			for vulnerable_input in set_vulnerable_inputs:
				print(Fore.GREEN + Style.BRIGHT + ">> [+] Vulnerable Input ==> " + str(vulnerable_input))
			print(Fore.CYAN + Style.BRIGHT + ">> [+] Go XSS'em Boi")
	except Exception:
		pass

if(len(directories) != 0 and (all_links) != 0):
	print(Fore.GREEN + Style.BRIGHT + ">> [+] " + str(len(all_links)) + " Links Have Been Found")
	print(Fore.GREEN + Style.BRIGHT + ">> [+] " + str(len(directories)) + " Directories Have Been Found")
	print(Fore.BLUE + Style.BRIGHT + ">> [*] Since There Was Directories Found, I Will Navigate To Them And Search For Possible Links To Add To Our Attack Scope")
	print(Fore.CYAN + Style.BRIGHT + ">> [*] Note: I Will Sleep Now For A Minute And Let My Threads Do The Work Faster For You, See Ya")
	for dir in directories:
		t = threading.Thread(target=navigate_directories)
		t.start()
	time.sleep(60)
	total_links = (links + special_links + special_links_2 + independent_links)
	print(Fore.GREEN + Style.BRIGHT + ">> [+] After Extensive Search In The Directories, The New Total Amount Of Links Is: " + str(len(total_links)))
	print(Fore.CYAN + Style.BRIGHT + ">> [*] Now We Have Gathered All Possible Links From All The Website, It Is Time Now To Start Looking For INPUTS") 
	print(Fore.BLUE + Style.BRIGHT + ">> [*] I Will Sleep For 5 Minutes And My Threads Will Initialize Now And Search Each Link For HTML Inputs. Cross Your Fingers")
	try:
		for link in links:
			t = threading.Thread(target=search_inputs_links)
			time.sleep(1)
			t.start()
		time.sleep(10)
		for sl in special_links:
			s = threading.Thread(target=search_inputs_special_links)
			time.sleep(1)
			s.start()
		time.sleep(10)
		for sl2 in special_links_2:
			c = threading.Thread(target=search_inputs_special_links_2)
			time.sleep(1)
			c.start()
		time.sleep(10)
		for il in independent_links:
			m = threading.Thread(target=search_inputs_independent_links)
			time.sleep(1)
			m.start()
	except Exception:
		pass
	time.sleep(60)
	inputs_set = set(inputs)
	print(Fore.GREEN + Style.BRIGHT + ">> [+] My Threads Have Done Working And The Total Amount Of Inputs Found On All Possible Webpages Is: " + str(len(inputs_set)))
	print(Fore.BLUE + Style.BRIGHT + ">> [*] I Will Launch A Bunch Of XSS Payloads Towards The Target With The Use Of Multithreading For Efficiency. Hope For The Best")
	print(Fore.BLUE + Style.BRIGHT + ">> [*] Note: It Might Take A Lot Of Time Depending On Your Internet Speed, Amount of Links and Inputs, And Your Processing Power")
	try:
		for link in links:
			o = threading.Thread(target=asses_vulnerability_links)
			o.start()
		time.sleep(60)
		for special_link in special_links:
			z = threading.Thread(target=asses_vulnerability_special_links)
			z.start()
		time.sleep(60)
		for special_link_2 in special_links_2:
			v = threading.Thread(target=asses_vulnerability_special_links_2)
			v.start()
		time.sleep(60)
		for independent_link in independent_links:
			r = threading.Thread(target=asses_vulnerability_independent_links)
			r.start()
		time.sleep(180)
		set_vulnerable_inputs = set(vulnerable_inputs)
		if(len(set_vulnerable_inputs) == 0):
			print(Fore.RED + Style.BRIGHT + ">> No INPUTS Are Vulnerable To XSS Attacks. Try Changing Your Payloads Or Choose Another Target. SEE YA")
		else:
			print(Fore.GREEN + Style.BRIGHT + ">> [+] Vulnerable Inputs Were Found Successfully")
			for vulnerable_input in set_vulnerable_inputs:
				print(Fore.GREEN + Style.BRIGHT + ">> [+] Vulnerable Input ==> " + str(vulnerable_input))
			print(Fore.CYAN + Style.BRIGHT + ">> [+] Go XSS'em Boi")
	except Exception:
		pass





if(len(directories) != 0 and (all_links) == 0):
	print(Fore.RED + Style.BRIGHT + ">> [!] No Links Have Been Found")
	print(Fore.GREEN + Style.BRIGHT + ">> [+] " + str(len(directories)) + " Directories Have Been Found")
	print(Fore.BLUE + Style.BRIGHT + ">> [*] Since There Was Directories Found, I Will Navigate To Them And Search For Possible Links To Add To Our Attack Scope")
	print(Fore.CYAN + Style.BRIGHT + ">> [*] Note: I Will Sleep Now For A Minute And Let My Threads Do The Work Faster For You, See Ya")
	for dir in directories:
		t = threading.Thread(target=navigate_directories)
		t.start()
	time.sleep(60)
	total_linkss = (links + special_links + special_links_2 + independent_links)
	print(Fore.GREEN + Style.BRIGHT + ">> After Extensive Search In The Directories, The New Total Of Links Is: " +  str(len(total_linkss)))
	if(len(total_links) == 0):
		print(Fore.RED + Style.BRIGHT + ">> [!] No Links Were Detected At All, So I Have To Go So Goodbye")
	else:
		print(Fore.CYAN + Style.BRIGHT + ">> [*] Now We Have Gathered All Possible Links From All The Website, It Is Time Now To Start Looking For INPUTS") 
		print(Fore.BLUE + Style.BRIGHT + ">> [*] I Will Sleep For 5 Minutes And My Threads Will Initialize Now And Search Each Link For HTML Inputs. Cross Your Fingers")
	try:
		for link in links:
			t = threading.Thread(target=search_inputs_links)
			time.sleep(1)
			t.start()
		time.sleep(10)
		for sl in special_links:
			s = threading.Thread(target=search_inputs_special_links)
			time.sleep(1)
			s.start()
		time.sleep(10)
		for sl2 in special_links_2:
			c = threading.Thread(target=search_inputs_special_links_2)
			time.sleep(1)
			c.start()
		time.sleep(10)
		for il in independent_links:
			m = threading.Thread(target=search_inputs_independent_links)
			time.sleep(1)
			m.start()
	except Exception:
		pass
	time.sleep(60)
	inputs_set = set(inputs)
	print(Fore.GREEN + Style.BRIGHT + ">> [+] My Threads Have Done Working And The Total Amount Of Inputs Found On All Possible Webpages Is: " + str(len(inputs_set)))
	print(Fore.BLUE + Style.BRIGHT + ">> [*] I Will Launch A Bunch Of XSS Payloads Towards The Target With The Use Of Multithreading For Efficiency. Hope For The Best")
	print(Fore.BLUE + Style.BRIGHT + ">> [*] Note: It Might Take A Lot Of Time Depending On Your Internet Speed, Amount of Links and Inputs, And Your Processing Power")
	try:
		for link in links:
			o = threading.Thread(target=asses_vulnerability_links)
			o.start()
		time.sleep(60)
		for special_link in special_links:
			z = threading.Thread(target=asses_vulnerability_special_links)
			z.start()
		time.sleep(60)
		for special_link_2 in special_links_2:
			v = threading.Thread(target=asses_vulnerability_special_links_2)
			v.start()
		time.sleep(60)
		for independent_link in independent_links:
			y = threading.Thread(target=asses_vulnerability_independent_links)
			y.start()
		time.sleep(180)
		set_vulnerable_inputs = set(vulnerable_inputs)
		if(len(set_vulnerable_inputs) == 0):
			print(Fore.RED + Style.BRIGHT + ">> No INPUTS Are Vulnerable To XSS Attacks. Try Changing Your Payloads Or Choose Another Target. SEE YA")
		else:
			print(Fore.GREEN + Style.BRIGHT + ">> [+] Vulnerable Inputs Were Found Successfully")
			for vulnerable_input in set_vulnerable_inputs:
				print(Fore.GREEN + Style.BRIGHT + ">> [+] Vulnerable Input ==> " + str(vulnerable_input))
			print(Fore.CYAN + Style.BRIGHT + ">> [+] Go XSS'em Boi")
	except Exception:
		pass


if(len(directories) == 0 and (all_links) == 0):
	print(Fore.RED + Style.BRIGHT + ">> [!] As Far As My Search Went, Your Target Doesn't Have Any Linked Links Or Directories Inside Their HTML Code")
	sys.exit()
	pass

else:
	pass



