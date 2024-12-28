import sys, os, json

version = "v0.1.4"

def main():
    if os.getuid() == 0:
        try:
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
            elif sys.argv[1] == "--help" or sys.argv[1] == "-h":
                print("nvmesmart " + version + " by ingressy")
                print("==HELP==")
                print("-i or --information\tprint a information about your disk\n e.g nvmesmart -i /dev/sda1")
            else:
                print("Please try again! ")
        except:
            print("nvmesmart " + version + " by ingressy")
            print("use --help or -h")
    else:
        print("please run with sudo permission!")

if __name__ == "__main__":
    main()