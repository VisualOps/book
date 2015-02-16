# pv


##### Description
manage LVM physical volume (PV)

##### Parameters

*   **`path`** (*required*): the path of the device or partition
`
		Example: /dev/sdc4, /dev/sde

*   **`force`** (*optional*): force to create the PV without any confirmation, by default ***`false`***

	>note: You can not recreate (reinitialize) a PV belonging to an existing volume group.


*   **`uuid`** (*optional*): specify the uuid for the device

	>note: Without this option, a random uuid will be generated. All of your PVs must have unique uuids. You need to use this option before restoring a backup of LVM metadata onto a replacement device - see vgcfgrestore(8). As such, use of restore file is compulsory unless the norestorefile is used.


*   **`zero`** (*optional*): whether or the first 4 sectors (2048 bytes) of the device should be wiped or not, by default ***`true`***

	>note: If this option is not given, the default is to wipe these sectors unless either or both of the --restorefile or --uuid options were specified.

*   **`data-alignment`** (*optional*): align the start of the data to a multiple of this number

	>note: You should also specify an appropriate "PV size" when creating the Volume Group (VG). To see the location of the first Physical Extent of an existing Physical Volume use pvs -o +pe_start. It will be a multiple of the requested alignment. In addition it may be shifted by alignment_offset from data_alignment_offset_detection (if enabled in lvm.conf(5)) or --dataalignmentoffset.

*   **`data-alignment-offset`** (*optional*): shift the start of the data area by this additional number

*   **`metadata-size`** (*optional*): the approximate amount of space to be set aside for each metadata area

	>note: The size you specify may get rounded

*   **`metadata-type`** (*optional*): specify which type of on-disk metadata to use, by default ***`lvm2`***

		Example: lvm1, lvm2, 1, 2

	>note: lvm1 or lvm2 can be abbreviated to 1 or 2 respectively. The default (lvm2) can be changed by setting format in the global section of the config file.

*   **`metadata-copies`** (*optional*): the number of metadata areas to set aside on each PV

		Example: currently this can be 0, 1 or 2

	>note: If set to 2, two copies of the volume group metadata are held on the PV, one at the front of the PV and one at the end. If set to 1 (the default), one copy is kept at the front of the PV (starting in the 5th sector). If set to 0, no copies are kept on this PV - you might wish to use this with VGs containing large numbers of PVs. But if you do this and then later use vgsplit(8) you must ensure that each VG is still going to have a suitable number of copies of the metadata after the split!

*   **`metadata-ignore`** (*optional*): whether to ignore metadata areas on this PV or not, by default ***`false`***

	>note: This setting can be changed with pvchange. If metadata areas on a physical volume are ignored, LVM will not store metadata in the metadata areas present on this Physical Volume. Metadata areas cannot be created or extended after Logical Volumes have been allocated on the device. If you do not want to store metadata on this device, it is still wise always to allocate a metadata area in case you need it in the future and to use this option to instruct LVM2 to ignore it.

*   **`restore-file`** (*optional*):

	>note: In conjunction with "uuid", this extracts the location and size of the data on the PV from the file (produced  by  vgcfgbackup) and ensures that the metadata that the program produces is consistent with the contents of the file i.e. the physical extents will be in the same place and not get overwritten by new metadata. This provides a mechanism to upgrade the metadata format or to add/remove metadata areas. Use with care. See also vgconvert(8).

*   **`no-restore-file`** (*optional*):

	>note: In conjunction with "uuid", this allows a uuid to be specified without also requiring that a backup of the metadata be provided.

*   **`label-sector`** (*optional*):

	>note: By default the PV is labelled with an LVM2 identifier in its second sector (sector 1). This lets you use a different sector near the start of the disk (between 0 and 3 inclusive - see LABEL_SCAN_SECTORS in the source). Use with care.

*   **`pv-size`** (*optional*):

	>>note: Overrides the automatically-detected size of the PV, use with care
				