# Team Management

Workspace has two type of roles: `Admin` and `Memeber`. When you create a new workspace, you will be `Admin`.

As `Admin`, you can:
- invite others to the workspace, who will be `Member`
- promote `Member` to `Admin`
- downgrade other `Admin` to `Member`
- delete a workspace (except `My Workspace`)
- configure the workspace's cloud access credential (AWS access keys)
- configure the workspace's billing information
- generate, edit, delete API token

Both can:
- leave the workspace (cannot leave if you are the last `Admin` in the workspace)
- full permission on all stacks in the workspace
- full permission on all apps in the workspace
- import existing cloud resources ([Import Existing VPC](../app/import.md))
- view API token
- view cloud usage report of the workspace

![](https://raw.githubusercontent.com/MadeiraCloud/docs-image/master/ide_workspace_team.jpg)<br />
