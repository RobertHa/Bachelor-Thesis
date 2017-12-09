#!/bin/bash
vm=$1
vmIP=192.168.217.1
ende=$2

while true
do

    screen -dmS vm$vm bash -c "qemu-system-arm -net vde,sock=/tmp/switch1 -net nic,macaddr=02:00:00:00:01:$(($vm + 10)) -net nic,model=lan9118 -nographic -smp 2 -M realview-pbx-a9 -kernel build/genode-focnados_pbxa9/var/run/dom0-HW/image.elf -M realview-pbx-a9 -kernel build/genode-focnados_pbxa9/var/run/dom0-HW/image.elf -m 768 -M realview-pbx-a9 -kernel build/genode-focnados_pbxa9/var/run/dom0-HW/image.elf"
    sleep 20 #wait till vm started
    #vmID="$(ps -ef | grep -ni -e "SCREEN -dmS vm$vm" | grep -v "grep" | awk '{print $2}')"
    ping -c 1 $vmIP > /dev/null
    if [ $? -eq 0 ]
    then
	echo $vmIP is okay to use	
    else
	vmIP="$(nmap -sP 192.168.217.0/24 >/dev/null && arp -n | grep -e "02:00:00:00:01:$(($vm + 10))" | awk '{print $1}')"
    fi
    if [[ $vmIP == *"192"* ]]
    then
	echo vm$vm started successful
    
	screen -dmS script$vm bash -c "python3 -u ./toolchain-host/host_dom0/dom0_p0.py $vmIP $vm $ende > ./output/out$vm.log 2> ./output/err$vm.log"
	sleep 1
	echo script$vm started
	while true
	do
		oldoutsize=$(stat -c%s "./output/out${vm}.log")
		sleep 120 
		if [ 0 -lt $(stat -c%s "./output/err${vm}.log") ]
       		then
			echo an error occured in script$vm: $(sed -n '$p' "./output/err${vm}.log")
			break
		fi
		if [ $oldoutsize -eq $(stat -c%s "./output/out${vm}.log") ]
		then
			echo script$vm died somewhere with: $(sed -n '$p' "./output/out${vm}.log")
			break
		fi
	done
	echo killing script$vm
	screen -S script$vm -X quit
    else
	echo cant find ip, restart vm$vm
    fi
    echo killing vm$vm
    screen -S vm$vm -X quit

    echo $(<./output/progress${vm}.log)
    if [ $(<./output/progress${vm}.log) == "done" ]
    then
        echo success on vm$vm till $ende
        exit 0
    fi
done
