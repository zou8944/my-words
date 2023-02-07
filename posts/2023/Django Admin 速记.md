---
created_at: 2023-02-06 17:24:12
updated_at: 2023-02-06 17:24:12
slug: django-admin-shorthand
---

> 作为Python平台上的约定类框架，Django Admin因为可以非常方便地管理数据表而经常被我们使用。尽管功能强大，但动辄好几个月的使用间隔会让重新上手时不知所措。这里针对常用case进行速记。

## 创建项目

安装django-admin命令行工具，创建项目

```shell
django-admin startproject <project_name>
```

## 多应用

一个项目可以管理多个数据源，每个数据源作为一个应用，步骤如下

- 创建应用

  ```shell
  python manage.py startapp <app_name>
  ```

- 定义数据库路由器，参考手册：https://docs.djangoproject.com/en/4.1/topics/db/multi-db/#an-example

- 修改settings.py，主要是 DATABASES 和 DATABASE_ROUTERS、INSTALLED_APPS

  ```python
  DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.postgresql_psycopg2',
          'NAME': 'xxx',
          'USER': 'xxx',
          'PASSWORD': 'xxx',
          'HOST': 'xxx',
          'PORT': 5432,
      },
  	  # 添加app的数据源
      '<app_name>': {
          'ENGINE': 'django.db.backends.postgresql_psycopg2',
          'NAME': 'xxx',
          'USER': 'xxx',
          'PASSWORD': 'xxx',
          'HOST': 'xxx',
          'PORT': 5432,
      },
  }
  
  # 指定数据库路由器
  DATABASE_ROUTERS = ['<上一步定义的router>']
  # 安装新增的app
  INSTALLED_APPS.append("<app_name>")
  ```

## 默认数据源

Django Admin的用户、鉴权相关表格都放在default数据源下。即DATABASES中key为default的数据源

## Model

### 生成Model

存在多个app时，可以只从单个app的数据源生成Model

```shell
python manage.py inspectdb --database <app_name>
```

### Model迁移

迁移指根据model.py中定义的模型对数据库进行修改。一般需要有两个步骤

- makemigrate，生成数据库迁移python脚本
- migrate，执行迁移

这意味着数据库的表结构会随着Django Admin项目的model定义变化。在我们的使用场景下这显然是不合理的：每个app有自己的数据表管理方式，Django Admin项目仅仅作为表数据查看和修改的窗口。

为了解决这个问题，**在migrate时加上 --run-syncdb 参数**：对库中已存在的表，migrate不会做创建和修改操作。

### 可以不migrate吗

不可以。至少在model刚定义时候需要migrate一次

migrate除了应用model的修改，还会将新增的model表增加到权限表。如果不migrate，在用户权限管理则不会存在对应model的权限。这意味着只有管理员才能看到该应用。

