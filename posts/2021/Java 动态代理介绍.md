---
created_at: 2021-11-03 15:38:51.083
updated_at: 2021-11-03 15:38:51.083
slug: dynamic-proxy-introduction
tags: 
- Java
- 反射
- 动态代理
---

动态代理说大不大，说小不小，可深可浅。往深了说还是对JVM的了解程度要足够深入，时间篇幅有限，本文专注于回答如下问题，不作更深入的探讨。

- JDK和Cglib动态代理，分别怎么使用
- JDK动态代理的原理
- Cglib动态代理的原理
- 为什么JDK动态代理一定要实现接口，而Cglib就不用？
- JDK和Cglib，本质上有什么区别？

<!-- more -->

## JDK动态代理

### 使用

一个简单的场景

- 一个Service接口，拥有sayHello()方法
- 一个ServiceImpl实现类，实现Service
- 创建一个ServiceImpl的代理类，代理sayHello()方法，在调用原方法的前后，打印锚点

例子如下

```kotlin
interface Service {

    fun sayHello()

}

class ActualService : Service {

    override fun sayHello() {
        println("Hello, Java dynamic proxy...")
    }

}

class MyHandler(private val service: Service) : InvocationHandler {

    /**
     * proxy: 生成的代理类
     * method: 方法
     * args: 方法参数
     */
    override fun invoke(proxy: Any, method: Method, args: Array<out Any>?): Any? {
        return if (method.name == "sayHello") {
            println("调用方法前")
            method.invoke(service).also {
                println("调用方法后")
            }
        } else null
    }

}

fun main() {
  	// 将生成的代理类进行打印
    System.setProperty("jdk.proxy.ProxyGenerator.saveGeneratedFiles", "true")
    val proxy = Proxy.newProxyInstance(
        Service::class.java.classLoader,
        arrayOf(Service::class.java),
        MyHandler(ActualService())
    )
    (proxy as Service).sayHello()
}
```

总结一下，要点

- 被代理的类要实现接口
- 代理的逻辑要通过InvocationHandler实现
- `Proxy.newProxyInstance()`生成代理类，需要提供类加载器、被代理的接口、InvocationHandler

### 原理

源码自己跟，最终会来到核心方法

- `java.lang.reflect.Proxy.ProxyBuilder#defineProxyClass`

  关键逻辑：生成类的字节码流；使用sun.misc.Unsafe直接从流创建Class对象。

  ```java
  private static Class<?> defineProxyClass(Module m, List<Class<?>> interfaces) {
  	
  	...
  	byte[] proxyClassFile = ProxyGenerator.generateProxyClass(proxyName, interfaces.toArray(EMPTY_CLASS_ARRAY), accessFlags);
    try {
      Class<?> pc = UNSAFE.defineClass(proxyName, proxyClassFile, 0, proxyClassFile.length, loader, null);
      return pc;
    } catch (ClassFormatError e) {
      ...
    }
  	...
  
  }
  ```

- `java.lang.reflect.ProxyGenerator#generateProxyClass(java.lang.String, java.lang.Class<?>[], int)`，这里可以看到

  这里是类字节码流生成的关键逻辑：凭空构建一个class流

  - 常规class字节码文件的组成：魔数、版本号、常量池等
  - 写入父类：固定为`"java/lang/reflect/Proxy"`
  - 写入需要被代理的接口，用户传入的
  - 写入字段和方法，这其中包含了我们传入的InvocationHandler

  ```java
  ByteArrayOutputStream bout = new ByteArrayOutputStream();
  DataOutputStream dout = new DataOutputStream(bout);
  
  dout.writeInt(0xCAFEBABE);
  // u2 minor_version;
  dout.writeShort(CLASSFILE_MINOR_VERSION);
  // u2 major_version;
  dout.writeShort(CLASSFILE_MAJOR_VERSION);
  
  cp.write(dout);             // (write constant pool)
  
  // u2 access_flags;
  dout.writeShort(accessFlags);
  // u2 this_class;
  dout.writeShort(cp.getClass(dotToSlash(className)));
  // u2 super_class;
  dout.writeShort(cp.getClass(superclassName));
  
  // u2 interfaces_count;
  dout.writeShort(interfaces.length);
  // u2 interfaces[interfaces_count];
  for (Class<?> intf : interfaces) {
    dout.writeShort(cp.getClass(
      dotToSlash(intf.getName())));
  }
  
  // u2 fields_count;
  dout.writeShort(fields.size());
  // field_info fields[fields_count];
  for (FieldInfo f : fields) {
    f.write(dout);
  }
  
  // u2 methods_count;
  dout.writeShort(methods.size());
  // method_info methods[methods_count];
  for (MethodInfo m : methods) {
    m.write(dout);
  }
  
  // u2 attributes_count;
  dout.writeShort(0); // (no ClassFile attributes for proxy classes)
  
  ```

