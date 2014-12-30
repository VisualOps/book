# chef solo


##### Description
Run a Chef solo. You should have your Chef recipe already present on your instance, or download it using the `recipe_url` parameter. Not that it is highly recommended to write a Chef configuration file, that you can specify in the `config` parameter. The config file may contains the location of your recipe, as well as the different items to run.

See Chef documentation for more details.

##### Parameters

*   **`config`** (*recommended*): Path to Chef recipe config file. Generally used to specify a custom location of your Chef recipe.

		example:
			/path/to/config/file

*   **`override_runlist`** (*optional*): Replace current run list with specified items for a single run

		example:
		        recipe[chef-server::default]

*   **`recipe_url`** (*optional*): URI to remote gzipped tarball of recipes (`-r` option of chef-solo)

		example:
			http://server.com/recipe.tgz

*   **`arguments`** (*optional*): Additional arguments to Chef, passed to the Chef binary (see Chef documentation). You can use these arguments to specify a running group, or a log level, for example.

		example:
			group:            root
			log_level:        warning

*   **`version`** (*optional*): Chef version. Leave empty for latest version.

		example:
			12.0.1
				