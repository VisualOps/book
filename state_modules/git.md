# git


##### Description
manage a git repo

##### Parameters

* **`path`** (*required* ): the path to clone the repo

		example: /var/www/html/mysite/

*   **`repo`** (*required*): the git repository uri

		example:
			/path/to/repo.git/
			file:///path/to/repo.git/
			http[s]://host[:port][path]
			ftp[s]://host[:port][path]
			ssh://[user@]host[:port]/~[user][path]
			git://[user@]host[:port]/~[user][path]
			rsync://host[:port][path]

* **`revision`** (*optional*): the revision to checkout

		example:
			specify a branch and keep it synced: master, develop
			specify a static tag - release-1.0
			specify a particular revision id - 8b1e0f7e499f9af07eed5ba6a3fc5490e72631b6

* **`ssh-key-file`** (*optional*): the path of the ssh keypair file

		example: /root/.ssh/id_rsa

* **`force`** (*optional*): force the checkout if there is conflict, by default ***`false`***

* **`user`** (*optional*): the username that performs the operation, by default ***`root`***
				