#!/bin/bash

name=hey
crit_time=100
quota=5M

for i in {1..6}
 do
	cp change_me_task.xml $name$i.xml
	arg=0
	crit_time=$((360*$i)) 
   
	sed -i -e 's/changeme_arg/'$arg'/g' -e 's/changeme_quota/'$quota'/g' -e 's/changeme_id/'$i'/g' -e 's/changeme_crit/'$crit_time'/g' -e 's/changeme_bin/'$name'/g' $name$i.xml
done
