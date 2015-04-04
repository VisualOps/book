# raid


##### Description
Create and ensure a Raid array is present.

See `mdadm` documentation for more details.

##### Parameters

*   **`device-name`** (*required*): Name of the raid array

		example:
			/dev/md0

*   **`level`** (*required*): The RAID level to use when creating the raid. Options are: linear, raid0, 0, stripe, raid1, 1, mirror, raid4, 4, raid5, 5, raid6, 6, raid10, 10, multipath, mp, faulty, container. Obviously some of these are synonymous.

		example:
			raid1

*   **`devices`** (*required*): A list of devices used to build the array.

		example:
			/dev/xvdf, /dev/xvdg

*   **`arguments`** (*optional*): Additional arguments passed to the mdadm binary (see mdadm documentation). You can use these arguments to specify chunk size, for example.

		example:
			chunk:	256
				