#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup

html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>
		    					    		</div>
		    		<div class="clr"></div>
		    	</div>
		    </form>
		    <table class="tablelist" cellpadding="0" cellspacing="0">
		    	<tbody><tr class="h">
		    		<td class="l" width="374">职位名称</td>
		    		<td>职位类别</td>
		    		<td>人数</td>
		    		<td>地点</td>
		    		<td>发布时间</td>
		    	</tr>
		    			    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=47428&amp;keywords=python&amp;tid=0&amp;lid=0">30628-腾讯广告算法高级工程师（研发中心-深圳）</a></td>
					<td>技术类</td>
					<td>1</td>
					<td>深圳</td>
					<td>2019-02-14</td>
		    	</tr>
		    			    	<tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=47423&amp;keywords=python&amp;tid=0&amp;lid=0">TEG02-网络运维工程师</a></td>
					<td>技术类</td>
					<td>1</td>
					<td>深圳</td>
					<td>2019-02-14</td>
		    	</tr>
		    			    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=47411&amp;keywords=python&amp;tid=0&amp;lid=0">22989-腾讯云资深运营开发工程师（深圳）</a></td>
					<td>技术类</td>
					<td>2</td>
					<td>深圳</td>
					<td>2019-02-14</td>
		    	</tr>
		    			    	<tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=47396&amp;keywords=python&amp;tid=0&amp;lid=0">PCG11-后台开发工程师（北京）</a></td>
					<td>技术类</td>
					<td>1</td>
					<td>北京</td>
					<td>2019-02-14</td>
		    	</tr>
		    			    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=47379&amp;keywords=python&amp;tid=0&amp;lid=0">22989-腾讯云serverless运营开发工程师（深圳总部）</a></td>
					<td>技术类</td>
					<td>2</td>
					<td>深圳</td>
					<td>2019-02-14</td>
		    	</tr>
		    			    	<tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=47380&amp;keywords=python&amp;tid=0&amp;lid=0">22989-腾讯云serverless运营开发工程师（成都）</a></td>
					<td>技术类</td>
					<td>2</td>
					<td>成都</td>
					<td>2019-02-14</td>
		    	</tr>
		    			    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=47374&amp;keywords=python&amp;tid=0&amp;lid=0">18436-NLP算法研究员（深圳）</a></td>
					<td>技术类</td>
					<td>1</td>
					<td>深圳</td>
					<td>2019-02-14</td>
		    	</tr>
		    			    	<tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=47359&amp;keywords=python&amp;tid=0&amp;lid=0">PCG17-QQ钱包后台开发工程师（深圳）</a></td>
					<td>技术类</td>
					<td>1</td>
					<td>深圳</td>
					<td>2019-02-14</td>
		    	</tr>
		    			    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=47353&amp;keywords=python&amp;tid=0&amp;lid=0">23295-互娱游戏数据营销经理（深圳）</a></td>
					<td>市场类</td>
					<td>1</td>
					<td>深圳</td>
					<td>2019-02-14</td>
		    	</tr>
		    			    	<tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=47354&amp;keywords=python&amp;tid=0&amp;lid=0">30359-后台开发高级工程师（北京）</a></td>
					<td>技术类</td>
					<td>1</td>
					<td>北京</td>
					<td>2019-02-14</td>
		    	</tr>
		    			    	<tr class="f">
		    		<td colspan="5"></title>
</head>
<body>

</body>
</html>


"""

bs= BeautifulSoup(html,"lxml")
# 第二个参数是解析器
# 不指定的话用bs4自带的 html.parser   python标准库
# lxml   xml   html5lib（容错最强）
#
print(bs.prettify())