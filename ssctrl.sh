#!/bin/bash

statusmsg(){
	if [ $1 == "status" ]; then
		echo "Check status of SQL Server service"
	fi

	if [ $1 == "start" ]; then
		echo "Start SQL Server service"
	fi

	if [ $1 == "stop" ]; then
		echo "Stop SQL Server service"
	fi

	if [ $1 == "restart" ]; then
		echo "Restart SQL Server service"
	fi

	if [ $1 == "disable" ]; then
		echo "Disable SQL Server service"
	fi

	if [ $1 == "enable" ]; then
		echo "Enable SQL Server service"
	fi

	echo ""
}

usage(){
	echo "ssctrl - SQL Service control utility"
	echo ""
	echo "USAGE:"
	echo ""
	echo "  ssctrl status    (Check status)"
	echo "  or"
	echo "  ssctrl start     (Start service)"
	echo "  or"
	echo "  ssctrl stop      (Stop service)"
	echo "  or"
	echo "  ssctrl restart   (Restart service)"
	echo "  or"
	echo "  ssctrl disable   (Disable service)"
	echo "  or"
	echo "  ssctrl enable    (Enable service)"

	exit
}

if [ $# -ne 1 ]; then
	usage
fi

case $1 in
	status)
		statusmsg $1
		systemctl status mssql-server
		exit
		;;
	start)
		statusmsg $1
		sudo systemctl start mssql-server
		exit
		;;
	stop)
		statusmsg $1
		sudo systemctl stop mssql-server
		exit
		;;
	restart)
		statusmsg $1
		sudo systemctl restart mssql-server
		exit
		;;
	disable)
		statusmsg $1
		sudo systemctl stop mssql-server
		sudo systemctl disable mssql-server
		exit
		;;
	enable)
		statusmsg $1
		sudo systemctl enable mssql-server
		sudo systemctl start mssql-server
		exit
		;;
esac

usage
