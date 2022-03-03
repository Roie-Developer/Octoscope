#!/usr/bin/env python3
import os # linux
import sys
import time
import logging
import argparse
import requests
import pandas
import test
""" running parameters """

try:
	#sys.path.insert(0, "/home/octoscope/octobox/stardust/pyAPI/")
	sys.path.insert(0, "/home/octoscope/Desktop/Upgrade Files/v3.4.40-rc1/octobox-v3.4.40-rc1/octobox/stardust/pyAPI/")

	from src.octobox import Octobox
except ImportError:
	sys.exit("for this script to work, it must be executed in octobox setup, bye!")

octobox = Octobox(host="127.0.0.1", port="8086")

PROFILE_MAX_DURATION = 2 * 7000  # sec
SLEEP_COUNT = 60

created_csvs = []
created_json = set()

""" setup parameters """

RESULTS_PATH = "/home/octoscope/results/"
PROFILES_BACKUP_PATH = "/home/octoscope/profiles/"

def Configuration():
	xsl_name = "Octoscope_Configuration.xlsx"
	df = pandas.read_excel(xsl_name)
	return df

data = Configuration()

def run_profile(profile_name,data,counter):
	logging.info("starting {}".format(profile_name))
	test_done = False
	start_time = time.strftime("%Y%m%d-%H%M%S")
	tt = {'name': profile_name, 'model': '', 'revision': ''}
	test_obj, read_response = octobox.throughputTest.read(tt)
	if read_response is not None:
		raise ValueError(read_response[0]["message"])
	logging.debug("test_obj: {}".format(test_obj))

	try:
		octobox.throughputTest.start(test_obj['id'])
		for check_is_running_count in range(PROFILE_MAX_DURATION):
			logging.debug("checking whether {} is still running".format(profile_name))
			if not octobox.throughputTest.isTestRunning(test_obj)[0]:
				test_done = True
				print('Out  of profile loop')
				break
			# TODO: show progressbar according to testDuration? (is it the same as calculated duration?)
			# sys.stdout.write('In run_profile #1:\n . ')
			# sys.stdout.flush()
			print("Entering sleeping count in run_profile for 60s")
			time.sleep(SLEEP_COUNT)
		if test_done:
			logging.info("{} - finished".format(profile_name))
		else:
			raise RuntimeError("{} has exceeded {} seconds!".format(profile_name, PROFILE_MAX_DURATION))
	except:
		raise RuntimeError("Exception while profile {} is running".format(profile_name))

	logging.info("generating CSV of: {}".format(profile_name))
	csv_url = octobox.throughputTest.getCSV(test_obj)[0]['href']
	# logging.info(f"\nThis is test throughput from running_profile \n {octobox.throughputTest.getCSV(test_obj)}")
	os.makedirs(name=RESULTS_PATH, mode=755, exist_ok=True)
	csv_path = os.path.join(RESULTS_PATH, profile_name + '_' + str(data.Channel[counter]) + '_' + str(data.STREAMS[counter]) + '_' + str(data.BANDWIDTH[counter]) + '_' + start_time + ".csv")
	json_path = os.path.join(RESULTS_PATH, profile_name + '_' + str(data.Channel[counter]) + '_' + str(data.STREAMS[counter]) + '_' + str(data.BANDWIDTH[counter]) + '_' + start_time + ".json")
	logging.info("saving CSV to {}".format(csv_path))
	with open(csv_path, "w+", newline= "") as file:
		file.write(requests.get(csv_url).text)
		# file.write("*****************************")
	created_csvs.append(csv_path)
	# Start - Added by Roie Turgeman
	parsing_data = test.ParsingToJson(csv_path,json_path)
	parsing_data.parse()
	logging.info("Parsing to json is finished")
	# End

