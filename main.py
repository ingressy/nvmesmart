import sys, os, json, time

version = "v0.1.5"

def main():
    if os.getuid() == 0:
        #try:
            if sys.argv[1] == "--information" or sys.argv[1] == "-i":
                try:
                    smartos = os.popen("sudo smartctl -a  --json " + sys.argv[2])
                    data = smartos.read().strip()
                    prased_data = json.loads(data)

                    print("nvmesmart " + version + " by ingressy")
                    print("Model name:\t" + prased_data["model_name"])
                    print("Type:\t\t" + prased_data["device"]["type"])
                    print("Serial number:\t" + prased_data["serial_number"] + "\n")

                    print("Space:\t\t", round(prased_data["user_capacity"]["bytes"] / 1073741824, 2), "GB")
                    print("Temperature:\t", prased_data["temperature"]["current"], "°C")
                    print("Power on time:\t", prased_data["power_on_time"]["hours"],"h")
                    print("Power cycle:\t", prased_data["power_cycle_count"], "\n")

                    print("Disk Health:\t", prased_data["nvme_smart_health_information_log"]["available_spare"], "%" )
                    print("Disk reads:\t", round((prased_data["nvme_smart_health_information_log"]["data_units_read"] * prased_data["logical_block_size"]) / 1048576,2), "GB")
                    print("Disk writes:\t", round((prased_data["nvme_smart_health_information_log"]["data_units_written"] * prased_data["logical_block_size"]) / 1048576,2), "GB")
                except:
                    print("please specify a disk | e.g. /dev/sda")
            elif sys.argv[1] == "--benchmark" or sys.argv[1] == "-b":
                try:
                    speed = diskspeed(sys.argv[2])
                    speed = round(speed,2)
                    print("Disk writing speed:", speed, "Mbytes per second")
                except:
                    print("please specify a folder | e.g. /tmp/")
            elif sys.argv[1] == "--help" or sys.argv[1] == "-h":
                print("nvmesmart " + version + " by ingressy")
                print("==HELP==")
                print("-i or --information\tprint a information about your disk\n e.g nvmesmart -i /dev/sda1")
                print("-b or --benchmark\t benchmarking your disk\n e.g. nvmesmart -b /tmp/")
            else:
                print("Please try again! ")
        #except:
         #   print("nvmesmart " + version + " by ingressy")
          #  print("use --help or -h")
    else:
        print("please run with sudo permission!")

def diskspeed(dirname):
    filesize = 1  # in MB
    maxtime = 0.5  # in sec
    filename = os.path.join(dirname, 'outputTESTING.txt')
    start = time.time()
    loopcounter = 0
    while True:
        try:
            diskspeedfile(filename, filesize)
        except:
            # I have no better idea than:
            raise
        loopcounter += 1
        diff = time.time() - start
        if diff > maxtime: break
    return (loopcounter * filesize) / diff

def diskspeedfile(filename,mysizeMB):
	mystring = "The quick brown fox jumps over the lazy dog"
	writeloops = int(1000000*mysizeMB/len(mystring))
	try:
		f = open(filename, 'w')
	except:
		# no better idea than:
		raise
	for x in range(0, writeloops):
		f.write(mystring)
	f.close()
	os.remove(filename)

if __name__ == "__main__":
    main()