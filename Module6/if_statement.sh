if grep "127.0.0.1" /etc/hosts
then
	echo "Everything is okay"
else
	echo "ERROR!"
fi
