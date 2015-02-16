# yum repo


##### Description
manage a yum repo

##### Parameters

* **`name`** (*required*): the repo name

		 example: epel

* **`content`** (*optional*): the content of the repo configuration file

		example:
			[10gen]
			name=10gen Repository
			baseurl=http://downloads-distro.mongodb.org/repo/redhat/os/i686
			gpgcheck=0
			enabled=1

* **`rpm-url`** (*optional*): the repo rpm url (if no content specified)

		example: http://mirrors.hustunique.com/epel/6/i386/epel-release-6-8.noarch.rpm
				