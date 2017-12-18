startvmX.sh is a shellsript for maual testing, taking an id(int) as argument to:
  -start a instance of QEMU and load the image of the Genode OS
  -print the process id of the QEMU instance and the ip address of the Genode OS

autoVM.sh is a shellscript for datageneration, which takes an id(int) and the end or the range to work on, as arguments to:
  - start a instance of QEMU and load the image of the Genode OS
  - find the ip of the OS
  - start a dom0_p0.py
  - checking every t seconds if the output from the dom0_p0.py has changed
      - if it hasn't kill the script, kill the QEMU instance and restart
  The necessary output and progress files are in a directory called 'output'
