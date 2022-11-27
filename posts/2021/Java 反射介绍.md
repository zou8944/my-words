---
created_at: 2021-10-21 18:09:05.37
updated_at: 2021-10-21 18:09:05.37
slug: java-reflection-introduction
tags: 
- Java
- 反射
---


我会写Java反射，我知道反射是用来获取、改变程序运行时状态的方式，通过反射API我们能够获取类对象、类的方法、成员变量、注解等。

我不会写Java反射，我不知道Type和Class有啥关系，ParameteredType、TypeVariable呢？

我会Java反射吗？不，我不会。

<!-- more -->

## 反射是什么？

反射是什么，镜子里看自己。往小了说，就是Java提供的一组能够在运行时查看和修改对象信息的API；往大了说，从计算机专业来看，是编程语言提供的运行时动态更新自身状态的能力，Java的反射只是其中的一种。Go、C#、JS等都实现了自己的反射机制。

吐槽”反射“这个翻译，英文”Reflection“、”Reflective“。说这个翻译名不好吧，它是直译，且一定程度能够反应其含义：程序能够看到本身；但说他准确也并不能让人信服，翻译成内省个人认为会更好一点，但无奈Java中内省是另外一套API。

照我的意思，就别翻译了，就Reflection和Instropection就好，英文原意，哪怕你不能完全理解，总比被翻译曲解来得好。

## 理解其组成

就API能力来说，反射无非是让我们获取类对象的各个组成部分，并提供对类对应的实例相应部分的修改。因此，首先要理解类的各个组成部分和反射API接口之间的对应关系，用一张思维导图说明。

