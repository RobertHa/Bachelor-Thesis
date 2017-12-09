#!/bin/bash

name=namaste
crit_time=1000
quota=5M

for i in {1..5}
 do
	cp change_me_task.xml $name$i.xml
	arg=0
	crit_time=$(($crit_time*($i*2))) 
   
	sed -i -e 's/changeme_arg/'$arg'/g' -e 's/changeme_quota/'$quota'/g' -e 's/changeme_id/'$i'/g' -e 's/changeme_crit/'$crit_time'/g' -e 's/changeme_bin/'$name'/g' $name$i.xml
done


