#!/bin/bash

name=linpack
crit_time=400
quota=5M

for i in {0..5}
 do
	cp change_me_task.xml $name$i.xml
	arg=$(($i*5)) #arg is the size of the matrix used in linpack
	crit_time=$((400+$i*600))
   
	sed -i -e 's/changeme_arg/'$arg'/g' -e 's/changeme_quota/'$quota'/g' -e 's/changeme_id/'$i'/g' -e 's/changeme_crit/'$crit_time'/g' -e 's/changeme_bin/'$name'/g' $name$i.xml
done


