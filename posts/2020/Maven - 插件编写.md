---
created_at: 2020-02-29 16:03:23.0
updated_at: 2021-02-16 23:23:09.804
slug: maven-write-a-plugin
tags: 
- Maven
---

Maven是个很好用的打包编译工具，也是目前自己正在使用的主力工具。对一些个性化的需求，编写插件，实现一些特有的功能，还是非常有效的。这次刚好，有需求如是：maven编译时用到数据库表描述文件自动生成插件，需要从配置文件中读取账号密码，而目前maven只提供了读取properties文件到声明周期的工具。而项目的通用配置文件是json，如果临时加一个重复的properties文件，显得多余且没必要。于是需求应运而生，开发一个读取json文件到Maven生命周期的工具。

我叫它 json-loader-maven-plugin。

<!--more-->

首先创建一个maven空工程，我们从已有的Maven工程开始。

## pom配置

### 基础信息

基础信息和普通项目没什么两样，需要注意的点如下

- groupId: 组织ID，具有权威性，由于是github中的项目，所以命名为com.github.用户名
- artifactId: Apache规定，凡是Maven插件命名必须以 maven-plugin结尾
- packagin: 此处开发插件，因此打包类型为 maven-plugin

```xml
  <modelVersion>4.0.0</modelVersion>
  <groupId>com.github.zou8944</groupId>
  <artifactId>json-loader-maven-plugin</artifactId>
  <packaging>maven-plugin</packaging>
  <version>1.0.0</version>
```

### 依赖

我们会用到Maven Plugin API ，插件相关注解，比如@Mojo，还会用到单元测试（这里使用JUnit）。再加上解决的一些依赖问题，得到必备的依赖项如下

```xml
  <dependencies>
    <!-- 基础组件 -->
    <dependency>
      <groupId>org.apache.maven</groupId>
      <artifactId>maven-plugin-api</artifactId>
      <version>3.6.2</version>
    </dependency>
    <!-- 插件注解 -->
    <dependency>
      <groupId>org.apache.maven.plugin-tools</groupId>
      <artifactId>maven-plugin-annotations</artifactId>
      <version>3.6.0</version>
      <scope>provided</scope>
    </dependency>
    <!-- maven project API，提供运行的整个project的各种API，比如读取和动态设置依赖项等 -->
    <dependency>
      <groupId>org.apache.maven</groupId>
      <artifactId>maven-project</artifactId>
      <version>2.2.1</version>
    </dependency>
    <!-- 为解决依赖问题而加，必须和maven-project保持同一版本-->
    <dependency>
      <groupId>org.apache.maven</groupId>
      <artifactId>maven-artifact</artifactId>
      <version>2.2.1</version>
    </dependency>
    <!-- 单元测试 -->
    <dependency>
      <groupId>junit</groupId>
      <artifactId>junit</artifactId>
      <version>4.13</version>
      <scope>test</scope>
    </dependency>
    <!-- 用于读取json文件 -->
    <dependency>
      <groupId>com.alibaba</groupId>
      <artifactId>fastjson</artifactId>
      <version>1.2.61</version>
    </dependency>
  </dependencies>
```

## 编写Mojo

Mojo是插件执行的目标类，在使用时和\<goal>标签对应，一个插件可以有多个Mojo。

对Mojo的编写，一般集成AbstractMojo类，它实现了Mojo接口的必要方法，只留下一个execute()方法让我们编写业务逻辑。同时我们为定义的类加上@Mojo注解，Maven在运行时就能够检测到它。

```java
@Mojo(name = "read-project-json-to-properties", defaultPhase = LifecyclePhase.INITIALIZE)
public class ReadJsonMojo extends AbstractMojo {

  // 注入Maven环境
  @Parameter(defaultValue = "${project}", readonly = true, required = true)
  private MavenProject project;

  // 注入参数
  @Parameter
  private File[] files;

  @Override
  public void execute() throws MojoExecutionException, MojoFailureException {
    try {
      // 将文件解析为properties对象
      Properties properties = parseFileProperties(files);
      // 将解析的properties对象加入到project实例中
      project.getProperties().putAll(properties);
    } catch (IOException e) {
      throw new MojoExecutionException("Error reading json from " + resource, e);
    }
  }
}
```

上述代码是简化后的，目的是为了关注到插件的实现上，而不是业务逻辑。针对这段代码，有如下几点说明

- @Mojo

  指定了Mojo名，对应goal，可设置默认工作的生命周期节点。

