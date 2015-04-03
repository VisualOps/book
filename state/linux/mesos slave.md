# mesos slave


##### Description
Runs a Mesos Slave instance

##### Parameters

*   **`masters_addresses`** (*required*): IPs/hostnames of the Mesos Master servers. If no hostname is given, the ip address will be used by default as hostname.


		example:
			@{master1.PrivateIpAddress}:    master1
			@{master2.PrivateIpAddress}:    master2
			@{master3.PrivateIpAddress}:

*   **`attributes`** (*required*): Mesos slave attributes (see Mesos documentation)

		example:
			subnet: web
			public: true
			rack:   rack-5
			asg:    asg0
			zone:   all
