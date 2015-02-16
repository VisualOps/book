# pip


##### Description
manage pip packages

##### Parameters

*	**`name`** (*required*): the package names and versions. You can specify multiple packages. The following values can be used for package version:
	- ***`<null>`*** *`default`*: ensure the package is installed. If not, it will install the latest version available of all PIP repos activated
	- ***`<version>`***: ensure the package is installed, in the specified version. If the version in unavailable of all PIP repos activated on the host, the state will fail
	- **`latest`**: ensure the package is installed at the latest version. If a newer version is available of all PIP repos activated on the host, the package will upgrade automatically
	- **`removed`**: ensure the package is absent
				