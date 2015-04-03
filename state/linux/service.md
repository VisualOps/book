# service


##### Description
ensure the specified services are running, and trigger service restart if necessary

##### Parameters

*   **`name`** (*required*): the list of the service names to be run. The value represents the action if one of the watched file has changed (if applicable):

	- ***`<null>`*** *`default`*: try to reload the service. If reload fails, restart the service.
	- ***`<command>`***: path to a command to execute
	- ***`reload`***: 'reload' the service
	- ***`restart`***: 'restart' the service


		example: httpd: bash /opt/scripts/nginx_mysql_restart.sh, mysqld: restart


*   **`watch`** (*optional*): watch a list of files, execute action if any of them is modified

		example: /etc/nginx/nginx.conf, /etc/my.cnf
				