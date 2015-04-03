
# Create the stack

When creating a new stack, you can choose the stack type: normal AWS stack, or Mesos stack (running on AWS too).

![]()

- Scale: three predefined cluster sizes for quickstart

    - small: 5 instances by default (1 CPU, 2GB Mem), with auto-scaling up to 50
    - medium: 50 instances by default (2 CPU, 3.75GB Mem), with auto-scaling up to 200
    - large: 200 instances by default (8 CPU, 15GB Mem), with auto-scaling up to 1000

- Region: select the AWS region to deploy
- Framework:

    - Marathon: when enabled, [Marathon](https://github.com/mesosphere/marathon) will be automatically setup on top of the Mesos cluster
