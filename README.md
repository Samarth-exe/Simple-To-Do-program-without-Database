# Simple-To-Do-program-without-Database

Modules used- pyttsx3(needs to be installed, use: pip install pyttsx3).
The To-Do list will be stored in a txt file on your computer(barely takes space).

The Code has been commented with detail to make the program easy to understand.

To create an executable file to share with people who don't have python installed:
Install The library: pyinstaller using pip (pip install pyinstaller).

-Open The folder where your file is being kept.
-Shift+Right click anywhere on the white screen in the folder.
-Open Windows Powershell here.
-In the windows powershell, write: pyinstaller --onefile nameofthefile.py --hidden-import=pyttsx3.drivers --hidden-import=pyttsx3.drivers.dummy --hidden-import=pyttsx3.drivers.espeak --hidden-import=pyttsx3.drivers.nsss --hidden-import=pyttsx3.drivers.sapi5
-Press Enter.
-Let the Process finish.
-Open Dist folder.
-Open the program.
-You can delete the txt file created while making the exe and the build and pycache folder.


Now The EXE file is ready to run on any computer even without requiring Python Interpreter Installed!

Extra:
Try to use speech_recognition library to input the item names just by speaking
