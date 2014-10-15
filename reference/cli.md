# CLI

``visualops`` is a command-line interface for VisualOps. It allows you to
deploy the same stack, or clone running apps to your laptop, for dev/testing/debugging purposes.

note: output shown in this documentation is indicative only, please do not refer to it.

Requirements
------------

Before install, ensure Docker is installed (see http://docs.docker.com) in version >= 1.2.0.

On Mac OS X, `boot2docker` is required.

Platform
--------

All Linux distributions supported by Docker should be compatible with VisualOps.
`Ubuntu`, `CentOS`, `Amazon Linux` and `RedHat Linux` (on their latest version) are officially suported.

> Mac is not fully supported yet (coming soon)

Install
-------

Preferred method of install is ``pip``:

    $ pip install visualops

Commands
--------

Check usage for detailed arguments:

    $ visualops --help

Use the help command to get help about one specific command:

    $ visualops help [command]


Notes
--------

- when launching a stack or cloning an app, only the `Docker` states will be executed; the other states will be ignored
- if you try to bind multiple containers to the same host port, only one container can be started with the correct port binding
