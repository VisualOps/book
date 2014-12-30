# Import CloudFormation template (Preview)

You can import CloudFormation templates into the IDE to visualize.

![](https://raw.githubusercontent.com/MadeiraCloud/docs-image/master/ide_stack_import_cfn.png)

## Prerequisite
The current release has some prerequisite so that CloudFormation templates can be imported:

- The resource in template which is not supported by VisualOps will be ignored.

- The template must not include any existing resource as follow:

    AWS::EC2::EBS::Volume
    
    AWS::EC2::EIP
    
    AWS::EC2::Instance
    
    AWS::EC2::SecurityGroup
    
    AWS::ELB
    
    AWS::EC2::NetworkAcl
    
    AWS::EC2::CustomerGateway
    
    AWS::EC2::NetworkInterface
    
    AWS::EC2::InternetGateway
    
    AWS::EC2::RouteTable
    
    AWS::EC2::Subnet
    
    AWS::EC2::VPC
    
    AWS::EC2::VPNConnection
    
    AWS::EC2::VPNGateway
    
    AWS::AutoScaling::Group
    
    AWS::AutoScaling::LaunchConfiguration
    
    AWS::AutoScaling::ScalingPolicy
    
    AWS::CloudWatch::CloudWatch
    
    AWS::RDS::DBInstance
    
    AWS::RDS::DBSubnetGroup

- If you want to import existing resource template, you need to convert it to a complete new component like following figure and fill in the connection between two component such as availability zone, subnet id so that our algorithm can find out the architecture of your template. 

![](https://raw.githubusercontent.com/MadeiraCloud/docs-image/master/ide_stack_import_cfn_sharepoint2.png)
- Even you finish above steps, you may still failed to import due to follwoing reason:

    The availability zone of the volume is not match with corresponed attached instance.
    
    The region you want to import do not match the availability zone you describe in the template
    
    Your template have more than 2 VPC component
    
    One of the component is missing AWS required property like subnet is missing property VpcId