![image-20230206161951029](https://gdz.oss-cn-shenzhen.aliyuncs.com/local/image-20230206161951029.png)

### Model元数据

Model类允许定义内部类，指明一些元数据，比如

```python
class User(models.Model):
  	# ... ...

    class Meta:
        managed = False
        db_table = 'user'
        verbose_name = '用户'
        verbose_name_plural = '用户'
```

- managed：是否受Django Admin的migrate管理。设置为否时，migrate会忽略对该model的所有操作
- db_table：Model对应的数据表名
- verbose_name：Model在页面显示的单数名称。默认的复数名称会在后面直接加s
- verbose_name_plural：Model在页面显示的复数名称

### 自定义字段

在Model类中定义方法，在显示时引用，能够显示该方法的返回值，比如下面这个Model定义

```python
class Resource(models.Model):
    # ......
    data = models.JSONField()

    def belong_time(self):
        if 'belong_time' in self.data:
            return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(self.data['belong_time']/1000))
        else:
            return ''
```

ModelAdmin中使用时如下

```python
@admin.register(Resource)
class ResourceAdmin(GeneralAdmin):
    list_display = ['id', 'type', 'user_id', 'data', 'belong_time', 'updated_time']
```

### 表关联 - 外键

外键关联在Django Admin中有很多好处，典型的可以做内联。即如果A表记录是B表记录的外键，则B表的详情页中，可以直接编辑或查看A表记录，而不必再单独到A表搜索。一个外键定义如下

```python
class Subscription(models.Model):
    id = models.BigIntegerField()
    user_id = models.BigIntegerField(primary_key=True)
    # ... ...

class SubscriptionHistory(models.Model):
    id = models.BigIntegerField(primary_key=True)
    subscription = models.ForeignKey(Subscription, db_column='user_id', on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'subscription_history'
```

- 外键不一定需要真的在数据库中存在。我们可以将具有一对多关联的两个表声明称外键关系，以享受其带来的便利。
- 外键字段默认为 xxx_id，外键对应的字段为xxx.id，比如user表的id字段是blog表的外键，外键字段名为blog.user_id，且要求user.id必须声明为主键
- 上述规则中外键字段名可以修改，上述例子中，我们将subscryption的user_id和subscryption_history表的user_id字段作为外键关联

## Model管理

### 基本属性

- list_display：列表页显示的列名
- list_editable：列表页可以编辑的列名
- list_filter：列表页中可以通过下拉选过滤的列。列表页顶部会出现下拉选框，下拉选的内容是对应字段做select distinct 的结果。所以**需要注意到设置该字段会带来的额外查询负担**
- fields：详情页显示的列名，默认显示所有
- readonly_fields：详情页的只读字段（详情页除主键外默认所有字段都是可编辑的）
- search_fields：列表页顶部出现一个搜索框，该搜索框输入的内容作为哪些字段的搜索依据。
  - 设置多个field时，它们之间是or关系
  - 默认是模糊匹配，写成'=\<field>'为精确匹配
  - 因为 Django Admin 本身的支持问题，搜索框无法自定义place holder
- date_hierachy：在列表页顶部显示日期层级面包屑，该字段指明日期数据来源
- ordering：列表显示结果按照哪些字段排序。负号表示倒序
- list_per_page：每页显示多少条数据，默认为 100

### 自定义显示字段

前面说了Model中自定义的方法可以作为自定义字段显示。ModelAdmin中自定义方法也可以作为自定义字段显示

```python
@admin.register(User)
class UserAdmin(GeneralAdmin):
    list_display = ['id', 'image_url']
    
    # ... ...
    
    def image_url(self, obj):
      absolute_url = obj.avatar
      return format_html(
        f'<img src={self.default_thumbnail_url(absolute_url)} height="70px" width="70px">')
```

### 自定义ListFilter

list_filter字段可以是自定义的，只要定义好下拉选内容来源(重写lookups方法)、查询方法即可

```python
class CommentListFilter(admin.SimpleListFilter):
    title = "评论状态"
    parameter_name = 'state'

    # 下拉选的内容
    def lookups(self, request, model_admin):
        return (
            ('0', "待审核"),
            ('1', "通过"),
            ('2', "未通过"),
            ('3', "已删除"),
        )

    # 点击搜索时对queryset增加的查询条件
    def queryset(self, request, queryset):
        # 获取state状态
        if self.value() == '0':
            return queryset.filter(state=0, deleted_time=None)
        if self.value() == '1':
            return queryset.filter(state=1, deleted_time=None)
        if self.value() == '2':
            return queryset.filter(state=2, deleted_time=None)
        if self.value() == '3':
            return queryset.exclude(deleted_time=None)

          
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
  	# ... ...
    list_filter = (CommentListFilter,)
```

### 自定义action

列表页顶部会显示一个操作列表，可通过如下方式向列表中增加操作

```python
def re_count_commented_in_video(video_id: str):
    video = Video.objects.filter(id=video_id).first()
    video.commented_count = Comment.objects.filter(video_id=video_id, state=1).count()
    video.save()


def re_count_comment(commentQueryset):
    for comment in commentQueryset.all():
        re_count_commented_in_video(comment.video_id)


def all_review(modeladmin, request, queryset):
    queryset.update(state=0)
    re_count_comment(queryset)


all_review.short_description = "标记为“待审核”"


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    评论管理
    """
    # 批量操作
    actions = [all_review]

```

### 自定义html组件样式

显示字段时，每一种Model的filed类型都有固定的html元素样式对应，比如Text类型对应\<textarea>元素。可以通过如下方式自定义

```python
@admin.register(Location)
class LocationAdmin(GeneralAdmin):
    # 为每种Model字段类型指定对应的html组件
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '5'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 1, 'cols': 40})},
    }
```

### 禁用删除和添加

重写如下方法能够禁用删除和添加action

```python
@admin.register(User)
class UserAdmin(GeneralAdmin):

		# 禁用删除
    def has_delete_permission(self, request, obj=None):
        return False

    # 禁用添加
    def has_add_permission(self, request, obj=None):
        return False
```

### 内联

在Model满足外键关系的情况下，可按照如下方式定义内联效果

```python
class SubscriptionHistoryInline(admin.TabularInline):
  	# 显示哪些字段
    fields = ['order_id', 'subscription_type', 'membership_level', 'created_at', 'source_type', 'comment']
    # 是否显示多一行空行，方便快速添加记录
    extra = 0
    # 内联的目标Model
    model = SubscriptionHistory


class SubscriptionRefundHistoryInline(admin.TabularInline):
    fields = ['order_id', 'refund_time', 'created_time']
    extra = 0
    model = SubscriptionRefundHistory


@admin.register(Subscription)
class SubscriptionAdmin(GeneralAdmin):
  	# 注意这里内联的是上面定义的内联对象，不是Model
    inlines = [
        SubscriptionHistoryInline,
        SubscriptionRefundHistoryInline
    ]
		# ... ...
```

## 创建API

- view中定义请求处理方法

  ```python
  # csrf_exempt 注解可以忽略csrftoken的校验
  @csrf_exempt
  def encrypt_content(request):
      content = request.body.decode()
      cmd = os.getcwd() + "/encryption -enc -str " + content
      encrypted_content = os.popen(cmd).read()
      return HttpResponse(encrypted_content)
  ```

- 做urls.py中做映射

  ```python
  urlpatterns = [
    	# ... ...
      path('api/encrypt', meiji_app.views.encrypt_content),
  ]
  ```

## 增加自定义页面

如果需要在某个应用下添加一个自定义入口，指向自定义页面。可以定义空Model和ModelAdmin，然后在ModeAdmin中重写changelist_view，将默认view指向自定义的view。具体如下

- 在目标app目录下创建 templates 目录，并添加模板html，比如下面这样

  ![image-20230206165937760](https://gdz.oss-cn-shenzhen.aliyuncs.com/local/image-20230206165937760.png)

- settings.py中将该templates路径添加到模板目录

  ```python
  TEMPLATES = [
    {
      'BACKEND': 'django.template.backends.django.DjangoTemplates',
      # 关键是这行
      'DIRS': [BASE_DIR / 'templates'],
      'APP_DIRS': True,
      'OPTIONS': {
        'context_processors': [
          'django.template.context_processors.debug',
          'django.template.context_processors.request',
          'django.contrib.auth.context_processors.auth',
          'django.contrib.messages.context_processors.messages',
        ],
      },
    },
  ]
  ```

- views.py中定义方法。这里的关键是 render_to_string 方法，其能够将模板直接转换为字符串，方便直接返回客户端

  ```python
  def tool(request):
      return HttpResponse(render_to_string("tool.html", request=request))
  ```

- 定义空Model

  ```python
  class Tool(models.Model):
  
      class Meta:
          verbose_name = '工具'
          verbose_name_plural = '工具'
  ```

- 定义ModelAdmin，将列表view换到上面自定义的view

  ```python
  @admin.register(Tool)
  class ToolAdmin(GeneralAdmin):
      def changelist_view(self, request, extra_context=None):
          return tool(request)
  ```

能够得到如下效果

![image-20230206170312741](https://gdz.oss-cn-shenzhen.aliyuncs.com/local/image-20230206170312741.png)

## 容器化

给一个能用的Dockerfile

```dockerfile
FROM python:3.10

COPY requirements.txt .

RUN sed -i 's/deb.debian.org/mirrors.ustc.edu.cn/g' /etc/apt/sources.list && \
    sed -i 's/security.debian.org/mirrors.ustc.edu.cn/g' /etc/apt/sources.list

RUN apt update -y
RUN apt install libsasl2-dev python-dev libldap2-dev libssl-dev vim -y
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt


COPY . .

WORKDIR .
EXPOSE 8969
ENV PORT=8969

ENV PYTHONPATH=/

# kubernets只会将环境变量传给bash，直接用sh启动很可能拿不到环境变量
RUN  ln -sf /bin/bash /bin/sh

# 受管理的app数据库都由app本身管理，因此不能将本系统的model修改应用上去，需要加上 --run-syncdb 参数
CMD ["sh", "-c", "python mampod/manage.py migrate --run-syncdb && python mampod/manage.py runserver 0.0.0.0:8969"]

```

### 健康检查

可以使用 [django-health-check](https://github.com/revsys/django-health-check) 增加一个健康检查接口。按照其配置，健康检查接口为：localhost:8000/ht/