# Keypair

While focusing on an instance, you can select the key-pair to use for this application

You have several options:

- Create a new key-pair (useful if you want to use a unique key for this instance, or app for example)
- Use an existing key-pair from your AWS account
- Import a key-pair from your computer
- Use no key-pair (useful in case of customs AMIs with specific password, that you already know)

Key pairs can be specified by instance, or by app, by selecting '$DefaultKeyPair' (default) in the properties panel of any instance

![](https://raw.githubusercontent.com/MadeiraCloud/docs-image/master/list_keys.png)

To manage your key-pair, click on 'Manage Region Key Pairs' in the properties panel of any instance

![](https://raw.githubusercontent.com/MadeiraCloud/docs-image/master/custom_keys.png)

***NOTE***: Upon launching a stack or updating an app, IDE will prompt you to specify an existing keypair as the replacement of the placeholder `$DefaultKeyPair`. All new instances in the stack/app with $DefaultKeyPair will be created using the specified keypair.

![](https://raw.githubusercontent.com/MadeiraCloud/docs-image/master/ide_ta_default_keypair.jpg)
