# mount


##### Description
manage mount points

##### Parameters

*   **`path`** (*required*): the path of the mount point

*   **`device`** (*required*): the device name

*   **`filesystem`** (*required*): the file system type of the device

*   **`fstab`** (*optional*): whether to save in /etc/fstab or not, by default ***`false`***

*   **`opts`** (*optional*): a list of options for /etc/fstab, see *`fstab(8)`*

	>note: this parameter applies only if `fstab is `true`

*   **`dump`** (*optional*): the dump value in /etc/fstab, see *`fstab(8)`*

	>note: this parameter applies only if `fstab` is `true`

*   **`pass`** (*optional*): the pass value in /etc/fstab, see *`fstab(8)`*

	>note: this parameter applies only if `fstab` is `true`
				