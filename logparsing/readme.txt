arrival
start
exit
exec time
sind in ms

critical time in µs

state 1 running
state 5 dead

01.hey  ----- bietet service an
hey	..... eigentlicher thread mit main und so
ep	..... entry point
signal handler


wird fertig
	exittime = 0
	nach stop
		entry point state = 5 und auf riptable
	nach clear
		auch task auf state = 5 und auf riptable

wird nicht fertig (zb wegen critical time)
	exittime = 0
	nach stop
		point  state = 5 und auf riptable

wird nicht fertig (gekillt durch stop)
	nach stop
		main bekommt exit time
		alle bleiben state = 1
		sehe auch ep und signal handler in log
	nach clear (nächster run log)
		alle auf rip und state = 5
