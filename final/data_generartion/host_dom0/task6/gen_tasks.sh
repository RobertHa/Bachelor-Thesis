#!/bin/bash

name=cond_42
crit_time=3600
quota=5M

for i in {1..6}
 do
	cp change_me_task.xml $name'_'$i.xml
	arg=150000000 #$(($i*14))
	#crit_time=$(($crit_time+$i*10))
   
	sed -i -e 's/changeme_arg/'$arg'/g' -e 's/changeme_quota/'$quota'/g' -e 's/changeme_id/'$i'/g' -e 's/changeme_crit/'$crit_time'/g' -e 's/changeme_bin/'$name'/g' $name'_'$i.xml
done


