# docker pulled


##### Description
Pull the latest image from the specified repository at the specified tag (if any)

##### Parameters

*   **`repo`** (*required*): Repository URL or/and Image name

		example:
			namespace/repo

*   **`tag`** (*optional*): Repository tag (default: latest)

		example:
			latest

*   **`username`** (*optional*): Username used to login to repository

*   **`password`** (*optional*): Password used to login to repository (required if username specified)

*   **`email`** (*optional*): Email used to login to repository (required if username specified)

*   **`containers`** (*optional*): Container(s) associated to this image (specify it if you want your container to be re-created when a new version of the image is pulled)

		example:
			my_container
				