- MavenProject属性，代表了pom.xml下的`<project>`标签下的所有内容，即Maven的运行环境。在Maven上下文创建时将会被注入。

- File属性，Maven支持直接将pom文件中指定的路径直接解析成File并注入Mojo类。除了File，还支持如下类型，而他们，都是通过@Parameter注解实现的。

  - Boolean
  - Integer
  - Float-Point
  - Date
  - File
  - URL
  - Plain text
  - Enum
  - Array
  - Collection
  - Map
  - Properties
  - Object class

  具体的使用方法，可以参考[官方文档](https://maven.apache.org/guides/plugin/guide-java-plugin-development.html#Parameter)。

## 单元测试

Unit test和普通Maven项目没有太大区别，仅仅在于预设环境的不同，简化代码如下

```java
public class ReadPropertiesMojoTest {

  private MavenProject projectStub;
  private ReadJsonMojo readJsonMojo;

  @Before
  public void setUp() {
     // 创建一个空的MavenProject对象
    projectStub = new MavenProject();
    // 创建刚才的Mojo实例
    readJsonMojo = new ReadJsonMojo();
    // 显示将MavenProject注入Mojo，set方法前面的代码省略了，请注意。
    readJsonMojo.setProject(projectStub);
  }

  @Test
  public void readJsonFile() throws Exception {
    File testFile = constructTestFile();
    Properties baseProperties = constructComparedProperties();

    readJsonMojo.setFiles(new File[]{testFile});
    readJsonMojo.execute();

    Properties projectProperties = projectStub.getProperties();

    assertNotNull(projectProperties);
    assertNotEquals(0, projectProperties.size());
    assertEquals(baseProperties, projectProperties);
  }

  private File constructTestFile() throws IOException {
    . . . . . .
    return file;
  }

  private Properties constructComparedProperties() {
    . . . . . .
    return properties;
  }

}
```

## 安装测试

单元测试后，可以安装到本地仓库进行测试

### 安装

```bash
mvn clean install
```

### 命令行测试

可以直接通过命令行执行刚才的插件

```bash
# 命令行执行格式
mvn groupId:artifactId:version:goal
# 本项目执行如下
mvn com.github.zou8944.json-loader-maven-plugin:1.0.0:read-project-json-to-properties
```

### 在其它项目中使用

在本机上的另一个项目中通过如下配置使用它

```xml
      <plugin>
        <groupId>com.github.zou8944</groupId>
        <artifactId>json-loader-maven-plugin</artifactId>
        <version>1.0.0</version>
        <executions>
          <execution>
            <!-- phase在@Mojo定义时默认为intialize，因此这里实际可以不写 -->
            <phase>initialize</phase>
            <goals>
              <!-- goal，对应@Mojo设置的name -->
              <goal>read-project-json-to-properties</goal>
            </goals>
            <configuration>
              <files>
                 <!-- 指定文件路径，Maven能够自行解析成文件 -->
                <file>hello.json</file>
              </files>
            </configuration>
          </execution>
        </executions>
      </plugin>
```

## 遇到的坑

开发过程相对顺利，其中一个依赖冲突导致卡了较长时间。

MavenProject类中引入`import org.apache.maven.artifact.DependencyResolutionRequiredException`类，但该类在默认的Maven-Artifact 3.6.2包中已经没有了，找了几个版本，发现只有2.2.1版本存在，因此参考[baeldung的教程](https://www.baeldung.com/maven-plugin)，自定义了依赖项，才使问题得以解决。即，将Maven-Artifact包修改为2.2.1版本

```xml
    <dependency>
      <groupId>org.apache.maven</groupId>
      <artifactId>maven-artifact</artifactId>
      <version>2.2.1</version>
    </dependency>
```

## 总结

通过该项目简单地了解了Maven插件的开发方法，虽然简单，却提供了很多种可能性。

此外，本文中的代码均为简化后的，源码在[github](https://github.com/zou8944/json-loader-maven-plugin)上，欢迎访问，只不过需要注意：源码的pom中包含了很多其它内容，比如远程发布相关配置、site相关配置，请自行忽略。

## 参考文档

1. [Apache Plugin Developer Centre](https://maven.apache.org/guides/plugin/guide-java-plugin-development.html)
2. [How to Create a Maven Plugin](https://www.baeldung.com/maven-plugin)

3. [MojoHaus Properties Maven Plugin](https://github.com/mojohaus/properties-maven-plugin)