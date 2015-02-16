# hg


##### Description
manage a hg repo

##### Parameters

* **`path`** (*required* ): the path to clone the repo

		example: /var/www/html/mysite/

*   **`repo`** (*required*): the hg repository uri

		example:
			local/filesystem/path
			file://local/filesystem/path
			http://[user@]host[:port]/[path]
			https://[user@]host[:port]/[path]
			ssh://[user@]host[:port]/[path]

* **`revision`** (*optional*): the revision to checkout

		example:
			specify a branch and keep it synced: master, develop
			specify a static tag - release-1.0
			specify a particular revision id - 8b1e0f7e499f9af07eed5ba6a3fc5490e72631b6

* **`force`** (*optional*): force the checkout if there is conflict, by default ***`false`***

* **`user`** (*optional*): the username that performs the operation, by default ***`root`***
				