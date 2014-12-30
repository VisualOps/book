# puppet run


##### Description
Run a Puppet round. This module is useful in case you already have a custom configuration for the puppet client, and simply want to run a round. No argument is required. If you don't have any specific requirement and want to apply a Puppet manifest or connect to a Puppet server, this module is probably not the one you want to use.

Note: Puppet module is incompatible with CentOS 6.4

##### Parameters

*   **`arguments`** (*optional*): Arguments to the round, passed to the Puppet binary (see Puppet documentation). You can use these arguments to specify a modules directory, or some specific classes to run, for example.

		example:
			tags:       basefiles::edit,apache::server

*   **`version`** (*optional*): Puppet version. Leave empty for latest version.

		example:
			3.7.3
				