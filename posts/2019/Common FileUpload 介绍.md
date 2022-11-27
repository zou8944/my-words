---
created_at: 2019-09-07 22:31:33.0
updated_at: 2021-02-16 23:26:39.301
slug: common-fileupload-introduction
---

> 这是一篇半翻译半笔记式的文章，如果你之前对Common FileUpload了解不多，本文可以快速了解如何使用方法，如果你有时间，推荐你看[官方文档](http://commons.apache.org/proper/commons-fileupload/using.html)

<!--more-->

# 概述
FileUpload能够以多种不同的方式使用，具体取决于应用程序的要求。在最简单的情况下，您将调用单个方法来解析servlet请求，然后处理解析出来的Item集合。此外也可以自定义FileUpload以完全控制各个Item的存储方式，比如设置缓存目录、直接将接收到的Item以流的形式写入数据库等。

> FileUpload依赖于Commons IO，因此类路径下要有Commons IO的jar包。当然采用Maven依赖的方式不用担心，maven会自动为我们下载Commons IO包

# 工作原理
FileUpload依据规范[RFC1867](http://www.ietf.org/rfc/rfc1867.txt)中"基于表单的HTML文件上载"对上传的文件数据进行解析，解析出来的每个项目对应一个FileItem对象。
每个FileItem都有许多我们可能感兴趣的属性：获取contentType，获取原本的文件名，获取文件大小，获取FiledName(如果是表单域上传)，判断是否在内存中，判断是否属于表单域等。
FileUpload使用**FileItemFactory**创建新的FileItem。该工厂可以控制每个项目的创建方式。目前提供的工厂实现可以将项目的数据存储临时存储在内存或磁盘上，具体取决于项目的大小（即数据字节，在指定的大小内时，存在内存中，超出范围，存在磁盘上）。
# 开始之前的判断
在处理上传项目前，最好是先解析一下当前请求是否属于文件上传请求，采用如下方式：

```
//检查我们是否有文件上传请求
boolean isMultipart = ServletFileUpload.isMultipartContent(request);
```
该方法的原理也很简单，就是获取request的contentType以判断是否是multipart，源码如下：

```
public static final boolean isMultipartContent(
            HttpServletRequest request) {
    if (!POST_METHOD.equalsIgnoreCase(request.getMethod())) {
        return false;
    }
    return FileUploadBase.isMultipartContent(new ServletRequestContext(request));
}
```

```
public static final String MULTIPART = "multipart/";
... ...
... ...
public static final boolean isMultipartContent(RequestContext ctx) {
    String contentType = ctx.getContentType();
    if (contentType == null) {
        return false;
    }
    if (contentType.toLowerCase(Locale.ENGLISH).startsWith(MULTIPART)) {
        return true;
    }
    return false;
}
```

# 可用的最简配置
有两种方式能够接收上传文件

 - 传统方式：首先创建FileItemFactory，创建ServletFileUpload时传入factory，再从upload对象获取FileItem，然后调用write(File)直接写入文件。这种方式将接收到的文件临时存储到内存或磁盘中，后续用户再进行处理，比较方便，但是占用时间和空间
 - 流方式：直接ServletFileUpload中获取FileItem，再从FileItem中获取输入流，从流中直接接收数据，没有临时缓存这一步。使用没那么方便，但是比较节省时间和空间

如下演示两种方式
## 使用传统API

```
// Create a factory for disk-based file items
DiskFileItemFactory factory = new DiskFileItemFactory();

// Configure a repository (to ensure a secure temp location is used)
ServletContext servletContext = this.getServletConfig().getServletContext();
File repository = (File) servletContext.getAttribute("javax.servlet.context.tempdir");
factory.setRepository(repository);

// Create a new file upload handler
ServletFileUpload upload = new ServletFileUpload(factory);

// Parse the request
List<FileItem> items = upload.parseRequest(request);
Iterator<FileItem> iter = items.iterator();
while (iter.hasNext()) {
    FileItem item = iter.next();
    
    // upload 是这里假定的上传文件的field name
    if("upload".equals(item.getFieldName)){
	    File uploadFile = new File("...");
	    item.write(uploadFile);
    }
}
```
FileItemFctory可以设置的内容如下

```
factory.setRepository(File dir); // 设置临时文件存储位置
factory.setSizeThreshold(long bytes); // 设置请求大小阈值，当请求大于该值时，接收到的数据是缓存在磁盘中的，否则直接缓存在内存中。
factory.setFileCleaningTracker(FileCleaningTracker pTracker); // 设置临时文件清理跟踪器，后面会讲到
```
ServletFileUpload可以设置的内容如下：

```
upload.setMaxSize(long bytes); //设置整个请求的最大值，大于该值时，是不允许传送的
upload.setFileMaxSize(long bytes); //设置单个文件的最大值，大于该值时，大于该值时，是不允许传送的
upload.setHeaderEncoding(String charset); // 设置读取每个FileItem的头数据的字符编码，不设置时采用request的编码，也没有时采用系统默认编码
upload.setProgressListener(ProgressListener pListener); // 设置上传进度监听器，后面会讲
```
FileItem能够获取的内容如下：

```
item.getContentType(); // 获取单个Item的ContentType
item.getName(); // 获取item本来的文件名，如果不是文件则为null
item.getFieldName(); // 获取item的field名
item.getSize(); // 获取item的大小
item.get(); // 将item转换成字节数组返回
item.isInMemory(); // item目前是否存在内存中
item.isFormField(); // 是否是表单域
item.getInputStream(); // 获取输入流，用于读取item
```

## 使用流API
这种方式其实说来应该是最好的选择，因为他也并不麻烦，而且节省了缓存的空间和时间，在性能上是最好的选择。只需要按照如下方式使用即可
```
// Create a new file upload handler
ServletFileUpload upload = new ServletFileUpload();

// Parse the request
FileItemIterator iter = upload.getItemIterator(request);
while (iter.hasNext()) {
    FileItemStream item = iter.next();
    String fileName = item.getName();
    InputStream stream = item.getInputStream();
    FileOutputStream os = new FileOutputStream(new File(fileName));
    /*
	 *	在这里将输入流的内容写入输出流即可
	 */
}
```

# 文件上传进度监听器
当上传文件非常大时，进度监听器就能够排上用场了，使用方式也非常简单，创建监听器对象，设置到ServletFileUpload即可。

```
ProgressListener listener = new ProgressListener() {
    /*
     * pBytesRead: 到目前为止总共读了多少个Byte
     * pContentLength: 整个content的长度，按Byte计算，也有可能是未知的：-1
     * pItems: 正在读取的item编号，0代表尚未开始读取，1代表第一个，以此类推
     */
    public void update(long pBytesRead, long pContentLength, int pItems) {
        // 获取进度百分比，并放在session中
        request.getSession().setAttribute("progress", 1.0*pBytesRead/pContentLength);
    }
};
upload.setProgressListener(progressListener);

```
此处有一个问题：监听器会被频繁调用，当其内部实现的逻辑较为简单时，可能无伤大雅，但当逻辑较为复杂或占用资源时，监听器就可能影响到程序的性能。
解决方案：以某种方式减少监听器内部逻辑执行的次数，比如下面这种方式

```
ProgressListener progressListener = new ProgressListener(){
   private long megaBytes = -1;
   public void update(long pBytesRead, long pContentLength, int pItems) {
	   // 每接收1M数据才执行一次后面的动作
       long mBytes = pBytesRead / 1000000;
       if (megaBytes == mBytes) {
           return;
       }
       megaBytes = mBytes;
       request.getSession().setAttribute("progress", 1.0*pBytesRead/pContentLength);
   }
};
```

# 临时文件清理跟踪器
文件清理跟踪器仅适用于传统方式: 传统方式在处理文件之前将文件写入临时文件，这样的临时文件在我们上传任务完成时就成了垃圾，需要进行自动回收。Cmmons FileUpload当然也提供了这个功能，其运行原理：org.apache.commons.io.FileCleanerTracker开启一个收割线程，在DiskFileItem被垃圾回收器回收时，自动清理掉对应的临时文件。
要想开启文件自动清理功能，需要按照如下配置：

 - 在Servlet中我们应该在web.xml中配置一个Servlet监听器
```
<listener>
  <listener-class>
    org.apache.commons.fileupload.servlet.FileCleanerCleanup
  </listener-class>
</listener>
```
 - 创建org.apache.commons.io.FileCleaningTracker对象，设置给DiskFileItemFactory。

```
FileCleaningTracker fileCleaningTracker = FileCleanerCleanup.getFileCleaningTracker(context);
DiskFileItemFactory factory = new DiskFileItemFactory();
factory.setFileCleaningTracker(fileCleaningTracker);
```
 - 然后就是按照我们之前学习的步骤正常操作即可

要想禁用临时文件自动删除功能，可将FileCleaningTracker设置为null(其实默认就为null)

```
factory.setFileCleaningTracker(null);
```