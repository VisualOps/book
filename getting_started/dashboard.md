# Dashboard

The dashboard is a control center where you can control both your VisualOps activity and your AWS account activity and resources.

![](https://raw.githubusercontent.com/MadeiraCloud/docs-image/master/ide_dashboard_all.png)<br /><br />

##### Stack creation button
A 'Create new Stack' button has been implemented to help you create new Stacks with VisualOps IDE. You can find it at the top left of the dashboard<br /><br />
![](https://raw.githubusercontent.com/MadeiraCloud/docs-image/master/ide_dashboard_newstack.png)<br />

##### Import stack button
The 'Import stack' button allows you to import previously created stacks to the IDE<br /><br />
![](https://raw.githubusercontent.com/MadeiraCloud/docs-image/master/ide_dashboard_importstack.png)<br />

##### Import VPC
The 'Import VPC' button helps you to import your existing VPCs as app into VisualOps.<br /><br />
![](https://raw.githubusercontent.com/MadeiraCloud/docs-image/master/ide_dashboard_visuvpc.png)<br />

#### Main View
![](https://raw.githubusercontent.com/MadeiraCloud/docs-image/master/ide_dashboard_main.png)<br /><br />
The 'Main View' is the top view of the dashboard, showing the number of Apps and Stacks in every AWS region. The 'Main View' is always displayed in the dashboard

#### Global
![](https://raw.githubusercontent.com/MadeiraCloud/docs-image/master/ide_dashboard_global.png)<br /><br />
The global view is an overview of the costly AWS resources in all AWS regions<br />
This view helps to quickly determine which resources are currently in use and will generate cost

As you can see above:

- [Running Instances](http://aws.amazon.com/ec2/instance-types/)
- [Elastic IPs](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html)
- [Volumes (EBS)](http://aws.amazon.com/ebs/)
- [Load Balancers (ELB)](http://aws.amazon.com/elasticloadbalancing/)
- [VPNs](http://aws.amazon.com/vpc/)

note: VPCs are inexpensive, however VPN connections to VPCs are more costly

note2: EIP are free if associated to any instance. If this instance is stopped, your EIP will generate cost

#### Region View
![](https://raw.githubusercontent.com/MadeiraCloud/docs-image/master/ide_dashboard_region.png)<br /><br />
The region specific view is an overview of different resources in a specific region

This view is separated in two parts:

- The App/Stack view: You can see here the App and Stack created in this specific region using VisualOps IDE
- The AWS resources view: You can see here the details of the most relevant AWS resources, whether or not created with VisualOps IDE

#### Resource Details
You can get more details about a specific resource by clicking on the 'Detail' icon, on the right of each resource. This will display all required information about the resource

For example, for an instance:<br />
![](https://raw.githubusercontent.com/MadeiraCloud/docs-image/master/ide_dashboard_ami.png)

