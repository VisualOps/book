# npm


##### Description
                                        manage node.js package (requires npm 1.2 or higher)

##### Parameters

*	**`name`** (*required*): the package names and versions. You can specify multiple packages. The following values can be used for package version:
	- ***`<null>`*** *`default`*: ensure the package is installed. If not, it will install the latest version available in all active NPM repos
	- ***`<version>`***: ensure the package is installed, at the specified version. If the version in unavailable in all active NPM repos on the host, the state will fail
	- **latest**: ensure the package is installed at the latest version. If a newer version is available in all active NPM repos on the host, the package will upgrade automatically
	- **removed**: ensure the package is absent

	>note: the specified packages will be installed as global packages (npm install --global)

* **`path`** (*optional*): the path where the packages should be installed to `$path/node_modules`
		>note:
			if ignored, the packages will be installed as global packages, usually `/usr/local/lib/node_modules/` (e.g. npm install --global)
				