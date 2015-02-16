# gem


##### Description
manage ruby gems

##### Parameters

*	**`name`** (*required*): the package names and versions. You can specify multiple packages. The following values can be used for package version:
	- ***`<null>`*** *`default`*: ensure the package is installed. If not, it will install the latest version available of all GEM repos available
	- ***`<version>`***: ensure the package is installed, at the version specified. If the version in unavailable of all GEM repos available on the host, the state will fail
	- **`latest`**: ensure the package is installed at the latest version. If a newer version is available of all GEM repos available on the host, the package will upgrade automatically
	- **`removed`**: ensure the package is absent
				