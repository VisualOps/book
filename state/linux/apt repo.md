# apt repo


##### Description
manage apt repo

##### Parameters

*   **`name`** (*required*): the repository name (`/etc/apt/sources.list.d/$name.list` will be created)

* **`content`** (*required*): the source list file content

		example: deb http://www.rabbitmq.com/debian/ testing main
				