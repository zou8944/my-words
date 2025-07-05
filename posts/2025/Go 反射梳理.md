---
created_at: 2025-07-05 15:00:00
updated_at: 2025-07-05 15:00:00
title: Go 反射梳理
slug: see-see-go-reflect
categories:
  - Go
tags:
  - "Go"
  - "反射"
---

> 反射是指程序检查自身的能力（尤其是通过类型），它是元编程的一种形式。
## Go 的类型系统
反射基于类型系统，因此必须先了解 Go 的类型系统。任何情况下，一个 Go 变量都会包含静态类型和值两个部分。

```Go
// 静态类型是 string，值是 "hello, world"
a := "hello, world"
// 静态类型是 int32，值是 12
b := int32(12)
```
值得关注的是，当变量类型是接口时，值就变得稍微复杂一点：接口只是声明一堆方法集合，甚至是空方法集合（空接口 interface{}），因此值就必须存储 (值, 值的具体类型) 对，以便转换为不同的接口进行调用。比如
```Go
var a interface{}
// 静态类型是 interface{}，值是 ("hello world", string) 对
a = "hello world"
```
这个可以在 debug 时看得比较明显。
<img src="https://gdz.oss-cn-shenzhen.aliyuncs.com/local/20250630215702.png" alt="image.png|500" style="zoom:50%;" />

> 一个接口变量的值，一定是存储的 (值, 具体类型) 对，而不能是 (值, 接口类型) 对，这样没有意义，也做不到。

几点说明
- `var i interface{}` ，这里 `i` 的静态类型是 `interface{}`，值是 `(nil, nil)` 对，即值和动态类型都是 `nil`
- 当两个变量值做相等比较时，只有值和动态类型都相等，才判断相等，否则不等
## 反射三定律
### 反射一定是从接口获取到反射对象
从根本上讲，反射只是一种检查接口变量中存储的类型和值对的机制。反射一定是从接口变量中获取反射对象的。
```Go
a := 12
aValue := reflect.ValueOf(a)

b := &Point{}
bType := reflect.TypeOf(b)
```
**问**：上面获取 `a` 的反射对象值明明是从基本类型变量 `a` 获取的，和前面一定从接口变量获取发射对象的论述冲突？
**答**：如下是 `reflect.ValueOf()` 函数的定义，可以看到，当 `a` 传入时，实际就传给了静态类型为 `interface{}` 的变量 `i`，此时 `i` 的静态类型为 `interface{}`，值是` (12, int)`。所以 “一定从接口变量获取发射对象” 的论述依然正确。 

```Go
func ValueOf(i any) Value {
    ...
}
```
### 反射也能从反射对象获取回接口值
反射会生成自己的逆。也就是说，通过 `refelct.ValueOf(xxx)` 能够获取到 `xxx` 的反射对象，也能通过反射对象的 `xxxValue.interface{}` 获取到原本 `xxx` 所代表的值。
> 只不过这里丢失了静态类型，这是合理的，静态类型是变量专属，通过 `xxxValue.interface{}` 获取到的仅仅是一个值，值是不会有静态类型的。

**问**：通过 `xxxValue.interface{}` 获取到的值是原本那个值吗？
答：如果原本的值是值类型，比如 `int`、`string` 等类型，那么得到的肯定是一个副本；如果原本的值是一个引用类型，那么得到的就是指向原始数据的引用。

### 要修改反射对象，其值必须可设置
反射的目的就是为了观察和修改原变量的值，因此会持有原变量的值。如果持有的是原变量的副本，修改就没了意义，此时能看不能改；但如果持有指向原变量的指针，就既能看也能改。一个典型的无法修改的情况如下：
```go
var x float64 = 3.4
v := reflect.ValueOf(x)
v.SetFloat(7.1) // Error: will panic.
```
这是因为 x 是值类型，向 `reflect.ValueOf()` 传递的是自己的副本，反射对象无法触及到原变量，所以无法修改。要让它能够被修改，得传入其指针
```go
var x float64 = 3.4
v := reflect.ValueOf(&x) // 获取到指向 x 的指针的反射对象
for v.Kind() == reflect.Ptr {
    v = v.Elem() // 取得指针指向的值的反射对象
}
if v.CanSet() {
    v.SetFloat(7.1) // 设置指针指向的值
}
fmt.Println(v.Interface()) // 输出 7.1
```
## `reflect` 包巡礼
> 反射的第一要义是弄懂 `reflect.Type`, `reflect.Value`, `reflect.Kind` 三者的关系。

