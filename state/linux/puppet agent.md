# puppet agent


##### Description
Run Puppet agent. This module will connect to the server specified in `server` and act as a regular Puppet client. Note thatPupper requires you to use the name of the server and not its IP address. You need to be able to resolve this name, either via DNS resolution or host file.

This module is useful if you already have a Puppet server running and you want to control the client recipe execution on your instance using VisualOps.

Note: Puppet module is incompatible with CentOS 6.4

##### Parameters

*   **`server`** (*required*): Server to connect to

		example:
			tags:       puppet.mydomain.com

*   **`arguments`** (*optional*): Arguments to the round, passed to the puppet binary (see puppet documentation). You can use these arguments to specify a modules directory, or some specific classes to run, for example.

		example:
			tags:       basefiles::edit,apache::server

*   **`version`** (*optional*): Puppet version. Leave empty for latest version.

		example:
			3.7.3
				
