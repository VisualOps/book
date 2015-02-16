# file


##### Description
manage a file

##### Parameters

*   **`path`** (*required*): the file path

		example: /root/.ssh/known_hosts

	>note: This state ensures the specifed file is present with correposnding attributes and content. If the file is present, its attributes will be left unchanged, otherwise it will be created with the same attributed of the specified file itself.

* **`user`** (*optional*): the user name of the file owner

		example: root

	>note: If specified, the file owner will be set to this user. Otherwise, the result depends on whether the file exists or not. If existed, the file owner will be left unchanged, otherwise default: root

* **`group`** (*optional*): the group name of the file owner

		example: root

	>note: If specified, the file will be set to this group. Otherwise, the result depends on whether the file exists or not. If existed, the file group will be left unchanged; otherwise default: root

* **`mode`** (*optional*): the file mode

		example: 0644

	>note: If specified, the file will be set to this mode. Otherwise, the result depends on whether the file exists or not. If existed, the file mode will be left unchanged

* **`content`** (*optional*): the file content

	>note: If the specified file exists and its MD5 does not match with `content`'s, the file will be overwritten

* **`remote_uri`** (*optional*): path where to get the content of the file (will overwrite the *content* parameter)

	>note: http, https and ftp protocols are supported

* **`absent`** (*optional*): ensure the file is absent, by default ***`false`***

	>note: If True, all other parameters are ignored
				