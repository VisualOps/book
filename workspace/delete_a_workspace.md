# Delete a workspace

> **NOTE**: cannot delete a workspace, if there is any outstanding bill

When `Admin` deletes a workspace, the following will happen:
- all stack will be deleted permantly
- all app will be deleted permantly, however **NO** cloud resources will be terminated
- all cloud resources in this workspace will continue to run, just "forgotten" by VisualOps
- you can re-import these resources into other workspaces
- all API token will be deleted permantly. API calls using any of these token will fail
- No furthure cost, though you may need to pay for the cost occurred
- cloud access credential and billing information will be removed from VisualOps

![](https://raw.githubusercontent.com/VisualOps/book-image/master/ide_workspace_delete.png)<br />
