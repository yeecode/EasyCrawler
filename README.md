# EasyCrawler

最基本最简单的Python爬虫示例，适合初学者了解爬虫的工作原理和实现，并在此基础上增加功能。

该爬虫的基本功能如下：

- 输入一个入口地址后，会爬取该地址网页中`href=`指向的页面，并将内容下载下来，依次保存
- 对于不能访问的坏链接，将会忽略
- 该爬虫只能爬取入口地址的链接，不再向更深处爬取
- 会自动给页面编ID，并跳过已爬取的页面

整个示例极少依赖外部项目，十分简单、易懂、纯粹。因此该项目不仅便于学习，也便于在此基础上扩充改装。

基于以上功能，我们可以修改实现众多其他功能，包括但不限于：

- 根据页面不断爬取，而不是只爬取一层链接
- 设置爬取范围，例如只爬取某个域名下的链接
- 定时爬取某个地址的数据，并对比其变化
- 只爬取网页中的图片信息
- 等等……