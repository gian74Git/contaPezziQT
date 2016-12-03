# contaPezziQT:on a clean install follow these instructions:
1.	sudo apt-get install mysql-server
2.	pip3 install PyMySQL3
3. 	sudo apt-get install python3-pyqt5

Notice:
Sometimes in a standard jessie installation we can have some freezes and lost of reads.
We can improve this simply with this command:

sudo sed -i '/# The named pipe \/dev\/xconsole/,$d' /etc/rsyslog.conf

remember to copy rsyslog.conf in a backup copy before the command.
See: https://blog.dantup.com/2016/04/removing-rsyslog-spam-on-raspberry-pi-raspbian-jessie/


Remember to stop all non used services.
The problem is also caused from mysql. We will implement an optional connection to sqllite soon.
