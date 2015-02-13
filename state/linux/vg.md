# vg


##### Description
manage LVM volume group (VG)

##### Parameters


*   **`name`** (*required*): the VG name

*   **`path`** (*required*): a list of block special devices

		Example: /dev/sdk1, /dev/sdl1

*   **`clustered`** (*optional*): whether to enable the clustered locking on the VG or not, by default ***`true`***

	>note: If the new VG is shared with other nodes in the cluster, need to enable this option. If the new VG contains only local disks that are not visible on the other nodes, this option must be turned off. If the cluster infrastructure is unavailable on a particular node at a particular time, you may still be able to use such VGs

*   **`max-lv-number`** (*optional*): specify the maximum number of LVs allowed in this VG

	>note: For VGs with  metadata in lvm1 format, the limit and default value is 255. If the metadata uses lvm2 format, the default value is 0 which removes this restriction: there is then no limit

*   **`max-pv-number`** (*optional*): specify the maximum number of PVs that can belong to this VG

	>note: For VGs with metadata in lvm1 format, the limit and default value is 255. If the metadata uses lvm2 format, the value 0 removes this restriction: there is then no limit

*   **`metadata-type`** (*optional*): specify which type of on-disk metadata to use, by default ***`lvm2`***

		Example: lvm1, lvm2, 1, 2

	>note:
			lvm1 or lvm2 can be abbreviated to 1 or 2 respectively. The default (lvm2) can be changed by setting format
			in the global section of the config file.

*   **`metadata-copies`** (*optional*): specify the desired number of metadata copies in the VG

		Example: unmanaged, all

	>note: If set to a non-zero value, LVM will automatically manage the 'metadata ignore' option on the PVs (see pvcreate(8) or pvchange --metadataignore) in order to achieve the copies of metadata. If set to unmanaged, LVM will not automatically manage the 'metadata ignore' option. If set to all, LVM will first clear all of the 'metadata ignore' option on all metadata areas in the VG, then set the value to unmanaged. This option is useful for VGs containing large numbers of PVs  with metadata  as it may be used to minimize metadata read and write overhead. The default value is unmanaged

*   **`pe-size`** (*optional*): specify the physical extent size on PVs of this VG

		Example: bBsSkKmMgGtTpPeE

   	>note: A size suffix (k for kilobytes up to t for terabytes) is optional, megabytes is the default if no suffix is present. The default is 4 MiB and it must be at least 1 KiB and a power of 2.

	>Once this value has been set, it is difficult to change it without recreating the volume group which would involve  backing up and restoring data on any logical volumes. However, if no extents need moving for the new value to apply, it can be altered using vgchange -s.

	>If the volume group metadata uses lvm1 format, extents can vary in size from 8KiB to 16GiB and there is a limit of 65534 extents in each logical volume. The default of 4 MiB leads to a maximum logical volume size of around 256GiB.

	>If the volume group metadata uses lvm2 format those restrictions do not apply, but having a large number of extents will slow down the tools but have no impact on I/O performance to the logical volume. The smallest PE is 1KiB

	>The 2.4 kernel has a limitation of 2TiB per block device.

*   **`autobackup`** (*optional*): whether to metadata should be backed up automatically after a change or not, by default ***`true`***

	>note: You are strongly advised not to disable this! See vgcfgbackup(8)

*   **`tag`** (*optional*): add the tag to this VG

	>note: A tag is a word that can be used to group LVM2 objects of the same type together. Tags can be given on the command line in place of PV, VG or LV arguments. Tags should be prefixed with  @ to avoid ambiguity. Each tag is expanded by replacing it with all objects possessing that tag which are of the type expected by its position on the command line. PVs can only possess tags while they are part of a Volume Group: PV tags are discarded if the PV is removed from the VG. As an example, you could tag some LVs as database and others as userdata and then activate the  database  ones  with  lvchange  -ay @database. Objects can possess multiple tags simultaneously. Only the new LVM2 metadata format supports tagging: objects using the LVM1 metadata format cannot be tagged because the on-disk format does not support it. Characters allowed in tags are: A-Z a-z 0-9 _ + . - and as of version 2.02.78 the following characters are also accepted: / = ! : # &

*   **`allocation-policy`** (*optional*): specify the allocation policy

		Example: contiguous, cling, normal, anywhere or inherit

	>note: When a command needs to allocate Physical Extents from the Volume Group, the allocation policy controls how they are chosen. Each Volume Group and Logical Volume has an allocation policy defined. The default for a Volume Group is normal which applies common-sense rules such as not placing parallel stripes on the same Physical Volume. The default for a Logical Volume is inherit which applies the same policy as for the Volume Group. These policies can be changed using lvchange(8) and vgchange(8) or overridden on the command line of any command that performs allocation. The contiguous policy requires that new Physical Extents be placed adjacent to existing Physical Extents. The cling policy places new Physical Extents on the same Physical Volume as existing Physical Extents in the same stripe of the Logical Volume. If there are sufficient free Physical Extents to satisfy an allocation request but normal doesn't use them, anywhere will - even if that reduces performance by placing two stripes on the same Physical Volume.
				