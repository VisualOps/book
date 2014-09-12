# docker


##### Description
Run a container from a remote image

##### Parameters

*   **`container`** (*required*): Desired name of the container (must be the name specified in "pulled" and "built" states, if any)

		example:
			my_container

*   **`image`** (*required*): Image/repo from which to build this container

		example:
			namespace/image

*   **`tag`** (*optional*): Repository tag (default: latest)

		example:
			latest

*   **`username`** (*optional*): Username used to login to repository

*   **`password`** (*optional*): Password used to login to repository (required if username specified)

*   **`email`** (*optional*): Email used to login to repository (required if username specified)

*   **`count`** (*optional*): Specify the number of containers to run

*   **`command`** (*optional*): Command to run in the container (if not specified in `Dockerfile`)

		example (in case of apache server):
			/usr/bin/apache2
			-D
			FOREGROUND

*   **`environment`** (*optional*): Environment variables for the container (if not specified in `Dockerfile`)

		example:
			FOO: bar

*   **`volumes`** (*optional*): List of volumes to attach (if not specified in `Dockerfile`). (specify :ro for read only mode)

		example:
			/host/path: /mount/point
			/host/path: /mount/point/read/only:ro

*   **`mem_limit`** (*optional*): Memory size limit (if not specified in `Dockerfile`)

		example:
			512m

*   **`cpu_shares`** (*optional*): CPU shares authorized (if not specified in `Dockerfile`)

		example:
			0-3

		example:
			0

*   **`publish_all_ports`** (*optional*): Publish all ports

*   **`links`** (*optional*): Link several container together (if not specified in `Dockerfile`)

		example:
			name_other_container: alias_for_other_container

*   **`port_bindings`** (*optional*): List of ports to expose on host system. Maps containers port/protocol to host listening ip:port

		note:
			If the count parameter is specified, the host port will be incremented by one on each.

		example:
			5000/tcp: 127.0.0.1:5000
			6000/tcp: 6000 (default ip: 0.0.0.0)
			80: 6666 (default protocol: tcp)

*   **`files`** (*optional*): list of persistent files

		example:
			/etc/nginx/nginx.conf : *content*
			/etc/my.cnf           : *content*
				