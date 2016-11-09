# arp2morse
Use python to scan your network for know devices (by MAC address). If a known device is found send a subtle morse signal.

----
The code was tested on a Laptop running Kubuntu and on a Raspberry Pi 3 running [Raspian Jessie Lite])https://www.raspberrypi.org/downloads/raspbian/).

This little project mainly stiches together small bits of code created by different people. A nice introduction to python and morse code can be found at [Morse Code and Dictionaries in Python (with Sound)] (http://thelivingpearl.com/2013/01/08/morse-code-and-dictionaries-in-python-with-sound/) by @cptdeadbones. This blogpost and software saved me hours of trying. 

If you have any suggestions or comments regarding the code, please let me know. I'm still knew to python and I love to improve my code. 

Just as [@cptdeadbones] (https://github.com/cptdeadbones/python_morse_code) I use the sound files from [Morse Code from wikimedia commons] (http://commons.wikimedia.org/wiki/Morse_code). He has conviently downloaded all the sound files and made them available to [download in zip-format] (http://temp3.net/thelivingpearl_downloads/morse_sound_files.zip).

# Installation
* download *arp2morse.py*
* [install Python] (https://www.python.org/)
* download the sound files mentioned above
* add your _MAC addresses_ and your _path to the sound files_ in *arp2morse.py*
* open a Terminal and run `sudo python arp2morse.py 192.168.0.0/24` (your IP address my vary)
* listen to the code
