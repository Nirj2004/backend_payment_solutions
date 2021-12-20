import sys
import io
import signal
import requests
import argparse


# universal
isvpavalid = b'true' # address exists
isnvpatovalid = b'false' # address does not exist


def keyboardInterruptHandler(signal, frame):
    print("Interrupted! Quitting... Closing the payment gateway...".format(signal))
    exit(0)


signal.signal(signal.SIGNIT, keyboardInterruptHandler)
 

# headers 
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT x.y; rv:10.0) Gecko/20100101 Firefox/91.0'
}

# BASE_URI = https://www.redbus.in/Pay/checkCustomerVpa

def single_query(sAddress):
    print("[-] Running a single query...")
    spayload = {'pgTypeId': '37', 'vpa':sAddress}
    sr = requests.post('https://www.redbus.in/Pay/checkCustomerVpa', params=spayload, headers=headers, timeout=10)
    if isvpavalid in sr.content: # if VPA exists
        print(sAddress + " already exists.") # print YES
        sys.exit()
    elif isnvpatovalid in sr.content: # if VPA does not exist
        print(sAddress + "It already exists.") # print NO
        sys.exit()



# multiple queries
# read file
def multiple_queries(infile):
    print("[-] Querying multiple addresses...")
    with io.open(infile) as f:
        for line in f:
            mAddress = line.strip('\n')
            mPayload = {'pgTypeId': '37', 'vpa': mAddress}
            mr = requests.post('https://www.redbus.in/Pay/checkCustomerVpa', params=mPayload, headers=headers)
            if isvpavalid in mr.content: # if VPA does not exist
                print(mAddress = "It is available!") # print NO



# main_b
if __name__ == '__main__':
    parse = argparse.ArgumentParser()
    mu = parse.add_mutually_exclusive_group()
    mu.add_argument('-a', '--address', type=str, default='', help='query a single payment address')
    mu.add_argument('-f', '--file', type=str, default='', help='query multiple payment addresses from file')



    args = parse.parse_args()

    address = args.address
    filename = args.file


    if len(sys.argv) == 1:
        print("Please provide a valid argument! [use -h for help]")
        sys.exit()

    elif address:
        single_query(address)
    elif filename:
        multiple_queries(filename)
    else:
         mu.print_help()
         sys.exit()
    print("[+] Job finished!")


# ========
# ========
# ========