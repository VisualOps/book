# docker built


##### Description
Ensure an image is built from a `Dockerfile`. If not, build it. If the file changes, the image will be rebuilt.

##### Parameters

*   **`tag`** (*required*): Tag of the image

		example:
			namespace/image

*   **`path`** (*required*): Filesystem path to the `Dockerfile`

		example:
			/opt/docker/image

*   **`containers`** (*optional*): Container(s) associated to the newly created image (specify it if you want your container to be re-created when the file changes)

		example:
			my_container

*   **`force`** (*optional*): Force (re)build on each round
				