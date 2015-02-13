# dir


##### Description
manage a directory

##### Parameters

*   **`path`** (*required*): a list of directory paths

		example: /var/www/html

	>note: This state ensures the specifed directory is present with correposnding attributes. If the parent directory is present, its attributes will be left unchanged, otherwise it will be created with the same attributes as the specified directory itself.

* **`user`** (*optional*): the user name of the directory owner

		example: root

	>note: If specified, the directory owner will be set to this user. Otherwise, the result depends on whether the directory exists or not. If existed, the directory owner will be left unchanged, otherwise default: root

* **`group`** (*optional*): the group name of the directory owner

		example: root

    >note: If specified, the directory will be set to this group. Otherwise, the result depends on whether the directory exists or not. If existed, the directory group will be left unchanged; otherwise default: root

* **`mode`** (*optional*): the directory mode

		example: 0755

	>note: If specified, the directory will be set to this mode. Otherwise, the result depends on whether the directory exists or not. If existed, the directory mode will be left unchanged

* **`recursive`** (*optional*): whehther to recursively set attributes of all sub-directories under *path*, by default ***`true`***

* **`absent`** (*optional*): ensure all directories are absent, by default ***`false`***

	>note: If True, all other parameters are ignored
				