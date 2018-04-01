# E-Shop
A project of E-commerce which is based on DjangoRestFramework.

Note about Django-RestFramework：

一、配置虚拟环境进行版本控制

1、安装 virtualenv：sudo pip install python-virtualenv
2、创建虚拟环境：virtualenv -p （py2或者py3的python路径） xxx         # 达成可控制版的要求
3、进入xxx虚拟环境 bin 
4、启动环境 source activate
5、退出环境 deactivate
*6、如果觉得启动步骤复杂 可以配置virtualenvwrrapper ：https://www.jianshu.com/p/2999e258cbf9

二、配置Django+DjangoRest Framework 
 
DjangoFramework官网：http://www.django-rest-framework.org/#

pip install django
pip install djangorestframework
pip install markdown       # Markdown support for the browsable API.
pip install django-filter  # Filtering support
pip install coreapi           #支持使用drf文档
pip install django-guardian 
pip inastall django-crispy-forms 

三、创建Django 项目

Pycharm 解释器选择 创建好的虚拟环境  创建Django项目

四、修改数据库设置

setting.py 切换数据库类型

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': "mxshop",
        'USER': "root",
        'PASSWORD':"123",
        'HOST': "127.0.0.1",
        'OPTIONS': {'init_command': 'SET default_storage_engine=INNODB;’}#INNODB是数据库存储
#引擎，由于需要引入第三方登录，那就需要INNODB而默认的是
    }
}

安装 mysqlclient   进入虚拟环境：pip install mysqlclient 肯定会出错（亦或是mysql_python）
这时候网上都是垃圾博客
* You installed python
* You did brew install mysql
* You did export PATH=$PATH:/usr/local/mysql/bin（that is the most important）
* And finally, you did pip install MySQL-Python 
trust Stack Overflow！！

五、在主项目下创建包apps 来存放应用
         将user直接拖拽到apps下
	 再创建一个extra_apps 用来管理存放第三方apps 或者修改一些包的源码需要
（将apps和extra_apps mark成 source root   会在后面给import带来方便）
	 然后创建Dir media用来存放图片、视频等   以及templates用来存放静态文件
	 创建db_tools 来存放python脚本，可以是处理数据库初始化，或者是web的脚本
将setting.py里这里
改为：
For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))
sys.path.insert(0, os.path.join(BASE_DIR, 'extra_apps'))
￼
所得到的效果：可以在引用apps和extra_apps下的对象时候可以直接import
从而得到基本目录

-------------------2018年03月29日22:42:49---------------------------

Restful Api 操作标准：http://www.ruanyifeng.com/blog/2014/05/restful_api.html

-------------------2018年03月30日22:47:29---------------------------


A many-to-one relationship. Requires two positional arguments: the class to which the model is related and the on_delete option.

and the ForeignKey.on_delete documentation:

When an object referenced by a ForeignKey is deleted, Django will emulate the behavior of the SQL constraint specified by the on_delete argument.

Pick one from the available options (models.CASCADE, models.PROTECT, models.SET_NULL, models.SET_DEFAULT, models.SET() or models.DO_NOTHING)

The parameter is required as of Django 2.0. In previous Django versions, the argument was optional and defaulted to models.CASCADE.

If you were used to the old behaviour, just set it to the old default:

board = models.ForeignKey(Board, models.CASCADE, related_name='topics')
starter = models.ForeignKey(User, models.CASCADE, related_name='topics')

ps. https://docs.djangoproject.com/en/2.0/ref/models/fields/#django.db.models.ForeignKey.on_delete
    http://www.django-rest-framework.org/


-------------------2018年03月31日23:50:32------------------------

API Guide
DjangoFilterBackend
The django-filter library includes a DjangoFilterBackend class which supports highly customizable field filtering for REST framework.

To use DjangoFilterBackend, first install django-filter. Then add django_filters to Django's INSTALLED_APPS

pip install django-filter
You should now either add the filter backend to your settings:

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',)
}
Or add the filter backend to an individual View or ViewSet.

from django_filters.rest_framework import DjangoFilterBackend

class UserListView(generics.ListAPIView):
    ...
    filter_backends = (DjangoFilterBackend,)
If all you need is simple equality-based filtering, you can set a filter_fields attribute on the view, or viewset, listing the set of fields you wish to filter against.

class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('category', 'in_stock')
This will automatically create a FilterSet class for the given fields, and will allow you to make requests such as:

http://example.com/api/products?category=clothing&in_stock=True
For more advanced filtering requirements you can specify a FilterSet class that should be used by the view. You can read more about FilterSets in the django-filter documentation. It's also recommended that you read the section on DRF integration.

SearchFilter
The SearchFilter class supports simple single query parameter based searching, and is based on the Django admin's search functionality.

When in use, the browsable API will include a SearchFilter control:

Search Filter

The SearchFilter class will only be applied if the view has a search_fields attribute set. The search_fields attribute should be a list of names of text type fields on the model, such as CharField or TextField.

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('username', 'email')
This will allow the client to filter the items in the list by making queries such as:

http://example.com/api/users?search=russell
You can also perform a related lookup on a ForeignKey or ManyToManyField with the lookup API double-underscore notation:

search_fields = ('username', 'email', 'profile__profession')
By default, searches will use case-insensitive partial matches. The search parameter may contain multiple search terms, which should be whitespace and/or comma separated. If multiple search terms are used then objects will be returned in the list only if all the provided terms are matched.

The search behavior may be restricted by prepending various characters to the search_fields.

'^' Starts-with search.
'=' Exact matches.
'@' Full-text search. (Currently only supported Django's MySQL backend.)
'$' Regex search.
For example:

search_fields = ('=username', '=email')
By default, the search parameter is named 'search', but this may be overridden with the SEARCH_PARAM setting.

For more details, see the Django documentation.

OrderingFilter
The OrderingFilter class supports simple query parameter controlled ordering of results.

Ordering Filter

By default, the query parameter is named 'ordering', but this may by overridden with the ORDERING_PARAM setting.

For example, to order users by username:

http://example.com/api/users?ordering=username
The client may also specify reverse orderings by prefixing the field name with '-', like so:

http://example.com/api/users?ordering=-username
Multiple orderings may also be specified:

http://example.com/api/users?ordering=account,username
Specifying which fields may be ordered against
It's recommended that you explicitly specify which fields the API should allowing in the ordering filter. You can do this by setting an ordering_fields attribute on the view, like so:

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = ('username', 'email')
This helps prevent unexpected data leakage, such as allowing users to order against a password hash field or other sensitive data.

If you don't specify an ordering_fields attribute on the view, the filter class will default to allowing the user to filter on any readable fields on the serializer specified by the serializer_class attribute.

If you are confident that the queryset being used by the view doesn't contain any sensitive data, you can also explicitly specify that a view should allow ordering on any model field or queryset aggregate, by using the special value '__all__'.

class BookingsListView(generics.ListAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = '__all__'
Specifying a default ordering
If an ordering attribute is set on the view, this will be used as the default ordering.

Typically you'd instead control this by setting order_by on the initial queryset, but using the ordering parameter on the view allows you to specify the ordering in a way that it can then be passed automatically as context to a rendered template. This makes it possible to automatically render column headers differently if they are being used to order the results.

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = ('username', 'email')
    ordering = ('username',)
The ordering attribute may be either a string or a list/tuple of strings.



-------------------2018-04-01 22:26:49------------------------










￼
￼
