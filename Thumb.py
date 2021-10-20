import ssl
import argparse
import OpenSSL
parser=argparse.ArgumentParser(description='Process args for Host')
parser.add_argument('-i', type=str, dest='ip', required=True)
parser.add_argument('-o', type=int ,dest="port", required=False, default=443)
args=parser.parse_args()

addr = (args.ip, args.port)
pem = ssl.get_server_certificate(addr)

thumbprint = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, pem)
bigprint = thumbprint.digest('sha1')


print(bigprint)
