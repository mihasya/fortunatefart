This is a script that will play a random sound from the directory you specify on your mac, with the likelihood you desire.

Typical usage is in a cron, such as this:

    * * * * * /usr/bin/backup.py -o 20 /Users/simplegeosf/farts

This will run the script every minute, with roughly 1 in 20 executions resulting in an actual sound.

Notice that here the file has been renamed to `backup.py` to disguise what it actually does. An even more subversive user might rename the directory containing the sounds as well.
