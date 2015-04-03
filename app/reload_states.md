
# Reload States

By default the instance states will re-run everything at 10 minute intervals<br />
You may trigger an immediate new run at any time by clicking the `Reload States` button

## Github Service
Besides the `Reload States` button, you can also use our Github service to trigger a state rerun when a commit is pushed.

To enable this:
- open `API Token` in `Manage Workspace > Your Workspace`, and generate a token (only availeb for workspace admin.)
![](https://raw.githubusercontent.com/VisualOps/book-image/master/ide_settings_generate_token.jpg)
- open the `app`, find the app id in the `property panel`
![](https://raw.githubusercontent.com/VisualOps/book-image/master/ide_app_id.jpg)
- goto your Github repo page, click `Settings`, select `Webhooks & Services`, add `VisualOps` service
![](https://raw.githubusercontent.com/VisualOps/book-image/master/github_webhook_visualops.jpg)
- Done! next time when you push a new commit to the repo, a new state run will be triggered immediately

