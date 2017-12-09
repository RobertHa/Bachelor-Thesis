  #!/bin/bash 
         COUNTER=10
         while [ $COUNTER -lt 41  ]; do
             echo The VM counter is $(($COUNTER-10))!
	     	#Create temporary file with new line in place
		screen -dmS vm$(($COUNTER-10)) bash -c " qemu-system-arm -net vde,sock=/tmp/switch1 -net nic,macaddr=02:00:00:00:01:$COUNTER -net nic,model=lan9118 -nographic -smp 2 -M realview-pbx-a9 -kernel build/genode-focnados_pbxa9/var/run/dom0-HW/image.elf -M realview-pbx-a9 -kernel build/genode-focnados_pbxa9/var/run/dom0-HW/image.elf -m 768 -M realview-pbx-a9 -kernel build/genode-focnados_pbxa9/var/run/dom0-HW/image.elf"
		#Copy the new file over the original file
		#mv /dir/temp_file /dir/file
             let COUNTER=COUNTER+1 
         done
