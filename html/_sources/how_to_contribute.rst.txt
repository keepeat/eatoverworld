加入我们
=====================

首先，明确下我们的愿景: 
**帮人民群众找到好吃的!** 


现在，我们需要做的:
**生产优质内容**



Slack
--------------
申请加入Slack: `Slack <https://keepeat.slack.com>`_ 
发送邮件至 wenter.wu@daocloud.io . 




项目结构:
-----------------
Github 地址 `eatoverworld <https://github.com/keepeat/eatoverworld>`_

`source` 文件夹 里包含了所有美食目录。 层级结构按  `城市 - 街区` 分类。
每一家店是一个 POI， 呈卡片形式。



什么是美食点 POI ?
-------------------

`POI <https://zh.wikipedia.org/wiki/%E8%88%88%E8%B6%A3%E9%BB%9E>`_ 描述了我们的美食点的各种信息。 
POI 编写得好不好，对广大人民群众能否找到美食至关重要。
所以，我们的 POI 必须包含以下信息:
	
	- 店铺名
	- 地址 (街道地址)
	- 场景 (和基友去喝酒下馆子， 和女友去约会， 和闺蜜去拍照， 多年未见的同学， 加班餐， 单人餐，早点， 夜宵，下午茶 )
	- 推荐菜 (你点过的那些菜让你至今难忘)
	- 点评地址 (详情页面)


当然，这些信息只是初步的，我们后面会视情况而增加。


怎么编写 POI ? 
-----------------

我们使用 `reStructuredText <http://www.sphinx-doc.org/en/stable/rest.html#rst-primer>`_  编写 POI 。
rest 具有良好的拓展性并且方便写作。



.. toctree::
	:maxdepth: 2
	
	example_poi


How to mirror site?
-------------------------
项目根目录有 Dockerfile, 你可以自己构建镜像。 构建出来是个 Nginx 静态页面。


ToDo
----------


- 瀑布流布局
- 手机录入POI
- 大众点评爬虫
- 相关推荐




