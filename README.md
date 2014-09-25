###Django depotapp

基于django的购物车应用，参照thinkinside的Django专栏教程编写http://blog.csdn.net/column/details/django.html，

###相关信息
+ window下eclipse开发

+ django版本1.4.1

+ python版本2.7.6

+ djangorestframework版本0.40（这里如有点问题,，请自己搜索解决）
+ 数据库：sqlite3 管理账户：root 密码：123456

###使用说明

这个版本是在windows下开发，现在我把它部署到了linux下,注意修改数据库路径"/srv/www/depot/sqlite.db"

+ [部署方法戳](http://peqiu.com/blog/centos-django-uwsgi-nginx.html)

+ [最后的效果戳](http://book.peqiu.com/depotapp/store/)
###内容介绍

内容已经基本上涵盖了Django开发的主要方面

 1 .从需求和界面设计出发，创建模型和修改模型

 2 . 并通过scaffold作为开发的起点；在scaffold的基础上重新定制模板，

 3 . 并且通过Model类和Form类对用户输入的数据进行校验。

 4 . 涉及到了单元测试。

 5 .为了提高开发用户界面的效率，更好地实现模板，还讨论了对静态资源（css，js，image等）的管理，并通过模板继承的方式实现了整个站点的统一布局。

 6 . 作为web应用必不可少的部分，还演示了如何使用会话（session）。
 
 7 . 在这些基础上增加了RESTful web service，将jquery集成到Django，并实现了ajax。后面还实现了Atom订阅，分页（Pagination)，Amin管理用户，权限控制，处理登录和注销


为了方便大家学习，把我写的源码传上来，大家也可以进行二次开发

















