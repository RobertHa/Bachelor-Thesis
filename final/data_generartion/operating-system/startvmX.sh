  #!/bin/bash 

vm=$1         
echo VM $vm started
#Create temporary file with new line in place
screen -dmS vm$vm bash -c " qemu-system-arm -net vde,sock=/tmp/switch1 -net nic,macaddr=02:00:00:00:01:$(($vm + 10)) -net nic,model=lan9118 -nographic -smp 2 -M realview-pbx-a9 -kernel build/genode-focnados_pbxa9/var/run/dom0-HW/image.elf -M realview-pbx-a9 -kernel build/genode-focnados_pbxa9/var/run/dom0-HW/image.elf -m 768 -M realview-pbx-a9 -kernel build/genode-focnados_pbxa9/var/run/dom0-HW/image.elf"
pid="$(ps -ef | grep -ni -e "SCREEN -dmS vm$vm" | grep -v "grep" | awk '{print $2}')"
echo $pid
vmIP="$(nmap -sP 192.168.217.0/24 >/dev/null && arp -n | grep -e "02:00:00:00:01:$(($vm + 10))" | awk '{print $1}')"
echo $vmIP
	#Copy the new file over the original file
	#mv /dir/temp_file /dir/file


