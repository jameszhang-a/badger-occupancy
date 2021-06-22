# Badger Occupancy
A script to log the occupancy of the Nick Rec Center every 15 minutes to determine the best time to work out. 

## How to set up

1. First, run `crontab -e` in the terminal.

2. Then, add the following to the file:
```shell
*/15 6-21 * * 1-5 /usr/bin/python3 ~/code/project/badger-occupancy/main.py
```
The `*/15 6-21 * * 1-5` specifies that the script should run 

>At every 15th minute past every hour from 6 through 21 on every day-of-week from Monday through Friday.

And the rest specifies the location of python and the script. 