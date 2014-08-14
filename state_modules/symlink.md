# symlink


##### Description
manage a symbolic link

##### Parameters

*   **`source`** (*required*): the path to link to

		example: /data/

* **`target`** (*required*): the path of the symlink

		example: /mnt/data

	>note: If the target's parent path does not exist, this state will fail.

* **`user`** (*optional*): the user name of the link owner

		example: root

	>note: If specified, the link owner will be set to this user. Otherwise, the result depends on whether the link exists or not. If existed, the link owner will be left unchanged, otherwise default: root

* **`group`** (*optional*): the group name of the link owner

		example: root

	>note: If specified, the link will be set to this group. Otherwise, the result depends on whether the link exists or not. If existed, the link group will be left unchanged; otherwise default: root

* **`mode`** (*optional*): the link mode

		example: 0777

	>note: If specified, the link will be set to this mode. Otherwise, the result depends on whether the link exists or not. If existed, the link mode will be left unchanged, otherwise default: 0777

* **`absent`** (*optional*): ensure the link is absent, by default ***`false`***

	>note: If True, all other parameters are ignored
				