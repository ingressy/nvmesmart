import getpass, sys, os

def main():
    if getpass.getuser() == "root":
        try:
            if sys.argv[1] == "--table" or "-t":
                try:
                    smartos = os.popen("sudo smartctl -a /dev/nvme0")
                    output = smartos.read().strip()
                    print(output)
                except:
                    print("please specify a disk | e.g. /dev/sda")
            else:
                print("Please try again! ")
        except:
            print("nvmesmart v0.1 by ingressy")
            print("Use -h or --help for Help")
    else:
        print("please run as root!")

if __name__ == "__main__":
    main()