![](https://gdz.oss-cn-shenzhen.aliyuncs.com/local/image-20211021122902091.png)

可以看到，Java中的每种元素，都有对应的反射抽象对应

- 所有类型，包括类、接口、抽象类、注解、枚举等，由Class类进行抽象。在一个完全面向对象的语言中，运行时查看和修改的也肯定是对象的信息，因此它也是反射的入口。
- 对类中的成员，有构造方法、普通方法、字段，分别由Constructor、Mehtod、Field抽象
- 对特殊的数组类型，有Array抽象
- 对泛型，根据情况有TypeVariable、GenericArrayType、ParameterizedType、WildcardType分别进行抽象

所有这些抽象的目的，都是为了能够让我们通过某条路径获取到确定的那个元素，如字段声明`List<String> str`，为了获取到List中的泛型String，需要通过如下路径调用

1. 获取字段所属类的Class对象clazz
2. `clazz.getDeclaredFiled("str")`获取到该Field
3. `field.getGenericType()`获取泛型类型ft，并强转为ParameterizedType
4. `ft.getActualTypeArguments()[0]`获取该泛型的具体参数String

Java反射用的好不好，就看反射的API用的熟不熟。

## 几个抽象树

针对不同元素的特性，反射API从不同维度进行了抽象，下面依次看一下。

### Type

Java 1.5之前，反射只有Class对象，并没有各种Type，但1.5之后引入了泛型，考虑到兼容性，Class对象并没有修改，而是将新的泛型表示抽象了出来。Class自然也是Type的子类，但由于其方法过多，我们没有画出来

![image-20211021125002864](https://gdz.oss-cn-shenzhen.aliyuncs.com/local/image-20211021125002864.png)

Type的上述几个类型，都是泛型的各种形态。

### AnnotatedElement

表示可被注解的元素，可以看到，包括了包、Module、参数、类对象、可访问对象（方法、构造方法、字段）、各种泛型类型

一个可被注解的元素，能够获取到自己上面的所有注解。

![image-20211021125118611](https://gdz.oss-cn-shenzhen.aliyuncs.com/local/image-20211021125118611.png)

### GenericDeclaration

可声明泛型变量的元素，有类、构造方法、方法。泛型变量指的是T这样的东西。

一个可生命泛型变量的元素，能够获取到该元素的所有类型变量，即TypeVariable数组。

![image-20211021140853046](https://gdz.oss-cn-shenzhen.aliyuncs.com/local/image-20211021140853046.png)

### AccessibleObject

可访问对象，有方法、构造函数、字段。访问他们需要权限。`xxx.setAccessible(true)`我们一定很熟悉。

一个可访问对象，实现了Java的访问控制策略，能够限制用户对自己的访问。

![截屏2021-10-21 下午2.12.58](https://gdz.oss-cn-shenzhen.aliyuncs.com/local/%E6%88%AA%E5%B1%8F2021-10-21%20%E4%B8%8B%E5%8D%882.12.58.png)

### Member

成员，可作为成员的对象。有方法、构造函数、字段。

一个成员，能够获取该成员的名称、获取修饰符、获取声明该成员的类对象。

![截屏2021-10-21 下午2.15.52](https://gdz.oss-cn-shenzhen.aliyuncs.com/local/%E6%88%AA%E5%B1%8F2021-10-21%20%E4%B8%8B%E5%8D%882.15.52.png)

## 一个例子

不展示常用的获取类成员的例子，我们展示一个泛型的例子：在Json反序列化过程中，由于类型擦除，我们无法判定具体值的类型，一般的库如Jackson、Fastjson提供了TypeReference\<XXX>帮助我们决定反序列化的类型，Gson中的TypeToken\<XXX>也是同样的作用。我们来模仿一下这个过程。

**题目**：给出一个字符串，将其转换成指定的泛型类型

```java
/**
 * 实现Comparable，并不是为了比较，而是为了得到泛型T的实际类型
 */
abstract class TypeReference<T> {

    private final Type type;

    protected TypeReference() {
        Type superClass = getClass().getGenericSuperclass();
        this.type = ((ParameterizedType) superClass).getActualTypeArguments()[0];
    }

    public Type getType() {
        return type;
    }
}

class ReflectUtils {

    /**
     * 根据给定的类型，将字符串转换为对应实例
     */
    public static <R> R convertReflective(String source, TypeReference<R> type) throws Exception {
        Type actualType = type.getType();
        if (actualType instanceof ParameterizedType) {
            return convertReflectiveForParameterizedType(source, actualType);
        } else if (actualType instanceof Class) {
            return convertReflectiveForClass(source, actualType);
        } else if (actualType instanceof GenericArrayType) {
            throw new Exception("尚未实现");
        } else {
            throw new Exception("啥类型都不是呀");
        }
    }

    /**
     * 带泛型的类型
     */
    private static <R> R convertReflectiveForParameterizedType(String source, Type type) {
        ParameterizedType rType = (ParameterizedType) type;
        Object result = null;
        Type rawType = rType.getRawType();
        Type[] actualTypes = rType.getActualTypeArguments();
        if (rawType.equals(List.class)) {
            Type actualType = actualTypes[0];
            result = Arrays.stream(source.substring(1, source.length() - 1).split(","))
                .map(String::trim)
                .map((String it) -> convertReflectiveForClass(it, actualType))
                .collect(Collectors.toList());
        } else {
            System.out.println("暂不支持");
        }
        return (R) result;
    }

    /**
     * 非泛型的普通类型
     */
    private static <R> R convertReflectiveForClass(String source, Type type) {
        Object result = 0;
        if (String.class.equals(type)) {
            result = source;
        } else if (Integer.class.equals(type)) {
            result = Integer.valueOf(source);
        } else if (Long.class.equals(type)) {
            result = Long.valueOf(source);
        } else {
            result = source;
        }
        return (R) result;
    }

}

public class Demo {

    public static void main(String[] args) throws Exception {
        // 字符串转字符串
        String s = ReflectUtils.convertReflective("这是普通字符串", new TypeReference<String>() {});
        System.out.println(s);
        // 字符串转列表
        List<String> list = ReflectUtils.convertReflective("[1,2,字符串]", new TypeReference<List<String>>() {});
        list.forEach(System.out::println);
    }

}
```

输出

```bash
这是普通字符串
1
2
字符串
```

简单讲解

- 定义`TypeReference<T>`泛型抽象类，使用时候构建的是它的匿名子类，如`new TypeReference<List<String>>() {}`

  为什么要构建子类呢？因为`TypeReference<T>`的泛型在反射系统中永远是T，这是其类定义决定的，运行时给定的类型，统统会被擦除，因此是无法只使用`TypeReference<T>`就获取到指定的类型的；通过构建匿名子类`new TypeReference<List<String>>() {}`，对应新的类对象，其泛型就是具体的类型了，此时通过`getClass().getGenericSuperclass()`就能获取到`TypeReference<List<String>>`这一`ParameterizedType`。

  这点很重要，是实现这个功能的关键之一。

- 取得的泛型中的类型，依然可能是带有泛型，因此我们要递归判断。上面简单写，针对几个基本类型和List做了处理

## 反射工具库

很多库提供反射工具，比如[hutool的ReflectUtil](https://www.hutool.cn/docs/#/core/%E5%B7%A5%E5%85%B7%E7%B1%BB/%E5%8F%8D%E5%B0%84%E5%B7%A5%E5%85%B7-ReflectUtil)，我们看一下它做了什么。。。。。。它们也没做什么，就是将常用的操作封装到一个静态方法，比如直接获取构造方法，比我们自己做，多了些检查。

```java
public static <T> Constructor<T> getConstructor(Class<T> clazz, Class<?>... parameterTypes) {
  if (null == clazz) {
    return null;
  }

  final Constructor<?>[] constructors = getConstructors(clazz);
  Class<?>[] pts;
  for (Constructor<?> constructor : constructors) {
    pts = constructor.getParameterTypes();
    if (ClassUtil.isAllAssignableFrom(pts, parameterTypes)) {
      // 构造可访问
      setAccessible(constructor);
      return (Constructor<T>) constructor;
    }
  }
  return null;
}
```

其它的呢，也都差不多。

## 反射的实现

类的描述信息，它就在class文件中，因此在Class对象中可以看到。运行时修改的内容这个，可以去研究一下Java虚拟机实现。

## 反射和内省

内省指的是Introspector，是Java提供的另一个类，对应Java Bean规范，用以运行时查看Java Bean的属性、方法、事件等状态。其实现，也是通过反射。可以理解为使用反射为Java Bean提供了快捷访问方法，此时重点就要落在Java Bean上。如果你操作的是一个Bean，请直接用Introspector，如果你操作的是一个普通的类，那就用反射。

此外，Java Bean规范，有空的时候，也可以研究一下。看看它，到底是不是自己认识的那个样子。

## 反射很慢吗？

反射很慢吗？哪方面慢？慢多少？

我们用JMH测试针对自定义对象的某个空方法的调用，对比反射调用100万次、1亿次，和直接调用的差别。

```java
class MyClass {

    public void testMethod() {
    }

}

@BenchmarkMode(Mode.SingleShotTime)
@Warmup(iterations = 1, time = 10)
@Measurement(iterations = 1, time = 1)
@State(Scope.Thread)
@OutputTimeUnit(TimeUnit.MILLISECONDS)
public class ReflectionBenchmark {

    @Param({"1000000", "100000000"})
    int times;

    @Benchmark
    @Fork(1)
    public void invokeReflective() throws Exception {
        MyClass myClass = new MyClass();
        Method method = MyClass.class.getDeclaredMethod("testMethod");
        for (int i = 0; i < times; i++) {
            method.invoke(myClass);
        }
    }

    @Benchmark
    @Fork(1)
    public void invokeDirect() {
        MyClass myClass = new MyClass();
        for (int i = 0; i < times; i++) {
            myClass.testMethod();
        }
    }

    public static void main(String[] args) throws RunnerException {
        Options options = new OptionsBuilder()
            .include(ReflectionBenchmark.class.getSimpleName())
            .build();
        new Runner(options).run();
    }
}
```

测试结果如下，可见，反射确实会慢一些。上面的测试是调用空方法，次数非常多，会放大这种速度对比。但这个测试只能说明反射比直接调用慢。慢的程度，呈倍数关系比较合理。

![截屏2021-10-21 下午5.17.34](https://gdz.oss-cn-shenzhen.aliyuncs.com/local/%E6%88%AA%E5%B1%8F2021-10-21%20%E4%B8%8B%E5%8D%885.17.34.png)

转换成图表如下，更加直观。![截屏2021-10-21 下午5.23.19](https://gdz.oss-cn-shenzhen.aliyuncs.com/local/%E6%88%AA%E5%B1%8F2021-10-21%20%E4%B8%8B%E5%8D%885.23.19.png)

相关知乎问答：[Java反射到底慢在哪里](https://www.zhihu.com/question/19826278)

一篇分析反射方法调用的文章（传说中的R大）：[关于反射调用方法的一个log](https://www.iteye.com/blog/rednaxelafx-548536)

一篇针对反射的性能测试（我持保留看法）：[Java的反射调用性能很低吗?](https://zhuanlan.zhihu.com/p/55075493)

总体来说，反射确实会慢一些，对空方法来说，可能会慢个几倍吧，但对正常方法来说，还好。慢的原因，一是多了中间步骤，比如MethodAccessor的创建、参数的包装、一些条件判断等；二就是较为底层的实现了。

要想完全了解反射调用的原理，还是得从底层出发，需要对虚拟机实现、JIT即时编译实现细节有所了解，这是暂时还没什么时间去做的事情，所以就此打住吧。

## 还可以去看的文章

- [Reflective programming](https://en.wikipedia.org/wiki/Reflective_programming)
- [What is reflection and why is it useful?](https://stackoverflow.com/questions/37628/what-is-reflection-and-why-is-it-useful)

- [为什么c/c++没有反射？](https://www.zhihu.com/question/361153307)