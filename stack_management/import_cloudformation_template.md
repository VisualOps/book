# Import CloudFormation template (Preview)

You can import CloudFormation templates into the IDE to visualize.

![](https://raw.githubusercontent.com/MadeiraCloud/docs-image/master/ide_stack_import_cfn.png)

## Prerequisite

The current release has some prerequisite on the CloudFormation templates to be imported:
- the template must not include any reference to existing VPC, Subnet or Security Group
- These components must be defined as complete new resources

To meet these requirements, you can edit the template as follow.

## Example
Here is the example in AWS, named is Template_1_SharePoint_2013.template.

![](https://raw.githubusercontent.com/MadeiraCloud/docs-image/master/ide_stack_import_cfn_sharepoint.png)


The VPC and subnets are defined in Parameters section which means it reference to the existing VPC and subnets.
In order to import this template, you have to do a little modification.
Move the VPC and subnet to Resources section and convert to a new resource like the following.

![](https://raw.githubusercontent.com/MadeiraCloud/docs-image/master/ide_stack_import_cfn_sharepoint2.png)


