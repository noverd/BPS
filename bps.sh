#!/bin/bash
case $1 in install)
	case "$2" in
	-f) 
		echo "Установка из файла..." ;;
	*) 
		echo "Поиск файла в репозитории..." ;;
	esac
	;;
esac  