通过设置系统属性：`System.setProperty("jdk.proxy.ProxyGenerator.saveGeneratedFiles", "true")`可以将生成的字节码保存为文件，然后反编译看结果

```java
package com.sun.proxy;

import com.gitee.floyd.proxy.Service;
import java.lang.reflect.InvocationHandler;
import java.lang.reflect.Method;
import java.lang.reflect.Proxy;
import java.lang.reflect.UndeclaredThrowableException;

public final class $Proxy0 extends Proxy implements Service {
    private static Method m1;
    private static Method m3;
    private static Method m2;
    private static Method m0;

    public $Proxy0(InvocationHandler var1) throws  {
        super(var1);
    }

    public final boolean equals(Object var1) throws  {
        try {
            return (Boolean)super.h.invoke(this, m1, new Object[]{var1});
        } catch (RuntimeException | Error var3) {
            throw var3;
        } catch (Throwable var4) {
            throw new UndeclaredThrowableException(var4);
        }
    }

    public final void sayHello() throws  {
        try {
            super.h.invoke(this, m3, (Object[])null);
        } catch (RuntimeException | Error var2) {
            throw var2;
        } catch (Throwable var3) {
            throw new UndeclaredThrowableException(var3);
        }
    }

    public final String toString() throws  {
        try {
            return (String)super.h.invoke(this, m2, (Object[])null);
        } catch (RuntimeException | Error var2) {
            throw var2;
        } catch (Throwable var3) {
            throw new UndeclaredThrowableException(var3);
        }
    }

    public final int hashCode() throws  {
        try {
            return (Integer)super.h.invoke(this, m0, (Object[])null);
        } catch (RuntimeException | Error var2) {
            throw var2;
        } catch (Throwable var3) {
            throw new UndeclaredThrowableException(var3);
        }
    }

    static {
        try {
            m1 = Class.forName("java.lang.Object").getMethod("equals", Class.forName("java.lang.Object"));
            m3 = Class.forName("com.gitee.floyd.proxy.Service").getMethod("sayHello");
            m2 = Class.forName("java.lang.Object").getMethod("toString");
            m0 = Class.forName("java.lang.Object").getMethod("hashCode");
        } catch (NoSuchMethodException var2) {
            throw new NoSuchMethodError(var2.getMessage());
        } catch (ClassNotFoundException var3) {
            throw new NoClassDefFoundError(var3.getMessage());
        }
    }
}

```

几个要点

- 该代理类直接继承了Proxy类，实现类我们指定的Service接口
- `sayHello()`代理的原理：调用`InvocationHandler.invoke()`完成实际调用
- 代理类的所有方法，都会调用`InvocationHandler.invoke()`

### 小结

JDK的动态代理，是从头构建新的类字节码流，然后加载到JVM中达成的。其使用方法必须依赖接口、InvocationHandler、Proxy，并不是非常方便。

## CGlib

### 使用

类似上面，一个简单的场景

- 一个Service类，不用实现任何接口
- 创建Service的代理类，代理sayHello()方法，在调用原方法的前后，打印锚点

```kotlin
open class PersonService {

    open fun sayHello(name: String): String {
        return "Hello, $name"
    }

}

fun tryMethodInterceptor() {
    val enhancer = Enhancer()
    enhancer.setSuperclass(PersonService::class.java)
    enhancer.setCallback(MethodInterceptor { obj, method, args, proxy ->
        if (method.name == "sayHello") {
            println("我先执行一下")
            proxy.invokeSuper(obj, args).also {
                println("然后我再执行一下")
            }
        } else null
    })
    val proxy = enhancer.create() as PersonService
    println(proxy.sayHello("你好"))
}

fun main() {
    // 打印出生成的代理类
    System.setProperty(DebuggingClassWriter.DEBUG_LOCATION_PROPERTY, "/Users/zouguodong/Code/Personal/play-floyd/proxy/generatedClass")
    tryMethodInterceptor()
}
```

