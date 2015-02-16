# user


##### Description
manage a user

##### Parameters

*   **`username`** (*required*): the user name

*   **`password`** (*required*): the encrypted password

	>note: use `openssl passwd -salt <salt> -1 <plaintext>` to generate the password hash

*   **`fullname`** (*optional*): the user's full name

*   **`uid`** (*optional*): the user id

*   **`gid`** (*optional*): the group id

*   **`home`** (*optional*): the user's home directory, by default `/home/$username`

	>note: if the directory already exists, the uid and gid of the directory will be set to this user; otherwise, the directory (and its parent directories) will be created, with the uid and gid

*   **`system-account`** (*optional*): whether to create a system account or not (see `useradd(8)`), by default: `false`

*   **`no-login`** (*optional*): whether to allow user to login or not, by default `false`

*   **`groups`** (*optional*): a list of groups of the user

	>note: if pass in an empty list, all groups of the user will be removed except the defaut one
				