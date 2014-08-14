# FAQ

Q: What is [VisualOps](http://www.visualops.io)?

>VisualOps is a visual DevOps automation tool. It automates the tasks of resource provisioning, code deployment and configuration management, to ensure your cloud application always runs in the desired state.

>VisualOps is created with the goal of being super **easy to understand** alongside giving you **total control**. We believe these two factors are imperative for any level of users in adopting a technology, whether you are running an individual project, startup, ISV, enterprise or anything in between. VisualOps is ideal for managing small setups with a handful of instances as well as highly complex environments with thousands.

Q: How does [VisualOps](http://www.visualops.io) work?

>1. Drag-n-drop components to build your AWS infrastructure
2. Click onto instances and use the built-in editor to setup the software configuration (package, conf file, code, etc.)
3. One click to deployment, within minutes the app is ready to use
4. **VisualOps ensures the app always runs in the defined states, by repeatedly continually the instance configuration and fixing any drift**

Q: What are the uses?

> You can currently use VisualOps for the following activities:
>
  1. **Template-Based Provisioning**: fast and repeatable Dev/QA, Demo environment setup
  2. **Continuous Deployment**: launch your stack into a running app, VisualOps deploys your code and automatically upgrades it once there is a newer version
  3. **App Ensure**: design, launch and relax. VisualOps will ensure your app is always up & running, in the state you defined

Q: What is the main difference between [VisualOps](http://www.visualops.io) and other DevOps tools?

>Compared with the traditional DevOps solutions, VisualOps avoid problems like：

>- Needing to learn a new and complex tool/DSL
- Having to write the recipes manually
- Hosting and operating a configuration manager master server, like Puppet or Chef, for example
- Needing to integrate with the other services, like CloudFormation
- **VisualOps gives you a clear view of how your system is setup, as well as offering in depth details of how each instance is configured**

Q: What is the main difference between [VisualOps](http://www.visualops.io) and [CloudFormation](http://aws.amazon.com/cloudformation/)?

> In terms of template-based deployment, VisualOps does share a similar goal as CloudFormation. In this regard, despite the visual part, you can use VisualOps as you use CloudFormation. However the key difference is that VisualOps doesn't merely manage the lifecycle of the infrastructure (provision, update, destroy, etc.) it continuously manages the application running on top of it. If some state drift occurs, VisualOps will spot the issue, fix it and return the system back to the desired state.

Q: What is the main difference between [VisualOps](http://www.visualops.io) and [OpsWorks](http://aws.amazon.com/opsworks/)?

> "AWS OpsWorks is an application management service that makes it easy for DevOps users to model and manage the entire application" [[1]](http://aws.amazon.com/opsworks/). OpsWorks is tightly entwined with [Chef](http://www.getchef.com/), which can be both a significant advantage/disadvantage. Compared with OpsWorks/Chef's bottom-up approach, VisualOps takes a different route. First focus on the infrastructure level, then use the visual [IDE](https://ide.visualops.io) to design the architecture; then drill down into the servers to configure and connect them. We believe this is the best approach of the DevOps toolchain: **system architecture first, then server details**.

Q: How much will it cost?

> VisualOps is currently FREE to use. We will keep you informed about when we will be releasing the full price plan. However we will be keeping the design feature as free, and then will price by the number of managed apps/resources.
Interested? Then sign up for free now. As we are in fairly early stages we are most interested in attracting those people who’s feedback can help us evolve into an evermore useful and beneficial tool.



Q: What about the security?

> We continue to put enormous effort into toughening up our security.

> - Everything is encrypted
We encrypt all data at every step of the way: your data is firstly encrypted in the browser, then transmitted via 256-bit Comodo SSL, and stay encrypted in the database. Even in the log files, your sensitive information, such as username, email address, are logged in the encrypted format.

> - Verified by AWS
We are an official technical partner for Amazon Web Services. We are hosted on AWS as well, which achieved ISO 27001 certification, PCI DSS Level 1 compliance, and SAS70 Type II.

> - Strict security processes
Abiding by strict security processes our team members never decrypt any user data without explicit permission being given or a request made directly from the user (mostly for support cases). Furthermore no staff member has the ability to decrypt any data, unless also granted permission by our security officer.

Q: Which AWS services do you currently support? What about the others (say RDS)?

> Right now, EC2, EBS, ELB, AutoScaling and VPC are supported. Take a look at [our roadmap](https://trello.com/b/wQdmsmp0/visualops-idea) for other services we support. Of course, your feedback, reviews and comments will help us greatly in prioritizing our work.

Q: Do you support EC2-Classic and Default VPC?

> We support custom VPC only. Please see [our blog article](http://blog.visualops.io/2014/02/18/vpc-always-forget-about-the-rest/) to learn why.

Q: Can I upload my CloudFormation scripts and have them visualized in the IDE?

> We support the CloudFormation export feature, and plan to support the import feature in the near future. [We'll do](https://trello.com/c/Ro23G4sR/62-cloudformation-import)



[1] http://aws.amazon.com/opsworks/