总结一下，要点

- 只需要被代理类自己，但被代理类和方法必须是open的，即可被继承和覆盖的
- 使用Enhancer类，方法拦截使用MethodInterceptor定义代理逻辑

### 原理

同样，跟跟源码，发现关键逻辑在：`net.sf.cglib.proxy.Enhancer#generateClass`，这里是通过ASM库来生成类字节码的，过程比较复杂，需要对ASM API比较了解才能分析，这里这里暂时忽略。直接看生成的代码。

设置系统属性`System.setProperty(DebuggingClassWriter.DEBUG_LOCATION_PROPERTY, "xxx")`可以将生成的代理类输出。

```java
public class PersonService$$EnhancerByCGLIB$$470f9603 extends PersonService implements Factory {
    private boolean CGLIB$BOUND;
    public static Object CGLIB$FACTORY_DATA;
    private static final ThreadLocal CGLIB$THREAD_CALLBACKS;
    private static final Callback[] CGLIB$STATIC_CALLBACKS;
    private MethodInterceptor CGLIB$CALLBACK_0;
    private static Object CGLIB$CALLBACK_FILTER;
    private static final Method CGLIB$sayHello$0$Method;
    private static final MethodProxy CGLIB$sayHello$0$Proxy;
    private static final Object[] CGLIB$emptyArgs;
    private static final Method CGLIB$length$1$Method;
    private static final MethodProxy CGLIB$length$1$Proxy;
    private static final Method CGLIB$equals$2$Method;
    private static final MethodProxy CGLIB$equals$2$Proxy;
    private static final Method CGLIB$toString$3$Method;
    private static final MethodProxy CGLIB$toString$3$Proxy;
    private static final Method CGLIB$hashCode$4$Method;
    private static final MethodProxy CGLIB$hashCode$4$Proxy;
    private static final Method CGLIB$clone$5$Method;
    private static final MethodProxy CGLIB$clone$5$Proxy;

    static void CGLIB$STATICHOOK1() {
        CGLIB$THREAD_CALLBACKS = new ThreadLocal();
        CGLIB$emptyArgs = new Object[0];
        Class var0 = Class.forName("com.gitee.floyd.proxy.PersonService$$EnhancerByCGLIB$$470f9603");
        Class var1;
        Method[] var10000 = ReflectUtils.findMethods(new String[]{"equals", "(Ljava/lang/Object;)Z", "toString", "()Ljava/lang/String;", "hashCode", "()I", "clone", "()Ljava/lang/Object;"}, (var1 = Class.forName("java.lang.Object")).getDeclaredMethods());
        CGLIB$equals$2$Method = var10000[0];
        CGLIB$equals$2$Proxy = MethodProxy.create(var1, var0, "(Ljava/lang/Object;)Z", "equals", "CGLIB$equals$2");
        CGLIB$toString$3$Method = var10000[1];
        CGLIB$toString$3$Proxy = MethodProxy.create(var1, var0, "()Ljava/lang/String;", "toString", "CGLIB$toString$3");
        CGLIB$hashCode$4$Method = var10000[2];
        CGLIB$hashCode$4$Proxy = MethodProxy.create(var1, var0, "()I", "hashCode", "CGLIB$hashCode$4");
        CGLIB$clone$5$Method = var10000[3];
        CGLIB$clone$5$Proxy = MethodProxy.create(var1, var0, "()Ljava/lang/Object;", "clone", "CGLIB$clone$5");
        var10000 = ReflectUtils.findMethods(new String[]{"sayHello", "(Ljava/lang/String;)Ljava/lang/String;", "length", "(Ljava/lang/String;)I"}, (var1 = Class.forName("com.gitee.floyd.proxy.PersonService")).getDeclaredMethods());
        CGLIB$sayHello$0$Method = var10000[0];
        CGLIB$sayHello$0$Proxy = MethodProxy.create(var1, var0, "(Ljava/lang/String;)Ljava/lang/String;", "sayHello", "CGLIB$sayHello$0");
        CGLIB$length$1$Method = var10000[1];
        CGLIB$length$1$Proxy = MethodProxy.create(var1, var0, "(Ljava/lang/String;)I", "length", "CGLIB$length$1");
    }

    final String CGLIB$sayHello$0(String var1) {
        return super.sayHello(var1);
    }

    public final String sayHello(String var1) {
        MethodInterceptor var10000 = this.CGLIB$CALLBACK_0;
        if (var10000 == null) {
            CGLIB$BIND_CALLBACKS(this);
            var10000 = this.CGLIB$CALLBACK_0;
        }

        return var10000 != null ? (String)var10000.intercept(this, CGLIB$sayHello$0$Method, new Object[]{var1}, CGLIB$sayHello$0$Proxy) : super.sayHello(var1);
    }

    final int CGLIB$length$1(String var1) {
        return super.length(var1);
    }

    public final int length(String var1) {
        MethodInterceptor var10000 = this.CGLIB$CALLBACK_0;
        if (var10000 == null) {
            CGLIB$BIND_CALLBACKS(this);
            var10000 = this.CGLIB$CALLBACK_0;
        }

        if (var10000 != null) {
            Object var2 = var10000.intercept(this, CGLIB$length$1$Method, new Object[]{var1}, CGLIB$length$1$Proxy);
            return var2 == null ? 0 : ((Number)var2).intValue();
        } else {
            return super.length(var1);
        }
    }

    final boolean CGLIB$equals$2(Object var1) {
        return super.equals(var1);
    }

    public final boolean equals(Object var1) {
        MethodInterceptor var10000 = this.CGLIB$CALLBACK_0;
        if (var10000 == null) {
            CGLIB$BIND_CALLBACKS(this);
            var10000 = this.CGLIB$CALLBACK_0;
        }

        if (var10000 != null) {
            Object var2 = var10000.intercept(this, CGLIB$equals$2$Method, new Object[]{var1}, CGLIB$equals$2$Proxy);
            return var2 == null ? false : (Boolean)var2;
        } else {
            return super.equals(var1);
        }
    }

    final String CGLIB$toString$3() {
        return super.toString();
    }

    public final String toString() {
        MethodInterceptor var10000 = this.CGLIB$CALLBACK_0;
        if (var10000 == null) {
            CGLIB$BIND_CALLBACKS(this);
            var10000 = this.CGLIB$CALLBACK_0;
        }

        return var10000 != null ? (String)var10000.intercept(this, CGLIB$toString$3$Method, CGLIB$emptyArgs, CGLIB$toString$3$Proxy) : super.toString();
    }

    final int CGLIB$hashCode$4() {
        return super.hashCode();
    }

    public final int hashCode() {
        MethodInterceptor var10000 = this.CGLIB$CALLBACK_0;
        if (var10000 == null) {
            CGLIB$BIND_CALLBACKS(this);
            var10000 = this.CGLIB$CALLBACK_0;
        }

        if (var10000 != null) {
            Object var1 = var10000.intercept(this, CGLIB$hashCode$4$Method, CGLIB$emptyArgs, CGLIB$hashCode$4$Proxy);
            return var1 == null ? 0 : ((Number)var1).intValue();
        } else {
            return super.hashCode();
        }
    }

    final Object CGLIB$clone$5() throws CloneNotSupportedException {
        return super.clone();
    }

    protected final Object clone() throws CloneNotSupportedException {
        MethodInterceptor var10000 = this.CGLIB$CALLBACK_0;
        if (var10000 == null) {
            CGLIB$BIND_CALLBACKS(this);
            var10000 = this.CGLIB$CALLBACK_0;
        }

        return var10000 != null ? var10000.intercept(this, CGLIB$clone$5$Method, CGLIB$emptyArgs, CGLIB$clone$5$Proxy) : super.clone();
    }

    public static MethodProxy CGLIB$findMethodProxy(Signature var0) {
        String var10000 = var0.toString();
        switch(var10000.hashCode()) {
        case -1816210712:
            if (var10000.equals("sayHello(Ljava/lang/String;)Ljava/lang/String;")) {
                return CGLIB$sayHello$0$Proxy;
            }
            break;
        case -508378822:
            if (var10000.equals("clone()Ljava/lang/Object;")) {
                return CGLIB$clone$5$Proxy;
            }
            break;
        case 166945484:
            if (var10000.equals("length(Ljava/lang/String;)I")) {
                return CGLIB$length$1$Proxy;
            }
            break;
        case 1826985398:
            if (var10000.equals("equals(Ljava/lang/Object;)Z")) {
                return CGLIB$equals$2$Proxy;
            }
            break;
        case 1913648695:
            if (var10000.equals("toString()Ljava/lang/String;")) {
                return CGLIB$toString$3$Proxy;
            }
            break;
        case 1984935277:
            if (var10000.equals("hashCode()I")) {
                return CGLIB$hashCode$4$Proxy;
            }
        }

        return null;
    }

    public PersonService$$EnhancerByCGLIB$$470f9603() {
        CGLIB$BIND_CALLBACKS(this);
    }

    public static void CGLIB$SET_THREAD_CALLBACKS(Callback[] var0) {
        CGLIB$THREAD_CALLBACKS.set(var0);
    }

    public static void CGLIB$SET_STATIC_CALLBACKS(Callback[] var0) {
        CGLIB$STATIC_CALLBACKS = var0;
    }

    private static final void CGLIB$BIND_CALLBACKS(Object var0) {
        PersonService$$EnhancerByCGLIB$$470f9603 var1 = (PersonService$$EnhancerByCGLIB$$470f9603)var0;
        if (!var1.CGLIB$BOUND) {
            var1.CGLIB$BOUND = true;
            Object var10000 = CGLIB$THREAD_CALLBACKS.get();
            if (var10000 == null) {
                var10000 = CGLIB$STATIC_CALLBACKS;
                if (var10000 == null) {
                    return;
                }
            }

            var1.CGLIB$CALLBACK_0 = (MethodInterceptor)((Callback[])var10000)[0];
        }

    }

    public Object newInstance(Callback[] var1) {
        CGLIB$SET_THREAD_CALLBACKS(var1);
        PersonService$$EnhancerByCGLIB$$470f9603 var10000 = new PersonService$$EnhancerByCGLIB$$470f9603();
        CGLIB$SET_THREAD_CALLBACKS((Callback[])null);
        return var10000;
    }

    public Object newInstance(Callback var1) {
        CGLIB$SET_THREAD_CALLBACKS(new Callback[]{var1});
        PersonService$$EnhancerByCGLIB$$470f9603 var10000 = new PersonService$$EnhancerByCGLIB$$470f9603();
        CGLIB$SET_THREAD_CALLBACKS((Callback[])null);
        return var10000;
    }

    public Object newInstance(Class[] var1, Object[] var2, Callback[] var3) {
        CGLIB$SET_THREAD_CALLBACKS(var3);
        PersonService$$EnhancerByCGLIB$$470f9603 var10000 = new PersonService$$EnhancerByCGLIB$$470f9603;
        switch(var1.length) {
        case 0:
            var10000.<init>();
            CGLIB$SET_THREAD_CALLBACKS((Callback[])null);
            return var10000;
        default:
            throw new IllegalArgumentException("Constructor not found");
        }
    }

    public Callback getCallback(int var1) {
        CGLIB$BIND_CALLBACKS(this);
        MethodInterceptor var10000;
        switch(var1) {
        case 0:
            var10000 = this.CGLIB$CALLBACK_0;
            break;
        default:
            var10000 = null;
        }

        return var10000;
    }

    public void setCallback(int var1, Callback var2) {
        switch(var1) {
        case 0:
            this.CGLIB$CALLBACK_0 = (MethodInterceptor)var2;
        default:
        }
    }

    public Callback[] getCallbacks() {
        CGLIB$BIND_CALLBACKS(this);
        return new Callback[]{this.CGLIB$CALLBACK_0};
    }

    public void setCallbacks(Callback[] var1) {
        this.CGLIB$CALLBACK_0 = (MethodInterceptor)var1[0];
    }

    static {
        CGLIB$STATICHOOK1();
    }
}
```

