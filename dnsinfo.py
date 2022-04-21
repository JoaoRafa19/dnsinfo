import argparse
from fileutils import *
from os import system
from os import sys


class DNSInfo():

    def __init__(self):
        parser = argparse.ArgumentParser(description='Scan IPs from a file or from a computer and return the accessed sites and the IPs')
        parser.add_argument('-f', '--file', help='File to scan', required=False)
        parser.add_argument('-i', '--internal', help='Scan internal IPs', required=False, action='store_true' )
        parser.add_argument('--no-console', help='Do not print the output in the console', required=False, action='store_true')
        parser.add_argument('-c', '--clear', help='Clear the output directory', required=False, action='store_true')

        args = parser.parse_args()
        if args.file:
            self.fromfile(args.file, output_console= not args.no_console)
        elif args.internal:
            self.internal(output_console= not args.no_console)
        elif args.clear:
            clear_file()

        else:
            parser.print_help()


    def fromfile(self, filename, output_file='outputfile.txt', output_console=True) -> str:

        try: 
            with open(filename, 'r') as file:
                outputString = ''
                for row in file:
                    if 'Nome do registro'.upper() in row.upper():
                        try:
                            outputString+= "\n"+ row.split(':')[1]
                        except Exception as e:
                            if e is not TypeError:
                                print("Critical error in internal scan ", e)
                                sys.exit()
                            else: 
                                continue

            with open(output_file, 'w') as outputfile:
                outputfile.write(outputString)
                outputfile.close()

            if output_console:
                print(outputString)
            file.close()
            return outputString

        except:
            print("File not found")
            sys.exit()

    def internal (self, output_file=None, output_console=True):
        """
        Scan internal IPs
        """
        if not output_file:
            output_file = 'outputfile.txt'

        path = create_output_dns_file()
        systemIpInformation = system(f'ipconfig/displaydns > {path}')

        if output_console:
            print(self.fromfile(path, output_file=output_file, output_console=output_console))