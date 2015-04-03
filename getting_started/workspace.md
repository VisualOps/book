# Workspace

A workspace is a collaboration space where a team of members can work on a set of stacks and apps.

By default, we create a personal `My Workspace` for every user. Ther are some differences between `My Workspace` and `Team Workspace`:
- `My Workspace` is an individual workspace, which means that you cannot invite others to it
- For team collaboration, you can create new workspace, and invite your team to join
- In `My Workspace`, you can 3600 free credits per month, which is enough to run 5 instances for a month. However, no free credis is availale in other workspace
- `My Workspace` cannot be deleted
- For existing accounts, all stack/app are grouped into `My Workspace`. Please read [Transfer Stack / App between Workspaces](../workspatransfer_stack__app_between_workspaces), if you want to migrate

Each workspace can be configured with separate:
- cloud access credential, e.g. AWS access/secret key
- billing information
- API access token (check [Reload States](../app/reload_states.md) )

> **NOTE**: This means that ***all apps and resources in a workspace share the same credential, bill and API token***.

The workspace switch is located at the left-top corner in the IDE.
![](https://raw.githubusercontent.com/VisualOps/book-image/master/ide_workspace_switch.png)<br />


![](https://raw.githubusercontent.com/VisualOps/book-image/master/ide_workspace.png)<br />

