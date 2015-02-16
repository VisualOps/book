# cmd


##### Description
execute a shell command

##### Parameters
*   **`shell`** (*optional*): the absolute path of the shell to execute the command, by default `/bin/sh`

*   **`cmd`** (*required*): the command to execute

		example: find . -name *.pyc | xargs rm

*   **`cwd`** (*optional*): the current working directory to execute the command, be default `/opt/visualops/tmp/`

*   **`user`** (*optional*): the user to execute the command, by default the user which the agent runs as

*   **`group`** (*optional*): the group to execute the command, by default the group which the agent runs as

*   **`env`** (*optional*): environment variables for the command

*   **`timeout`** (*optional*): command timeout, by default `600` (in seconds)

	>note: By default, a command will be terminated and taken "failed" if not finishe in 600 seconds. However you can change with this option.

*   **`if-path-present`** (*optional*): the command will run only if all specified paths exist

*   **`if-path-absent`** (*optional*): the command will not run if any of the specified paths exists
				