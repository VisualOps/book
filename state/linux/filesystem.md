# filesystem


##### Description
create a filesystem

##### Parameters

*   **`device`** (*required*): the path of the device to format (/dev/xvd*)

*   **`fstype`** (*required*): the filesystem type to use (ext2, ext3, ext4 or xfs)

	>note: on REHL 6, xfs requires a manual installation of the xfsprogs (yum pkg state)

*   **`label`** (*optional*): label of the device
				