def run(profiles, repeat=1):
	os.makedirs(name=RESULTS_PATH, mode=755, exist_ok=True)

	#  TODO: go over profiles and try to read them before starting
	#  and check whether any of them (or any at all?) is running
	#  use class for running a profile with read/check as first step

	if repeat == 1:
		logging.info("In octo run#1: running {}".format(profiles))
	else:
		logging.info("running {} {} times".format(profiles, repeat))
	for repeat_count in range(1, repeat+1):
		if repeat > 1:
			logging.info("repeat count: #{}".format(repeat_count))
		for profile_count, profile in enumerate(profiles):
			if data.Client[profile_count]=="PAL6":
				logging.info("PAL6")
				Pal6_Config(profile_count,profile,data)
			elif data.Client[profile_count]=="PAL5":
				logging.info("PAL5")
				Pal5_Config(profile_count, data)
			elif data.Client[profile_count] == "PAL24":
				logging.info("PAL24")
				Pal24_Config(profile_count, data)
			logging.info("running profile")
			run_profile(profile,data,profile_count)
			if profile_count < len(profiles):
				logging.info("Sleeping 60 seconds".format(SLEEP_COUNT))
				logging.info(f"Sleeping started {time.time()}")
				# for sleep_second in range(SLEEP_COUNT):
					# if sleep_second % 20 == 0:
						# sys.stdout.write('In octo run2:. \n')
						# sys.stdout.flush()
				time.sleep(SLEEP_COUNT)
				logging.info(f"Sleeping finished at {time.time()}")
	logging.info("CSV files created:\n{}".format('\n'.join([csv for csv in created_csvs])))



def get_parser(parser=argparse.ArgumentParser(prog='octo')):
	# TODO: find profiles' location (might need another script)
	parser.description = "octo.py script arguments"
	parser.formatter_class = argparse.RawTextHelpFormatter
	parser.add_argument("profiles", nargs='+', help="profile(s) to execute separated by \',\'")
	parser.add_argument("--repeat", '-r', type=int, help="number of executions to repeat", default=1)
	parser.add_argument("--verbose", '-v', action="store_true", help="verbosity on")
	return parser

def main():
	parser = get_parser()
	args = parser.parse_args()
	log_level = logging.DEBUG if args.verbose else logging.INFO
	logging.basicConfig(format='%(levelname)s: %(message)s', level=log_level)
	run(profiles=args.profiles, repeat=int(args.repeat))

def Pal24_Config(index,data):
	UNSET = "UNSET"
	scriptName = __file__
	ip = UNSET
	radiosetup_url = UNSET
	radiostatus_url = UNSET
	status_url = UNSET


	REST_TIMEOUT = 30

	def checkResponse(resp):
		if (resp.ok):
			print("    Successful")
		else:
			# If response code is not ok (200), print the resulting http error code with description
			resp.raise_for_status()

	dictofRadioSetupSTA = {
		"mode": "octopal",
		"radioMode": "station",
		"stationNum": 1,
		"interface": "ac",
		"channelWidth": int(data.BANDWIDTH[index]),
		"primaryChannel": int(data.Channel[index]),
		"guardInterval": "short",
		"rate": -1,
		"streams": int(data.STREAMS[index]),
		"priority": "bestEffort",
		"ssid": str(data.SSID.values.tolist()[index]),
		"securityProtocol": str(data.Security.values.tolist()[index]),
		"password": str(int(data.Password.values.tolist()[index])),
		"ipMode": 0,
		"ipAddress": "192.168.1.90",
		"subnetMask": "255.255.255.0",
		"enable_pbssid": False
	}

	ip = '169.254.26.7'
	radiosetup_url = "http://" + ip + "/api/radiosetup"
	radiostatus_url = "http://" + ip + "/api/radiostatus"
	status_url = "http://" + ip + "/api/status"
	stationlist_url = "http://" + ip + "/api/stationlist"

	myResponse = requests.put(radiosetup_url, json=dictofRadioSetupSTA, timeout=REST_TIMEOUT)
	checkResponse(myResponse)


