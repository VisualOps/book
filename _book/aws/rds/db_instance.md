# DB Instance

>A DB instance is an isolated database environment running in the cloud. It is the basic building block of Amazon RDS. A DB instance can contain multiple user-created databases (SQL Server only allows one database per DB instance), and can be accessed using the same client tools and applications you might use to access a stand-alone database instance.

You can create new blank DB instance or create from the previous DB Snapshot in the resource panel:

![](https://raw.githubusercontent.com/MadeiraCloud/docs-image/master/ide_resource_rds_instance.png)

### Restore to Point In Time

To restore DB instance, make sure ***Automatic Backup*** is enabled:
![](https://raw.githubusercontent.com/MadeiraCloud/docs-image/master/ide_property_rds_backup.jpg)

To restore a DB instance with a previous backup：
- open the app
- click `Edit App`
- click the top of the DB instance and drag-n-drop to restore
![](https://raw.githubusercontent.com/MadeiraCloud/docs-image/master/ide_resource_rds_restore.jpg)

- specify the restorable time
![](https://raw.githubusercontent.com/MadeiraCloud/docs-image/master/ide_canvas_rds_restore.jpg)
- click `Apply` to apply the changes

You can find out the restorable time by checking the DB log & event:
![](https://raw.githubusercontent.com/MadeiraCloud/docs-image/master/ide_property_log_backup.jpg)