看到

- 生成的代理类直接继承了`Service`类
- 方法拦截都是通过`MethodInterceptor`
- 构建`MethodProxy`传入，用于真实方法的调用。

注意：`MethodInterceptor`中如果直接调用Method，会造成堆栈溢出。必须通过`MethodProxy.invokeSuper()`方法调用才行。

### 小结

CGlib是基于ASM进行字节码生成的，在使用上会简单很多。

## 区别

可以看到，无论是JDK动态代理，还是CGlib，最终都是生成了代理类的字节码，并将其加载为新的类。从这个角度上看，貌似没啥区别呀？理论上，JDK的动态代理也可以设计成CGlib那样，直接基于类生成代理子类，就像[有人做的那样](https://blog.csdn.net/qq_34173920/article/details/105504407)。很多人说，JDK动态代理只能基于接口，是因为代理类继承了Proxy，而Java是单继承，没有办法再继承用户自定义类，我认为这个说法因果倒置了，都说了，如果想要继承自定义类，是能够办到的。对于这个问题，我的看法是JDK设计者故意为之，至于原因嘛，我也不大说得上来（说到底，还是菜）。

JDK代理和CGlib代理的区别，除了API使用上，更重要的是字节码生成方式上的区别：前者凭空生成；后者使用ASM基于被代理类生成。

都是生成，区别在于生成的效率以及生成的代理类的效率。这又涉及到谁效率高的问题了。用JMH大概试一试吧。我们用几乎一样的被代理类，生成代理类，调用方法。测试每个操作所耗费的时间。

```kotlin
///////////////////////CGlib的测试case
open class PersonService {
    open fun sayHello() {}
}

fun tryMethodInterceptor() {
    val enhancer = Enhancer()
    enhancer.setSuperclass(PersonService::class.java)
    enhancer.setCallback(MethodInterceptor { obj, method, args, proxy ->
        if (method.name == "sayHello") {
            proxy.invokeSuper(obj, args)
        } else null
    })
    (enhancer.create() as PersonService).sayHello()
}

///////////////////////JDK的测试CASE
interface Service {
    fun sayHello()
}

class ActualService : Service {
    override fun sayHello() { }
}

class MyHandler(private val service: Service) : InvocationHandler {
    override fun invoke(proxy: Any, method: Method, args: Array<out Any>?): Any? {
        return if (method.name == "sayHello") {
            method.invoke(service)
        } else null
    }
}

fun testJDKProxy() {
    val proxy = Proxy.newProxyInstance(
        Service::class.java.classLoader,
        arrayOf(Service::class.java),
        MyHandler(ActualService())
    )
    (proxy as Service).sayHello()
}

///////////////////////测试代码：测试各执行100次，平均每次耗时多少
@Fork(1)
@Threads(10)
@Warmup(iterations = 1)
@State(Scope.Benchmark)
@BenchmarkMode(Mode.AverageTime)
@OutputTimeUnit(TimeUnit.MILLISECONDS)
open class JMHWarm {

    @Param("100")
    var count: Int = 0

    @Benchmark
    fun testJDK() {
        for (i in 1..count) {
            testJDKProxy()
        }
    }

    @Benchmark
    fun testCGlib() {
        for (i in 1..count) {
            tryMethodInterceptor()
        }
    }

}

fun main() {
    val option = OptionsBuilder()
        .include(JMHWarm::class.simpleName)
        .resultFormat(ResultFormatType.JSON)
        .build()
    Runner(option).run()
}
```

对于上面的case，当只保留代理类创建逻辑时，测试结果

```bash
Benchmark          (count)  Mode  Cnt  Score    Error  Units
JMHWarm.testCGlib      100  avgt    5  0.001 ±  0.001  ms/op
JMHWarm.testJDK        100  avgt    5  0.004 ±  0.002  ms/op
```

当同时保留创建和方法调用逻辑时，测试结果

```bash
Benchmark          (count)  Mode  Cnt  Score   Error  Units
JMHWarm.testCGlib      100  avgt    5  0.028 ± 0.002  ms/op
JMHWarm.testJDK        100  avgt    5  0.006 ± 0.001  ms/op
```

当前这样的基准测试是不准确的，但还是大致可以得出代理类的创建CGlib比JDK快，但调用上JDK更快。快多少？快不了多少。

## 总结

按照本文的方式来探索动态代理，还是远远不够的，要想把这一块理解透彻，说到底，还是要对JVM有深入的研究，也就是说，还需要继续探索的点

- ASM库的使用、深入理解

- 类加载的深入研究，ClassLoader类的剖析

- sun.misc.Unsafe类的深入研究

- JVM的深入研究