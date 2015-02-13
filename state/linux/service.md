# service


##### Description
ensure the specified services are running, and trigger service restart if necessary

##### Parameters

*   **`name`** (*required*): the list of the service names to be run

		example: httpd, mysqld

*   **`watch`** (*optional*): watch a list of files, restart the service if any of them is modified

		example: /etc/nginx/nginx.conf, /etc/my.cnf
				