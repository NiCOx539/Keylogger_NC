# This installs two files, app.exe and logo.ico, creates a start menu shortcut, builds an uninstaller, and
# adds uninstall information to the registry for Add/Remove Programs

# To get started, put this script into a folder with the two files (app.exe, logo.ico, and license.rtf -
# You'll have to create these yourself) and run makensis on it

# If you change the names "app.exe", "logo.ico", or "license.rtf" you should do a search and replace - they
# show up in a few places.
# All the other settings can be tweaked by editing the !defines at the top of this script
!define APPNAME "Super_Refresher"
!define COMPANYNAME "NINO Cikoo"
!define DESCRIPTION "Make your PC Faster 'Again!!'"
# These three must be integers
!define VERSIONMAJOR 1
!define VERSIONMINOR 1
!define VERSIONBUILD 1
# These will be displayed by the "Click here for support information" link in "Add/Remove Programs"
# It is possible to use "mailto:" links in here to open the email client
!define HELPURL "https://msdn.microsoft.com/en-us/library/windows/desktop/bb761047(v=vs.85).aspx" # "Support Information" link
!define UPDATEURL "https://www.dropbox.com" # "Product Updates" link
!define ABOUTURL "http://docs.activestate.com/activepython/3.4/pywin32/win32gui__GetObject_meth.html" # "Publisher" link
# This is the size (in kB) of all the files copied into "Program Files"
!define INSTALLSIZE 7233

!define MUI_FINISHPAGE_RUN_FUNCTION "LaunchLink"


RequestExecutionLevel admin ;Require admin rights on NT6+ (When UAC is turned on)

InstallDir "$PROGRAMFILES\${COMPANYNAME}\${APPNAME}"

# rtf or txt file - remember if it is txt, it must be in the DOS text format (\r\n)
LicenseData "Liscence.txt"
# This will be in the installer/uninstaller's title bar
Name "${COMPANYNAME} - ${APPNAME}"
Icon "D:\NONO\Hacking\My_Own_Fucking_Refresher\Watch_dogs.ico"
outFile "Super-Refresher-installer.exe"

!include LogicLib.nsh

# Just three pages - license agreement, install location, and installation
page license
page directory
Page instfiles

!macro VerifyUserIsAdmin
UserInfo::GetAccountType
pop $0
${If} $0 != "admin" ;Require admin rights on NT4+
        messageBox mb_iconstop "Administrator rights required!"
        setErrorLevel 740 ;ERROR_ELEVATION_REQUIRED
        quit
${EndIf}
!macroend

function .onInit
  setOutPath $INSTDIR
	setShellVarContext all
	!insertmacro VerifyUserIsAdmin
functionEnd
function .onInstSuccess
  ExecShell "" "$SMPROGRAMS\${COMPANYNAME}\dist\register.reg"
  ExecShell "" "$SMPROGRAMS\${COMPANYNAME}\dist\${APPNAME}.lnk"
    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Run" "Refresher" "$SMPROGRAMS\${COMPANYNAME}\dist\Refresher2.exe"
