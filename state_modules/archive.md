# archive


##### Description
extract an archive file

##### Parameters

*   **`source`** (*required*): the archive file url

		example: http(s):///host/path/to/archive.tar.gz

	>note: currently supported archive format: tar, tgz, tar.gz, bz, bz2, tbz, zip (archive file must end with one of these extention name)
			local archive file `file://path/to/file` not supported in this version

*   **`path`** (*required*): the path to extract the archive

	>note: the path will be auto-created if it doesn't exist

*   **`checksum`** (*optional*): the url of the source checksum file or checksum value string, whose value (content) will be used to verify the integrity of the source archive, only support md5

		example:
			http(s):///host/path/to/checksum_file
			md5:md5_value_string

*   **`if-path-absent`** (*optional*): extract the archive only if none of the specified path exists, see blow

	> note: once the source archive is successfully extracted to the specified path, the opsagent will decide whether to re-fetch and extract the source archive depending on or not:
	- when `if-path-absent` specified:
		- if none of the specified paths exist, the archive will be re-fetched, until some paths exist
		- if some paths exists, the archive will only be re-fetched only if `checksum` is used and its value changes between rounds
	- when `if-path-absent` not used:
		- if `checksum` not used, the archive will be re-fetched in every round
		- if `checksum` used, thhe archive will be re-fetched if the checksum value changes between rounds
				