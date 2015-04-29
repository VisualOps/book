# mesos master


##### Description
Runs a Mesos Master instance

##### Parameters

*   **`cluster_name`** (*required*): Name of the Mesos cluster

		example:
			Mesos Cluster

*   **`server_id`** (*required*): ID of the Mesos Master server

		example:
			1
			2

*   **`masters_addresses`** (*required*): IPs/hostnames of the Mesos Master servers. If no hostname is given, the ip address will be used by default as hostname.

		example:
			@{master1.PrivateIpAddress}:    master1
			@{master2.PrivateIpAddress}:    master2
			@{master3.PrivateIpAddress}:

*   **`hostname`** (*optional*): Hostname of the Mesos Master server instance

		example:
			master1

*   **`framework`** (*optional*): Framework to install on top of Mesos

		example:
			marathon
			