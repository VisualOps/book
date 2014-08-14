## Connecting VisualOps with AWS
An Amazon Web Services account is necessary in order to get full functionality from VisualOps.

### 1. Entering Your Credentials
The next step is to enter your AWS account credentials in order for VisualOps to connect with AWS on your behalf.

You will be promped on your first connection to [VisualOps IDE](https://ide.visualops.io/). If not, or if you wish to update your credentials, login to [VisualOps IDE](https://ide.visualops.io/login/), then click on your username on the top-right corner

=> "Settings" => "AWS Credential" => "Update".

![](https://raw.githubusercontent.com/MadeiraCloud/docs-image/master/aws_cred.png)

You can find your AWS credentials by clicking [here](https://console.aws.amazon.com/iam/home?#security_credential).

After logging in, you can find your Account Number/Account ID in the __Account Identifiers__ section:

![](https://raw.githubusercontent.com/MadeiraCloud/docs-image/master/kb-connect-acc.png)

This is optional, but is required for some of our advanced features such as sharing an EC2 AMI or EBS snapshot with other users.

Use a valid Access Key and Secret Access Key. This is required in order to use AWS' Rest APIs to let you manage your AWS account through the VisualOps application.

Just copy and paste these three pieces of information into the AWS Credentials setting form, hit save and you are ready to go.

### 2. Connecting VisualOps and AWS Using IAM
#### 2.1 - Make sure IAM access is enabled.
Log in to your AWS account and then click [here](https://aws-portal.amazon.com/gp/aws/manageYourAccount).

![](https://raw.githubusercontent.com/MadeiraCloud/docs-image/master/kb-iam-active.png)

Scroll down to the IAM user access section and make sure that both the 'Account Activity Page' and 'Usage Reports Page' checkboxes are ticked and then click Activate Now.

#### 2.2 - Create a user for use with VisualOps.
Go to the AWS Console and click the [IAM tab](https://console.aws.amazon.com/iam/home), then create a group for your user. You can call it anything you like, we suggest making it something VisualOps related for ease of use

![](https://raw.githubusercontent.com/MadeiraCloud/docs-image/master/kb-iam-create-group.png)

Click 'Select' after 'Amazon EC2 Full Access'.

![](https://raw.githubusercontent.com/MadeiraCloud/docs-image/master/kb-iam-ec2-full.png)

Here you can review the permissions. If you are happy, click 'Continue'.

![](https://raw.githubusercontent.com/MadeiraCloud/docs-image/master/kb-iam-policy.png)

Click the 'Create New Users' tab and enter a name for your new user. Leave 'Generate an access key for each User' ticked and then click 'Continue'.

![](https://raw.githubusercontent.com/MadeiraCloud/docs-image/master/kb-iam-new.png)

Review your settings and click 'Finish'.

![](https://raw.githubusercontent.com/MadeiraCloud/docs-image/master/kb-iam-review.png)

The IAM account has now been created. Click 'Show User Security Credentials'.

![](https://raw.githubusercontent.com/MadeiraCloud/docs-image/master/kb-iam-cred.png)

You can now see the Access Key ID and Secret Access Key for this user.

Copy and paste these into the IDE and click 'Save' and you're connected!