反射就是使用反射对象描述变量的运行时状态。根据反射第一定律，反射的起始一定是接口，而接口的值以 `(值，具体类型)` 对存在。Go 使用 `reflect.Value` 来描述此处的值，`reflect.Type` 来描述此处的具体类型。

还有一个很重要的概念是 `reflect.Kind`，它是一个枚举，描述具体类型的基本类型，下图对比 `reflect.Type` 和 `reflect.Kind` ：任何具体类型都是由基础类型定义而来。
![image.png](https://gdz.oss-cn-shenzhen.aliyuncs.com/local/20250701212201.png)

### `reflect.Kind`
```go
const (
	Invalid Kind = iota
	Bool
	Int
	Int8
	Int16
	Int32
	Int64
	Uint
	Uint8
	Uint16
	Uint32
	Uint64
	Uintptr
	Float32
	Float64
	Complex64
	Complex128
	Array
	Chan
	Func
	Interface
	Map
	Pointer
	Slice
	String
	Struct
	UnsafePointer
)
```

`Kind` 枚举了所有基础类型：

- 常规类型：`Bool`、`Intx`、`Uintx`、`Floatxx`、`Complexxx`、`String`

- 指针相关
    - `Uintptr` 对应于 `uintptr` 类型，它可以表示一个无符号的整型值，其大小足够容纳一个指针。主要用于与底层指针操作相关，常见场景是和指针地址值互相转换，平时用不到。
    
    - `UnsafePointer`：`对应于 unsafe.Pointer`，允许对内存进行不安全的操作（例如类型强转、规避类型检查等）。
    
    - `Pointer`：就是一个普通的指针。前面两种都不是常规指针类型，不常用，但这个常用。
    
      > 我们通常还会用 `reflect.Ptr`，它是 `reflect.Pointer` 的别名。
    
- 接口：`Interface`。`reflect.Interface` 并不能直接得到，但是可以在复合类型中定义元素是 `interface{}`，比如
    ```go
    
    // 定义一个元素为 interface{} 的切片，那么切片的反射对象的元素的 Kind 就是 reflect.Interface。类似的
    var slice []interface{}
	slice = append(slice, "Hello", 42, 3.14)
	fmt.Println("Slice Element Type Kind:", reflect.TypeOf(slice).Elem().Kind())
    
    // 结构体的字段类型为 interface{}，那么通过结构体的反射对象获取到的字段的 Kind 就是 reflect.Inerface
    type MyStruct struct {
		Field1 interface{}
	}
	ms := MyStruct{Field1: "World"}
	fmt.Println("MyStruct Field1 Type Kind:", reflect.TypeOf(&ms).Field(0).Type.Kind())
    ```
    
- 结构体：`Struct`

- 集合类型：`Slice` `Array` `Map`

- 通道：`Chan`

- 函数：`Func`

  每种类型在反射对象上都有对象的操作方法，后面一一说明。

> **如何理解上面结构体 `MyStruct` 字段 `Field1` 的反射对象的 Kind 不是具体类型，而是 `reflect.Interface`？**
>
> 答：构建反射对象时，加载的是目标变量具体类型的静态声明信息，而不是动态信息。这是有道理的：
>
> - 一来，任何时候通过 `reflect.TypeOf(ms).Field(0).Type` 访问得到的都是声明的接口类型，具有一致性。
> - 二来，返回静态声明类型直接访问编译后的类型信息就行了，比较高效

> **我想，真正的疑问是：`reflect.TypeOf(xxx)` 时获取的是 xxx 的具体类型；而涉及到复合类型的元素时获取到的却是静态类型，行为似乎不一致。**
>
> 答：`reflect.TypeOf(xxx)` 时 `xxx` 的类型已确定，不会再变；但复合类型的元素只能按声明类型操作，因为其元素随时可能发生变化，如果按照 `string` 返回，但它其实还可以设置为 int 类型的值，这样明显不合理。
>
> 要获取到 `string`，可以通过 `reflect.Value`，比如 `reflect.ValueOf(&ms).Elem().Field(0).Elem().Kind()` ，其中 `Elem()` 函数表示获取接口包含的具体元素或接口指向的元素。
### `reflect.Type`
`reflect.Type` 是一个接口，
```go
type Type interface {
    // 类型的对齐值
    func Align() int
    // 类型作为其它结构体的字段时的对齐值。大多数情况和 Align() 一样，不一样的时候目前还不清楚
    func FieldAlign() int

    // 获取第 i 个方法，方法按字典顺序排
    Method(int) Method
    // 通过方法名获取方法
    MethodByName(string) (Method, bool)
    // 方法数量：非接口类型仅包括导出方法；接口类型既包括导出方法，也包括非导出方法
    NumMethod() int
  
  	// 类型名（包含包路径）
  	Name() string
  	// 包路径
	  PkgPath() string	
  	// 该类型的值需要占用的字节数。类似 unsafe.Sizeof
  	Size() uintptr
  
 		// 返回类型的字符串表示，不同的类型的 String() 可能一样，不保证唯一
  	String() string
  
  	// 当前类型是否实现了接口 u
  	Implements(u Type) bool
  	// 当前类型的值是否可赋值给类型 u 的变量
  	//（可以赋值的几种情况：当前类型实现了接口 u; 当前类型是一个接口，但 u 是兼容的更大的接口; 类型相同等）
  	AssignableTo(u Type) bool
  	// 当前类型是否可以转换为类型 u，即 T(x) 这种转换能否成功
  	ConvertibleTo(u Type) bool
  
  	// 当前类型的值是否可比较
  	Comparable() bool
  
  	// 仅对所有整型、无符号整型、浮点型、复数类型有效，返回该类型所占用的位宽，比如 8 16 32 64 之类的
  	Bits() int
  
  	// 仅当 chan 是时有效，返回通道方向
  	ChanDir() ChanDir
  
  	// 仅当 slice、array、chan、map、指针 时有效，返回它们包含的元素的类型
  	Elem() Type
  
  	// 如下几个方法仅当结构体时有效
  	// 返回第 i 个字段，字段顺序就是声明顺序
  	Field(i int) StructField
  	// 按照索引返回字段，支持嵌套，比如字段的类型也是结构体，则可以获取该结构体的字段
  	FieldByIndex(index []int) StructField
  	// 按字段名获取字段，也支持嵌套
  	FieldByName(name string) (StructField, bool)
  	// 还是按照名称找，只不过使用函数支持更加复杂的处理
  	FieldByNameFunc(match func(string) bool) (StructField, bool)
  	// 导出字段的数量。不包含嵌套
	  NumField() int
  
  	// 如下几个方法仅当函数时有效
  	// 获取第 i 个入参数的类型（如果有接收值，接收值就是第一个参数）
  	In(i int) Type
  	// 获取第 i 个返回值的类型
	  Out(i int) Type
  	// 入参数量（算接收值的）
  	NumIn() int
  	// 出参数量
  	NumOut() int
  	// 判断最后一个参数是否为可变参数。如果是，那么最后一个参数就是 []T 类型
  	IsVariadic() bool
  
  	// 仅当 map 时有效，返回 key 的类型
  	Key() Type
  
  	// 仅当 Array 时有效，返回数组的长度
  	Len() int
}
```

#### 对齐

**变量对齐的意义**

概念：每个变量都有一个对齐值，其作用是知道变量地址分配：分配的地址必须是对齐值的整数倍

为什么分配的地址必须是对齐值的整数倍

- 首先明白，CPU 从内存读取数据是按照 word 读取的，32 为系统的 word 是 4 字节，64 位是 8 字节

- **要求分配的地址必须是对齐值的整数倍，是为了确保变量的数据在尽量少的 word 内**，减少读取次数，提升效率

  举例：假设 word 是 4 字节，变量大小是 2 字节，不要求起始地址是 2 的整数倍时：如果被分配到了 1-2 字节，能够被一次性读出，没有问题；但如果被分配到 3-4 字节，就需要读取两次，浪费一次。

  要求起始地址是 2 的倍数时：它肯定被分配到每个 word 内部，一定能够被一次读出。

**类型对齐值的计算**

对齐值最大只有 8 字节，因为操作系统最大也就是 64 位，该场景下一个 word 就是 8 字节

- 基本类型的对齐值就是占用字节大小

- 指针类型和引用类型(如切片、channel 等) 对齐值就是一个 word

- 结构体的的对齐值是其字段对齐值的最大值

  有时候如果分不清楚，就使用 `unsafe.Alignof(查看)`。

**对齐优化**

通常是排列结构体的字段顺序，使得整个结构体占用更少 word

```go
type Struct1 struct {
	Field1 int8
	Field2 int64
	Field3 int8
}
type Struct2 struct {
	Field1 int8
	Field3 int8
	Field2 int64
}

func main() {
	st1 := Struct1{Field1: 1, Field2: 2, Field3: 3}
	st2 := Struct2{Field1: 1, Field3: 3, Field2: 2}
	println(unsafe.Sizeof(st1)) // 输出 24
	println(unsafe.Sizeof(st2)) // 输出 16
}
```

解释：我的操作系统是 64 位，`Struct1` 由于 `Field2` 的对齐值是 8，因此单独占用一个 word，于是 `Field1` 和 `Field3` 不得不自己占用一个 word，总共 3 个 word；`Struct2` 中，`Field1` 和 `Field3` 共同占用一个 word，`Field2` 占用一个 word，总共 2 个 word。

#### 方法注意事项

- 类型的方法按照字典顺序排
- 对于非接口类型，只能看到导出的方法；对于接口类型，导出方法和非导出方法都能看到。
- 定义在类型指针上的方法，通过类型的 `reflect.Type` 是获取不到的

#### 可比较

- 基础类型比较的是值
- 指针类型比较的是地址
- 接口类型比较的是 (值,具体类型) 对
- 数组类型如果所有元素可比较，就可比较
- 切片、`map`、函数 不可比较，它们只能和 `nil` 比较，如果硬比较会报编译错误
- 结构体如果所有字段都可比较，就可比较

除 `interface{}` 外，多数可比较与否都可以在编译阶段检测出来

如果是 `interface{}`，其动态类型可以是上面说的任何类型，所以无法直接判断可比较与否，如果强行将两个不可比较的动态类型做比较，会 panic，比如

```go
var slice1 any = []string{"1", "2"}
var slice2 any = []string{"1", "2"}
println(slice1 == slice2) // panic: runtime error: comparing uncomparable type []string
```

可以先判断两者是否可比较，再比较

```go
var slice1 any = []string{"1", "2"}
var slice2 any = []string{"1", "2"}
if reflect.TypeOf(slice1).Comparable() && reflect.TypeOf(slice2).Comparable() {
  println(slice1 == slice2)
}
```

补充：如果两个不同类型都可比较，如果直接比较它们会报编译错误，如下

```go
a := 12
b := 1.1
println(a == b) // compile error: invalid operation: a == b (mismatched types int and float64)
```

但如果它们都是动态类型，此时比较不会 panic，只不过结果是 false，因为 `interface{}` 比较的是 `(值,类型)` 对。

```go
var a any = 12
var b any = 1.1
println(a == b) // output: false
```

### `reflect.Value`

`reflect.Value`是一个结构体，只能通过 IDE 概览方法，但如果想要复制下来逐个分析就有困难，我们通过如下代码可以打印出所有方法

```go
rValue := reflect.ValueOf(12)
rValueType := reflect.TypeOf(rValue)
for i := 0; i < rValueType.NumMethod(); i++ {
  methodName := rValueType.Method(i).Name
  methodType := rValueType.Method(i).Type
  methodInParams := []string{}
  methodOutParams := []string{}
  for j := 1; j < methodType.NumIn(); j++ {
    methodInParams = append(methodInParams, methodType.In(j).Name())
  }
  for j := 0; j < methodType.NumOut(); j++ {
    methodOutParams = append(methodOutParams, methodType.Out(j).Name())
  }
  fmt.Printf("%s(%s) %s\n", methodName, strings.Join(methodInParams, ","), strings.Join(methodOutParams, ","))
}
```

逐个看

```go
// 获取 Type 对象
func Type() Type
// 返回 Kind，得到的效果和 Type.Kind() 一样
func Kind() Kind

func CanAddr() bool
// 返回指针值对象，该指针指向当前值（仅当当前值是 CanAddr 的才能返回，否则报 panic）
func Addr() Value
// 获取指针。仅对 指针、map、chan、slice、func、interface 有效
func Pointer() uintptr
// 也是返回指针，只不过类型是 unsafe.Pointer，也仅对 指针、map、chan、slice、func、interface 有效
func UnsafePointer() unsafe.Pointer
// 对所有可寻址的对象有效，返回存储数据的地址。当 指针、map、chan、slice、func、interface 时，得到的结果和 Pointer() 一样
func UnsafeAddr() uintptr
// 对 interface 或 pointer 有效
// interface 时返回其包含的元素反射值对象；指针时返回其执行的元素的反射值对象
func Elem() Value
// 判断是否 nil。仅对 指针、map、chan、slice、func、string、UnsafePointer 有效
func IsNil() bool
// 仅对 UnsafePointer，设置一个新的指针
func SetPointer(x unsafe.Pointer)

// 是否可设置值，仅当一个值是是 CanAddr，且是导出的，才能够设置值
func CanSet() bool
// 设置值的通用方法
func Set(Value) 
// 设置为当前类型的空值
func SetZero() 
// 将 *MapIter 当前轮 key 设置到当前值
func SetIterKey(iter *MapIter) 
// 将 *MapIter 当前轮 value 设置到当前值
func SetIterValue(iter *MapIter) 
// 说明：MapIter 是 MapRange() 函数返回的，设置上面两个方法是为了直接从 MapRange 返回的内容设置，避免创建新的 Value 对象

// 一些具体类型的方法
func Bool() bool
func SetBool(bool) 

func Bytes() []byte
func SetBytes() 

func CanFloat() bool
func Float() float64
func SetFloat(float64) 
func OverflowFloat(float64) bool // 判断将给定值赋给当前值时是否会发生溢出

func CanInt() bool
func Int() int64
func SetInt(int64)
func OverflowInt(int64) bool

func CanUint() bool
func Uint() uint64
func SetUint(uint64) 
func OverflowUint(uint64) bool

func CanComplex() bool
func Complex() complex128
func SetComplex(complex128) 
func OverflowComplex(complex128) bool

// 仅对通道，阻塞地接收一个元素
func Recv() (x Value, ok bool)
// 仅对通道，阻塞地发送一个元素
func Send(Value) 
// 仅对通道，非阻塞地接受一个元素
func TryRecv() Value,bool
func TrySend(Value) bool
// 仅对通道，关闭通道
func Close() 

// 如下仅对 map 生效
// 返回指定 key 对应的值的 Value 对象
func MapIndex(key Value) Value
// 返回所有 key
func MapKeys() []Value
// 返回一个用于遍历 map 的迭代器
func MapRange() *MapIter
// 设置一个键值对
func SetMapIndex(key, elem Value) 

// 仅对 array slice string 有用，返回 v[i:j]
func Slice(int,int) Value
// 仅对 array slice 有用，返回 v[i:j:k]
func Slice3(int,int,int) Value
// 仅对 slice 有用，设置容量
func SetCap(int) 
// 仅对 slice 有用，设置长度
func SetLen(int) 
// 仅对 slice，增长 n 个容量。增长后，添加 n 个以内的元素都不会再触发内存分配
func Grow(int) 
// 仅对 slice，返回容量
func Cap() int

// 仅对 array slice string 有效，返回第 i 个元素
func Index(int) Value

// 仅对 array slice map chan string 以及指向 array 的指针有效。返回长度
func Len() int

// 仅对 slice 和 map，清空切片或者 map 包含的值
func Clear() 

// 检测调用 Interface() 时会不会 panic
func CanInterface() bool
// 以 interface{} 形式返回值对象代表的值，等效于: var i interface{} = (v's underlying value)
func Interface() 
// 已过时，不用管
func InterfaceData() 

// 如果是 string，就返回字符串的值；否则返回 (T value) 这样的值，比如 <*main.mystruct Value>；它不会调用类型的 String 方法。
func String() string
// 仅对 String 有效，设置字符串
func SetString(string) 

// Func 相关和 Type 中定义的差不多，但是多了 Call 方法
func Method(int) Value
func MethodByName(string) Value
func NumMethod() int
// 调用方法，in 会作为参数逐个传递
func Call(in []Value) []Value
// 调用带有可变参数的方法，in 切片的最后一个元素会被传递给可变参数
func CallSlice(in []Value) []Value

// 是否可转换成目标类型，这里的转换就是 T(x) 这种转换
func CanConvert(Type) bool
func Convert(Type) Value

// 是否可比较，如果当前值是 interface{}，则检查其代表的具体类型是否可比较
func Comparable() bool
// 比较：如果当前值和目标值具有不同的类型，直接返回 false；如果是 interface{} 则比较具体类型；其它情况比较值
// 这个和 == 其实差不对，只不过 == 会在编译器检查并报错
func Equal(Value) bool


// 以下仅对 struct 有效
// 返回第 i 个字段
func Field(int) Value
// 返回嵌套字段
func FieldByIndex([]int) Value
// 返回嵌套字段，如果 index 路径上有空指针，返回一个 error。
func FieldByIndexErr([]int) Value,error
func FieldByName(string) Value
func FieldByNameFunc(func(string) bool) Value
func NumField() int

// 返回当前是否是一个有效值。一般来说，function 和 method 得到的 Value 都是无效的；
// 此外，通过 reflect.Zero() 创建的 Value 是无效的
func IsValid() bool

// 判断当前值是否是其所代表类型的空值
func IsZero() bool

```

#### Addressable Value

什么样的 value 才是可寻址的呢？

所谓可寻址，就是可以获取到原始值的地址信息。可以看一个例子，考虑下面三种情况的寻址情况

```go
a := 12
aValue := reflect.ValueOf(a)
println(aValue.CanAddr()) // false

b := lo.ToPtr(12)
bValue := reflect.ValueOf(b)
println(bValue.CanAddr())        // false
println(bValue.Elem().CanAddr()) // true

s := lo.ToPtr(12)
sValue := reflect.ValueOf(&s)
println(sValue.CanAddr())               // false
println(sValue.Elem().CanAddr())        // true
println(sValue.Elem().Elem().CanAddr()) // true
```

画图分析 reflectValue 的情况

- 对于 a，`reflect.ValueOf(a)` 时获得的是一个副本，原始值丢失了，无论如何都无法寻址
- 对于 b，`reflect.ValueOf(b)` 时获得了指针 b 的副本，该副本指向 12，因此直接获取的 Value 对象是不可寻址的，但其元素指向了原始值 12，可寻址
- 对于 c，有两层指针，最外层指针`&s` 在 `reflect.ValueOf(c)` 时复制过来了，因此它不是原始值，它指向的指针 s 和指针 s 指向的 12 都是原始值，可寻址

![image-20250703094921275](https://gdz.oss-cn-shenzhen.aliyuncs.com/local/image-20250703094921275.png)

#### Addr() 有什么用？

`Addr()` 获取的是一个 Value 的指针构成的 Value，有啥用呢🤔？

一个比较典型的用法是：如果我们在一个类型的指针上定义了方法，但获取到的是该类型的反射 Value 对象，此时可以通过 Addr() 获取到该值的指针 Value 对象，从而访问定义在类型指针上的方法。示例代码

```go
type mystr string

func (m *mystr) Hello() {
	println("hello, mystr")
}

type mystruct struct {
	Field1 mystr
}

func main() {
	s := &mystruct{Field1: "嘻嘻"}
	sValue := reflect.ValueOf(s)

	fieldValue := sValue.Elem().Field(0) // 获取 Field1 的反射值对象，类型是 mystr
	fieldPtrValue := fieldValue.Addr()   // Field1 的地址的反射纸对象，类型是 *mystr

	println(fieldValue.NumMethod())                 // 输出 0
	println(fieldPtrValue.NumMethod())              // 输出 1
	fieldPtrValue.Method(0).Call([]reflect.Value{}) // 输出 hello, mystr
}
```

#### `unsafe.Pointer` 和普通指针区别

- 普通指针是语言合法暴露给用户的，仅在引用类型时我们可以获取到指针，对指针的所有操作是安全的
- 但其实每个被存储的内容都是有地址的，我们可以通过` unsafe.Pointer` 获取到这些地址。如果我们知道变量的内存地址，再知道变量类型的内存结构，我们可以直接通过偏移量等骚操作跳过语法限制直接修改内存中的值来修改变量。如下举例

```go
type MyStruct struct {
	A int32
	B int64
}

func main() {
	s := MyStruct{
		A: 123,
		B: 456,
	}

	basePtr := unsafe.Pointer(&s)
	offsetB := unsafe.Offsetof(s.B)
	bPtr := (*int64)(unsafe.Pointer(uintptr(basePtr) + offsetB))

	// 修改字段 B 的值
	*bPtr = 999

	fmt.Println("s.A =", s.A) // 输出 123
	fmt.Println("s.B =", s.B) // 输出 999（被我们通过偏移写入的）
}
```

#### 分清几个寻址方法

`Addr()`, `UnsafeAddr()`, `Pointer()`, `UnsafePointer()` 几个方法的区别。

- `Addr()`: 返回指向当前值的指针的 Value 对象，只有当前值可寻址时才有效

- `UnsafeAddr()`: 等效于 `uintptr(Value.Addr().UnsafePointer())`
- `Pointer()`:  将当前值当做指针返回，只有当前值是引用类型才有效。等效于`uintptr(Value.UnsafePointer())`
- `UnsafePointer()`:  将当前值当做 `unsafe.Pointer` 返回，同样只有当前值是引用类型才有效

所以其实 `Addr()`, `UnsafeAddr()` 和  `Pointer()`, `UnsafePointer()` 这两个方法没有任何关系，后两个方法和 `Int()` 、`Bool()` 这样的方法类似，就是引用类型的值对象本身的值就是指针，通过 `Pointer()` 或 `UnsafePointer()` 得到原本的指针值罢了。

而 `Addr()` 获取指向当前值的地址的 Value 对象，`UnsafeAddr()` 得到的就是这个地址，即使不是指针或引用类型，只要是可寻址的，就能通过此方式获取到其地址。

#### `Type` 和 `Value` 都有的容易混淆的方法

| 方法        | `reflect.Type`                                               | `reflect.Value`                                              |
| ----------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `Elem()`    | 仅当 slice、array、chan、map、指针 时有效<br />返回它们包含的元素的类型 | 对 interface 或 pointer 有效<br/>- interface 时返回其包含的元素反射值对象；<br />- 指针时返回其执行的元素的反射值对象 |
| `Method(i)` | 返回第 i 个方法定义；<br />方法定义是 `reflect.Method 对象`，是对方法的描述 | 返回第 i 个方法本身；<br />方法本身是一个函数，即一个 `Func` |
| `Field(i)`  | 返回第 i 个字段定义；<br />字段定义是 `reflect.StructField`，`tag` 就从这里获取 | 返回第 i 个字段值本身；<br />是一个 `reflect.Value` 对象。   |

总之掌握一个原则，`reflect.Type` 代表的类型，类型是静态的，在定义时就已确定，`reflect.Type` 的所有方法都是在获取形式类型中的描述信息；`reflect.Value` 代表的是值，复杂不少。

实际使用时候会更多地依赖 `reflect.Value`，毕竟它包含更多信息。

### 操作 `reflect.Value` 的全局方法

```go
// 创建 reflect.Value
// 创建零值
func Zero(typ Type) Value
// 创建切片
func MakeSlice(typ Type, len, cap int) Value
func SliceAt(typ Type, p unsafe.Pointer, n int) Value // 创建切片，切片其实地址是 p
// 创建 map
func MakeMap(typ Type) Value
func MakeMapWithSize(typ Type, n int) Value
// 创建函数
func MakeFunc(typ Type, fn func(args []Value) (results []Value)) Value
// 创建指针
func New(typ Type) Value
func NewAt(typ Type, p unsafe.Pointer) Value // 创建指针，指针的值是传入的 p
// 创建通道
func MakeChan(typ Type, buffer int) Value


// 解一次引用
func Indirect(v Value) Value

// 切片操作
// 逐个元素添加
func Append(s Value, x ...Value) Value 
// 添加一批元素
func AppendSlice(s, t Value) Value

// select 操作
func Select(cases []SelectCase) (chosen int, recv Value, recvOK bool)

// 获取一个变量的 reflect.Value
func ValueOf(i any) Value
```

> 常用的也就 `func ValueOf(i any) Value` 和 `func Indirect(v Value) Value` 两个方法了。

### 三个全局方法

#### `reflect.Copy(Value, Value) n`

- 只对切片或数组有效，两个切片的元素类型必须一样
- 浅拷贝，只拷贝一层
- **不会对目标切片扩容**：如果目标切片容量不够，复制不会发生

```go
// 目标切片长度为0，不会复制任何东西
var s1 []string = make([]string, 0)
var s2 []string = []string{"hello"}
s1Value := reflect.ValueOf(s1)
s2Value := reflect.ValueOf(s2)
result := reflect.Copy(s1Value, s2Value)
// 目标切片长度为 1，能复制成功
var s1 []string = make([]string, 1)
var s2 []string = []string{"hello"}
s1Value := reflect.ValueOf(s1)
s2Value := reflect.ValueOf(s2)
result := reflect.Copy(s1Value, s2Value)
```

#### `func DeepEqual(x, y any) bool`

递归的深度比较，就是我们想的那个意义上的比较，只有所有都相等时候才会相等。有几个特殊的

- `slice` 比较时会比较容量和长度
- `Func` 的比较，只有他们都为 nil 时才会相等，否则不相等。（没错，自己和自己也不相等）

#### `func Swapper(slice any) func(i, j int)`

仅切片有效，返回可用于交换切片元素的函数

### xxx.(type) 与反射的关系

我们时常会看到这种代码。其实这也只是类型断言，和 `writer, ok := xxx.(io.Writer)` 是一样的，唯一区别是，`xxx.(type)` 只能和 switch 配合使用，可以检测多种类型；而 `writer, ok := xxx.(io.Writer)` 只能检测一种类型。
类型断言与反射的唯一关系就是他们都是构建与 Go 的类型系统之上，初次之外没有半毛钱关系。
```go
func retrieveVarAsString(v any) ([]string, bool) {
	// 仅支持基础类型，不支持复杂类型
	var values []string
	switch v := v.(type) {
	case []any:
		......
	case int, int8, int16, int32, int64:
		values = append(values, fmt.Sprintf("%d", v))
	case uint, uint8, uint16, uint32, uint64:
		values = append(values, fmt.Sprintf("%d", v))
	case float32, float64:
		values = append(values, fmt.Sprintf("%f", v))
	case string:
		values = append(values, v)
	default:
		return nil, false
	}
	return values, true
}
```

> 当仅涉及到简单的类型判断是，类型断言是首选：语法更简洁；性能更好（虽然都会在运行时判断动态类型信息，但编译器会对类型断言做优化，不必调用反射包。）

**问**：反射比起类型断言具体性能消耗在哪里？

**答**：

- 构建反射对象：反射需要构建 `reflect.Type` 对象，需要分配内存、需要初始化；而类型断言直接用读取变量的类型指针来判断就行了
- 通用性逻辑：`reflect.Type` 中不止包含类型，还包含每个字段的属性（如可否导出等），无论我们用不用，在创建该对象时都会去遍历这些信息

- reflect.Type 代表什么
- reflect.Value 代表什么
- reflect.Kind 代表什么
- xxx.(type) 怎么工作的？这个也是类型断言的一种。
- Type 和 Value 中那些相同的方法有什么区别？
- AI 出一道有难度的反射操作题目


- 如何获取一个变量的内存地址
- 研究一下 reflect.Value.Pointer() 和 reflect.Value.Addr() 函数

## 练习：实现一个通用的 Struct Tag 校验器

题目：实现一个函数

```go
func ValidateStruct(s interface{}) error
```

 当传入一个结构体时，该函数会检查结构体中被标记为 `validate:"required"` 的字段是否为“零值”。

- 如果字段是零值（例如 `""`、`0`、`nil`、`false`），则认为验证失败，返回一个错误，包含所有未通过验证的字段名称。
- 支持嵌套结构体递归校验。
- 忽略私有字段。
- 只处理结构体类型（否则返回 error）。
- 支持 `slice`、`map`、`array` 等
- 也可以附加支持 `min`、`max`、`email` 等验证

如下是一个实现了 `required` 和 `min` 的版本。实现时主要注意要先对字段做 validate 验证，再根据字段是否是复合类型决定是否验证其元素，因为无论字段是何种类型，都可能需要进行验证（比如 `required` 也需要验证指针、`interface{}` 等	）

```go

func validate(in interface{}) error {
	return validateValue(reflect.ValueOf(in))
}

func validateValue(v reflect.Value) error {
	switch v.Kind() {
	case reflect.Slice, reflect.Array:
		for i := 0; i < v.Len(); i++ {
			if err := validateValue(v.Index(i)); err != nil {
				return err
			}
		}
	case reflect.Map:
		iter := v.MapRange()
		for iter.Next() {
			if err := validateValue(iter.Value()); err != nil {
				return err
			}
		}
	case reflect.Pointer, reflect.Interface:
		if v.IsNil() {
			return nil
		}
		return validateValue(v.Elem())
	case reflect.Struct:
		for i := 0; i < v.NumField(); i++ {
			fieldValue := v.Field(i)
			structField := v.Type().Field(i)
			fieldName := structField.Name
			fieldTag := structField.Tag

			// 先对当前字段做检查
			validateStr, ok := fieldTag.Lookup("validate")
			if !ok {
				continue
			}
			constraints := strings.Split(validateStr, ",")
			for _, constraint := range constraints {
				if constraint == "required" && fieldValue.IsZero() {
					return fmt.Errorf("字段 %s 不可为空值", fieldName)
				}
				if strings.Contains(constraint, "min=") {
					min := strings.TrimPrefix(constraint, "min=")
					if err := validateMin(fieldName, fieldValue, min); err != nil {
						return err
					}
				}
			}

			// 如果字段是复合类型，还需要对复合类型的元素做检查
			for fieldValue.Kind() == reflect.Interface {
				fieldValue = fieldValue.Elem()
			}
			for fieldValue.Kind() == reflect.Ptr && !fieldValue.IsNil() {
				fieldValue = fieldValue.Elem()
			}
			switch fieldValue.Kind() {
			case reflect.Struct, reflect.Map, reflect.Slice, reflect.Array:
				if err := validateValue(fieldValue); err != nil {
					return err
				}
			}
		}
	default:
		return errors.New("Type not support")
	}
	return nil
}

func validateMin(fieldName string, fieldValue reflect.Value, min string) error {
	minInt, err := strconv.Atoi(min)
	if err != nil {
		return fmt.Errorf("%s: min 的参数必须为 int，实际为 %s.", fieldName, min)
	}
	switch fieldValue.Kind() {
	case reflect.Ptr, reflect.Interface:
		return validateMin(fieldName, fieldValue.Elem(), min)
	case reflect.Int8, reflect.Int16, reflect.Int32, reflect.Int64, reflect.Int:
		if fieldValue.Int() < int64(minInt) {
			return fmt.Errorf("%s:  的值小于最小值 %s", fieldName, min)
		}
		return nil
	default:
		return fmt.Errorf("%s: min 只能用在 int 类型", fieldName)
	}
}
```

