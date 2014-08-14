# (Instance) State

##### State
A (instance) state is a configuration statement of an instance. It is defined at the stack's design phase, and  applied to the instance at the runtime. A state should be [idempotent](http://en.wikipedia.org/wiki/Idempotence), as during the lifecycle of the app the app's state is consistently maintained. The state drift will be automatically fixed, so the app will *always* run in the desired state. (*If you are familiar with other DevOps tools, such as Puppet, you may find that a state is similar to Puppet manifest*)

![](https://raw.githubusercontent.com/MadeiraCloud/docs-image/master/ide_stack_states.png)

##### Modules
The complete state modules can be found [here](../state_modules/README.md).

##### Jinja syntax

The states editor is compatible with the [Jinja](http://jinja.pocoo.org/) syntax.

You can check out the [SaltStack documentation](http://docs.saltstack.com/en/latest/ref/renderers/all/salt.renderers.jinja.html) about the Jinja renderer for more details about it.




