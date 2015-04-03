# puppet apply


##### Description
Apply a Puppet manifest. This module will run independently, and doesn't require to connect to any Puppet server.

`puppet apply` will run the manifests files set in the `manifests` parameter.

Note: Puppet module is incompatible with CentOS 6.4

##### Parameters

*   **`manifests`** (*required*): Manifest(s) to run

		example:
			/path/to/manifest1
			/path/to/manifest2

*   **`arguments`** (*optional*): Arguments to the manifest, passed to the Puppet binary (see Puppet documentation). You can use these arguments to specify a modules directory, or some specific classes to run, for example.

		example:
			modulepath: /a/b/modules
			tags:       basefiles::edit,apache::server

*   **`version`** (*optional*): Puppet version to install. Leave empty for latest version.

		example:
			3.7.3
				