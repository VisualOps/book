# supervisord


##### Description
ensure supervisord and the specified services are running, and trigger supervisord to restart the services if necessary

##### Parameters

*   **`config`** (*required*): the path of supervisord configuration file

		example: /etc/supervisord.conf

		>note: When this file is modified, supervisord will be restarted, which causes all managed services to be restarted

*   **`name`** (*required*): the name list of the services to be running (see below)

		example: httpd, mysqld

*   **`watch`** (*optional*): watch a list of files, restart the service if any of them is modified

		example: /etc/nginx/nginx.conf
				