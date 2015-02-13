# chef client


##### Description
Run a Chef client. This module allows you to run a Chef recipe distributed by a Chef server. This is useful if you already have a Chef server running and you want to control the client recipe execution on your instance using VisualOps.

See Chef documentation for more details.

##### Parameters

*   **`server`** (*required*): URI to remote Chef server. Ensure you are able to resolv its hostname.

		example:
			https://localhost

*   **`client_key`** (*optional*): Path to client authentication key. This is usually required to establish a connection to the chef server.

		example:
			/path/to/client/key

*   **`config`** (*optional*): Path to chef config file

		example:
			/path/to/config/file

*   **`arguments`** (*optional*): Additional arguments to chef, passed to the chef binary (see chef documentation). You can use these arguments to specify a running group, or a log level, for example.

		example:
			group:     root
			log_level: warning

*   **`version`** (*optional*): Chef version. Leave empty for latest version.

		example:
			12.0.1
				