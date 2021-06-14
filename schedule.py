from crontab import CronTab

file_cron = CronTab(tabfile='file.txt')
mem_cron = CronTab(tab="""
  * * * * * command
""")

job = file_cron.new(command='main.py')
job.minute.every(1)

file_cron.write()