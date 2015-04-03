# Cloud Credential
An Amazon Web Services account is necessary in order to get full functionality from VisualOps. 

Each workspace can set up one Cloud Credential. By default, workspace is in "Demo Mode" when no cloud credential is provided yet. In demo mode, you can do all stack operations. Yet you are required to provide your cloud credential to show live resource in Dashboard, Import VPC, or Run App.

Only admin of a workspace has access to Cloud Credential section.
 
![](https://raw.githubusercontent.com/VisualOps/book-image/master/ide_workspace_credential_demo.png)

### 1. Set up Cloud Access Credential

In demo mode, open Workspace Setting > Cloud Access Credential, and click "Set up Cloud Access Credential".

![](https://raw.githubusercontent.com/VisualOps/book-image/master/ide_workspace_credential_add.png)

In the following popup, give your credential a freindly name in Credential Alias. And then provide the access credential of your AWS account. Note that the credential should at least have read access to AWS EC2 resources. To run app, write access is required.

### 2. Update Cloud Access Credential

You can update your cloud access credential by openning the dropdown from upper right corner of the credential item.

![](https://raw.githubusercontent.com/VisualOps/book-image/master/ide_workspace_credential_dropdown.png)

### 3. Delete Cloud Access Credential 

You can remove your cloud access credential from VisualOps. The "Delete" option is only available when there is no app in this workspace. You can either forget the apps from VisualOps (leaving resources untouched), or terminating all apps before deleting cloud access credential.
