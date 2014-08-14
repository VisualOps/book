# virtualenv


##### Description
manage a python virtualenv

##### Parameters

*   **`path`** (*required*): the environment path

*   **`python-bin`** (*optional*): the path the python interpreter to use

	>note:
			python2.5 will use the python2.5 interpreter to create the new environment.
			The default is the interpreter that virtualenv was installed with

*   **`requirements-file`** (*optional*): the python requirements file path, which will be used to configure this environment

*   **`system-site-packages`** (*optional*): whether to give the virtual environment access to the global site-packages or not, by default ***`true`***

*   **`extra-search-dir`** (*optional*): whether to always copy files rather than symlinking or not, by default ***`false`***
				