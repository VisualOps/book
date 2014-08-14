# wait


##### Description
wait for remote state(s) to complete. If any is not done yet, it will block the host on the waiting state.

##### Parameters

*   **`state`** (*required*): one or multiple remote states to be waited

		example:
			@{host.state.1}
					