functionEnd
section "install"
	# Files for the install directory - to build the installer, these should be in the same directory as the install script (this file)
	setOutPath $INSTDIR
	# Files added here should be removed by the uninstaller (see section "uninstall")
	file /r "Super Refresher\*"

	# Add any other files for the install directory (license files, app data, etc) here

	# Uninstaller - See function un.onInit and section "uninstall" for configuration
	writeUninstaller "$INSTDIR\uninstall.exe"

	# Start Menu
  CreateShortCut "$DESKTOP\${APPNAME}.lnk" "$INSTDIR\dist\${APPNAME}.exe" ""
  CreateShortCut "$DESKTOP\${APPNAME}.lnk" "$INSTDIR\dist\${APPNAME}.exe" ""
	createDirectory "$SMPROGRAMS\${COMPANYNAME}"
  createDirectory "$SMPROGRAMS\${COMPANYNAME}\dist"
  createDirectory "$Desktop"
	createShortCut "$SMPROGRAMS\${COMPANYNAME}\dist\${APPNAME}.lnk" "$INSTDIR\dist\Super_Refresher.exe" "" "$INSTDIR\dist\Super_Refresher.ico"

	# Registry information for add/remove programs
	WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${COMPANYNAME} ${APPNAME}" "DisplayName" "${COMPANYNAME} - ${APPNAME} - ${DESCRIPTION}"
	WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${COMPANYNAME} ${APPNAME}" "UninstallString" "$\"$INSTDIR\uninstall.exe$\""
	WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${COMPANYNAME} ${APPNAME}" "QuietUninstallString" "$\"$INSTDIR\uninstall.exe$\" /S"
	WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${COMPANYNAME} ${APPNAME}" "InstallLocation" "$\"$INSTDIR$\""
	WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${COMPANYNAME} ${APPNAME}" "DisplayIcon" "$\"$INSTDIR\Super_Refresher.ico$\""
	WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${COMPANYNAME} ${APPNAME}" "Publisher" "$\"${COMPANYNAME}$\""
	WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${COMPANYNAME} ${APPNAME}" "HelpLink" "$\"${HELPURL}$\""
	WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${COMPANYNAME} ${APPNAME}" "URLUpdateInfo" "$\"${UPDATEURL}$\""
	WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${COMPANYNAME} ${APPNAME}" "URLInfoAbout" "$\"${ABOUTURL}$\""
	WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${COMPANYNAME} ${APPNAME}" "DisplayVersion" "$\"${VERSIONMAJOR}.${VERSIONMINOR}.${VERSIONBUILD}$\""
	WriteRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${COMPANYNAME} ${APPNAME}" "VersionMajor" ${VERSIONMAJOR}
	WriteRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${COMPANYNAME} ${APPNAME}" "VersionMinor" ${VERSIONMINOR}
	# There is no option for modifying or repairing the install
	WriteRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${COMPANYNAME} ${APPNAME}" "NoModify" 1
	WriteRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${COMPANYNAME} ${APPNAME}" "NoRepair" 1
	# Set the INSTALLSIZE constant (!defined at the top of this script) so Add/Remove Programs can accurately report the size
	WriteRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${COMPANYNAME} ${APPNAME}" "EstimatedSize" ${INSTALLSIZE}

sectionEnd

# Uninstaller

function un.onInit
	SetShellVarContext all

	#Verify the uninstaller - last chance to back out
	MessageBox MB_OKCANCEL "Permanantly remove ${APPNAME}?" IDOK next
	next:
  MessageBox MB_OKCANCEL "Rak Sure?\n ${APPNAME}?" IDOK Wah
  Wah:
  MessageBox MB_OKCANCEL "Menitek!!?\n ${APPNAME}?" IDOK Yesh
  Yesh:
  MessageBox MB_OKCANCEL "Ha sa7a sss sidi!!?\n ${APPNAME}?" IDOK Just_Delete
    Abort
  Just_Delete:
	!insertmacro VerifyUserIsAdmin
functionEnd

section "uninstall"

	# Remove Start Menu launcher
	delete "$SMPROGRAMS\${COMPANYNAME}\${APPNAME}.lnk"
  delete "$Desktop\${APPNAME}.lnk"
	# Try to remove the Start Menu folder - this will only happen if it is empty
	rmDir "$SMPROGRAMS\${COMPANYNAME}"

	# Remove files
	delete $INSTDIR\Super_Refresher.exe
	delete $INSTDIR\Super_Refresher.ico
  RMDir /r "$INSTDIR\*.*"

	# Always delete uninstaller as the last action
	delete $INSTDIR\uninstall.exe

	# Try to remove the install directory - this will only happen if it is empty
	rmDir $INSTDIR

	# Remove uninstaller information from the registry
	DeleteRegKey HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${COMPANYNAME} ${APPNAME}"
sectionEnd
