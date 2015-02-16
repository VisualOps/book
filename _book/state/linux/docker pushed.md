# docker pushed


##### Description
Push an image to a docker registry. (`docker push`)

##### Parameters

*   **`repository`** (*required*): Repository to push

		example:
			namespace/image

		example:
			namespace/my_container

*   **`container`** (*optional*): Container id to commit (if desired to push a container as an image)

		example:
			my_container

*   **`tag`** (*optional*): Repository tag (default: latest)

		example:
			latest

*   **`message`** (*optional*): Commit message (if container specified to be commited)

*   **`author`** (*optional*): Author (if container specified to be commited)

*   **`username`** (*optional*): Username used to login to repository

*   **`password`** (*optional*): Password used to login to repository (required if username specified)

*   **`email`** (*optional*): Email used to login to repository (required if username specified)

*   **`dep_containers`** (*optional*): Containers needed to be shutdown if something new is pushed (in order to be rebuilt)

		example:
			my_container
				