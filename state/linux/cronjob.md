# cronjob


##### Description
manage a cron job

##### Parameters

*   **`user`** (*required*): the user to execute the cron job, by default: root

*   **`cmd`** (*required*): a list of command

		example:
			cat /proc/meminfo >> /tmp/meminfo
			ntpdate  time.apple.com

*   **`minute`** (*optional*): 0 - 59

*   **`hour`** (*optional*): 0 - 23 (must be a valid day if a month is specified)

*   **`day-of-month`** (*optional*): 1 - 31

*   **`month`** (*optional*): 1 - 12

*   **`day-of-week`** (*optional*): 0 - 7, sunday is represented by 0 or 7, monday by 1
				