def Pal5_Config(index,data):
	UNSET = "UNSET"
	scriptName = __file__
	ip = UNSET
	radiosetup_url = UNSET
	radiostatus_url = UNSET
	status_url = UNSET


	REST_TIMEOUT = 30

	def checkResponse(resp):
		if (resp.ok):
			print("    Successful")
		else:
			# If response code is not ok (200), print the resulting http error code with description
			resp.raise_for_status()

	dictofRadioSetupSTA = {
		"mode": "octopal",
		"radioMode": "station",
		"stationNum": 1,
		"interface": "ac",
		"channelWidth": int(data.BANDWIDTH[index]),
		"primaryChannel": int(data.Channel[index]),
		"guardInterval": "short",
		"rate": -1,
		"streams": int(data.STREAMS[index]),
		"priority": "bestEffort",
		"ssid": str(data.SSID.values.tolist()[index]),
		"securityProtocol": str(data.Security.values.tolist()[index]),
		"password": str(int(data.Password.values.tolist()[index])),
		"ipMode": 0,
		"ipAddress": "192.168.1.25",
		"subnetMask": "255.255.255.0",
		"enable_pbssid": False
	}

	ip = '169.254.26.5'
	radiosetup_url = "http://" + ip + "/api/radiosetup"
	radiostatus_url = "http://" + ip + "/api/radiostatus"
	status_url = "http://" + ip + "/api/status"
	stationlist_url = "http://" + ip + "/api/stationlist"

	myResponse = requests.put(radiosetup_url, json=dictofRadioSetupSTA, timeout=REST_TIMEOUT)
	checkResponse(myResponse)

def Pal6_Config(index,profile,data):
	try:
		sys.path.insert(0, "/home/octoscope/Desktop/Upgrade Files/v3.4.40-rc1/octobox-v3.4.40-rc1/octobox/stardust/pyAPI/")
		from octobox import Octobox

	except ImportError:
		sys.exit("for this script to work, it must be executed in octobox setup, bye!")
	octobox = Octobox(host="127.0.0.1", port="8086")
	tt = {'name': profile, 'revision': '', 'model': ''}
	test, errors = octobox.throughputTest.read(tt)
	testId = test['id']
	if data.RADIO_TYPE[index] == "RADIO_24":
		ipaddress="192.168.1.27"
	else:
		ipaddress = "192.168.1.28"
	from_, errors = octobox.endpoint.readByAddress(ipaddress)
	print(errors)



# pal6 = {
# "testId": testId,
# "endpoint": from_["id"],
# "ipAddress": "192.168.1.105",
# "primaryChannel": 6,
# "bandwidth": "BANDWIDTH_40_ADAPT",     #BANDWIDTH_20_FIXED,BANDWIDTH_40_ADAPT,BANDWIDTH_80_ADAPT,BANDWIDTH_160_ADAPT
# "apStaMode": "MODE_STA",
# "ssid": "MG_2.4G",
# "palRadio": "RADIO_24",               #RADIO_24,RADIO_5
# "streams": 2,                         #1,2,3,4
# "interface":"INTERFACE_AX"           #INTERFACE_B,INTERFACE_G,INTERFACE_A,INTERFACE_N,INTERFACE_AC,INTERFACE_AX
#     }


	pal6 = {
		"testId": testId,
		"endpoint": from_["id"],
		"ipAddress":ipaddress,
		"primaryChannel": int(data.Channel[index]),
		"bandwidth": str(data.BANDWIDTH.values.tolist()[index]),		# BANDWIDTH_20_FIXED,BANDWIDTH_40_ADAPT,BANDWIDTH_80_ADAPT,BANDWIDTH_160_ADAPT
		"apStaMode": 'MODE_STA',
		"ssid": str(data.SSID.values.tolist()[index]),
		"palRadio": str(data.RADIO_TYPE.values.tolist()[index]),  # RADIO_24,RADIO_5
		"streams": int(data.STREAMS[index]),  # 1,2,3,4
		"security":str(data.Security.values.tolist()[index]),      # SECURITY_WPA2,SECURITY_NONE
		"password":str(int(data.Password.values.tolist()[index])),
		"interface": str(data.WIFi_INTERFACE.values.tolist()[index])     #INTERFACE_B,INTERFACE_G,INTERFACE_A,INTERFACE_N,INTERFACE_AC,INTERFACE_AX
	}

	#deleted, errors = octobox.pal6Config.remove(pal6)
	pal6, errors = octobox.pal6Config.updateByEP(pal6)
	print(errors)
	push, errors = octobox.pal6Config.pushOne(pal6)
	print(errors)
	time.sleep(100)

if __name__ == "__main__": main()
