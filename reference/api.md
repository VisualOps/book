# API

With our Reload App API, you can either update one App or update more. All you needs are `app_id`, your `user name`, and a `token`.

- you can find your `app_id` in the right property panel of App View in VisualOps IDE

[figure]

- And you can generate and manage your application token in "xx -> xx -> xx". you can configure/revoke different tokens for different application, e.g. source repo, CI, packages upload.

[figure]

The API includes

#### Single App Reload


- URL:

  `POST https://api.visualops.io/v1/apps/app-id`

- Content-Type: `application/json`
- Content:

	  {
		  "user":  "a-user",
		  "token": "xxxxxxxxxxxxxxxxxxxxxxx"
	  }

- Return codes:
  - success update: `200`
  - invalid `user`/`token`: `401`
  - app not exist or not managed with visualops: `404`
  - request too fast(two requests of one app in less than 2 seconds): `429`
  - Internal server error: `500`

#### Batch Apps Reload


- URL:

  `POST https://api.visualops.io/v1/apps`

- Content-Type: `application/json`
- Content:

	  {
		  "user":  "a-user",
		  "app": [
			 "app1",
			 "app2"
		  ],
		  "token": "xxxxxxxxxxxxxxxxxxxxxxx"
	  }


- Return code `200`
  - Body

		{
			"success": ["app1", "app2"],
			"failed": ["app3", "app4"]
		}
- Failure return codes:
  - invalid `user`/`token`: `401`
  - Internal server error: `500`
