# Create the stack

Upon creating a new stack in VisualOps, you have two options: normal AWS stack, and Mesos stack. The Mesos stack comes with several options:

![](https://raw.githubusercontent.com/VisualOps/book-image/master/ide_mesos_stack.png)

- Scale:
  - small: 5 instances (1 CPU, 2GB Mem), with autoscaling up to 50 instances
  - medium: 50 instances (2 CPU, 3.75GB Mem), with autoscaling up to 200 instances
  - large: 200 instances (8 CPU, 15GB Mem), with autoscaling up to 1000 instances
- Region: select the region to deploy the cluster
- Framework：
  - Marathon: setup [Marathon](https://github.com/mesosphere/marathon) on top the Mesos cluster
