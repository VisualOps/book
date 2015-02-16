# svn


##### Description
manage a svn repo

##### Parameters

* **`path`** (*required* ): the path to checkout the repo

		example: /var/www/html/mysite/

* **`repo`** (*required*): the svn repository uri

		example:
			file://local/filesystem/path
			http://[user@]host[:port][path]
			https://[user@]host[:port][path]
			svn://[user@]host[:port][path]
			svn+ssh://[user@]host[:port][path]

* **`revision`** (*optional*): the revision to checkout

		example: HEAD, BASE, COMMITED, PREV, etc,. (ref: [Revision Specifiers](http://svnbook.red-bean.com/en/1.7/svn.tour.revs.specifiers.html))

* **`username`** (*optional*): the username of the svn server

* **`password`** (*optional*): the password of the svn user

* **`force`** (*optional*): force the checkout if there is conflict, by default ***`false`***

* **`user`** (*optional*): the username that performs the operation, by default ***`root`***
				