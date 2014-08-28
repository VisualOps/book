## How it works

### Workflow
- Drag-n-drop resources to design the infrastructure
- Click instances to setup the software configuration; package, file, code, etc.
- Launch the app, within minutes the app is ready to use

Then, **VisualOps manages your app 24/7 to ensure that the app always run in the desired state, by continually monitor the infrastructure and the app, to instantly spot and fix any drift**.

![](https://raw.githubusercontent.com/MadeiraCloud/docs-image/master/workflow.gif)

### Concept

In VisualOps:

> **STACK** : a stack is the template of an application spec, containing everything that's needed to run it, i.e. resource spec (servers, storage, network) and software configuration (package, code, files and data, etc.), in a static and re-usable form.


> **APP** : you can launch a stack into an app:all of its infrastructure will be provisioned and instances will be configured as specified in the stack. You can launch multiple apps from the same stack, there would be no conflicts among all apps.

> **(INSTANCE) STATE** : A (instance) state is a configuration statement of an instance. It is defined at the stack's design phase, and  applied to the instance at the runtime. A state should be [idempotent](http://en.wikipedia.org/wiki/Idempotence), as during the lifecycle of the app the app's state is consistently maintained. The state drift will be automatically fixed, so the app will *always* run in the desired state. (*If you are familiar with other DevOps tools, such as Puppet, you may find that a state is similar to Puppet manifest*)

> **Link**: Link gives the way to connect and coordinate different services across multiple instances to setup a distributed app. One example is to connect web_server->db_server using: ****@{db_server.PrivateIpAddress}**** in the web_server's configurtion file.

### IDE

![](https://raw.githubusercontent.com/MadeiraCloud/docs-image/master/ide_stack_all.png)<br />

VisualOps IDE is the visual console for you to build and manage the cloud application.

The following sections explains the main components in VisualOps IDE:

- [Dashboard](./dashboard.md)
- [Stack](./stack.md)
- [(Instance) State](./instance_state.md)
- [Link](./link.md)
- [App](./app.md)
- [Account Setting](./account_setting.md)

