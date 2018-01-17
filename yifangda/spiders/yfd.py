#!/usr/bin/env python
# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from yifangda.items import YifangdaItem


class YifangdaSpider(scrapy.Spider):
    name = 'yfd'

    def start_requests(self):
        #pages = 4883
        pages = 4883
        for id in range(1, pages + 1):
            page_url = 'http://www.yyzs.net/zhaoshang/default.aspx?page=%s' % id
            yield scrapy.Request(url=page_url, callback=self.parse)

    def parse(self, response):
        for product_html in response.css('table[id=alternativeTable] a.chanpin::attr(href)').extract():
	    product_res_url = "http://www.yyzs.net/zhaoshang/" + product_html
            yield scrapy.Request(url=product_res_url, callback=self.parse_question)

    def parse_question(self, response):
	product_url = response.url
	product_name = response.css('dl.cp-xx span[id=lbl_shangbiaoming]::text').extract()
	product_tag = response.css('dl.cp-xx span[id=lbl_otc]::text').extract()
	product_point = response.css('dl.cp-xx span[id=lbl_ys]::text').extract()
	investment_area = response.css('dl.cp-xx span[id=lbl_shengfen]::text').extract()
	product_category = response.css('dl.cp-xx span[id=lbl_xiaolei]::text').extract()
	approval_number = response.css('dl.cp-xx span[id=lbl_pzwh]::text').extract()
	manufacture_factory = response.css('dl.cp-xx span[id=lbl_scdw]::text').extract()
	product_pack = response.css('dl.cp-xx span[id=lbl_baoz]::text').extract()
	product_specifications = response.css('dl.cp-xx span[id=lbl_guige]::text').extract()
	product_ingredients = response.css('dl.cp-xx span[id=lbl_chengfen]::text').extract()
	product_usage = response.css('dl.cp-xx span[id=lbl_yfyl]::text').extract()

	product_function = response.css('div[id=tabbox] span[id=lbl_xingneng]::text').extract()

	telphone = response.css('div.zuo-down span[id=lbl_phone]::text').extract()
	mobilephone = response.css('div.zuo-down span[id=lbl_mobile]::text').extract()
	fax = response.css('div.zuo-down span[id=lbl_fax]::text').extract()
	# 联系人有两种类型（lbl_lianxiren和lblPerson）
	contact_name01 = response.css('div.zuo-down span[id=lbl_lianxiren]::text').extract()
	contact_name02 = response.css('div.zuo-down span[id=lbl_lblPerson]::text').extract()
	# QQ有两种类型（lbl_QQ和lblQQ）
	qq01 = response.css('div.zuo-down span[id=lbl_QQ] a::text').extract()
	qq02 = response.css('div.zuo-down span[id=lblQQ] a::text').extract()
	wechat = response.css('div.zuo-down span[id=lbl_wx]::text').extract()
	# 网址有两种类型（lbl_wangzhi和lblWZ）
	address01 = response.css('div.zuo-down span[id=lbl_wangzhi]::text').extract()
	address02 = response.css('div.zuo-down span[id=lblWZ]::text').extract()
	# 邮箱有两种类型（lbl_email和lblMail）
	mail01 = response.css('div.zuo-down span[id=lbl_email]::text').extract()
	mail02 = response.css('div.zuo-down span[id=lblMail]::text').extract()

        # 生成ItemLoder实例
        item_list = ItemLoader(item=YifangdaItem(), response=response)

        #(0)html文件名
        item_list.add_value('product_url', response.url)
        #(1)产品名称
        if product_name:
            item_list.add_value('product_name', product_name)
        else:
            item_list.add_value('product_name', 'None')
        #(2)产品标签
        if product_tag:
            item_list.add_value('product_tag', product_tag)
        else:
            item_list.add_value('product_tag', 'None')
        #(3)产品卖点
        if product_point:
            item_list.add_value('product_point', product_point)
        else:
            item_list.add_value('product_point', 'None')
        #(4)招商区域
        if investment_area:
            item_list.add_value('investment_area', investment_area)
        else:
            item_list.add_value('investment_area', 'None')
        #(5)产品类型
        if product_category:
            item_list.add_value('product_category', product_category)
        else:
            item_list.add_value('product_category', 'None')
        #(6)批准文号
        if approval_number:
            item_list.add_value('approval_number', approval_number)
        else:
            item_list.add_value('approval_number', 'None')
        #(7)生产单位
        if manufacture_factory:
            item_list.add_value('manufacture_factory', manufacture_factory)
        else:
            item_list.add_value('manufacture_factory', 'None')
        #(8)包　　装
        if product_pack:
            item_list.add_value('product_pack', product_pack)
        else:
            item_list.add_value('product_pack', 'None')
        #(9)规　　格
        if product_specifications:
            item_list.add_value('product_specifications', product_specifications)
        else:
            item_list.add_value('product_specifications', 'None')
        #(10)成　　份
        if product_ingredients:
            item_list.add_value('product_ingredients', product_ingredients)
        else:
            item_list.add_value('product_ingredients', 'None')
        #(11)用法用量
        if product_usage:
            item_list.add_value('product_usage', product_usage)
        else:
            item_list.add_value('product_usage', 'None')
        #(12)产品用途或者功能主治
        if product_function:
            item_list.add_value('product_function', product_function)
        else:
            item_list.add_value('product_function', 'None')
        #(13)电  话
        if telphone:
            item_list.add_value('telphone', telphone)
        else:
            item_list.add_value('telphone', 'None')
        #(14)联系手机
        if mobilephone:
            item_list.add_value('mobilephone', mobilephone)
        else:
            item_list.add_value('mobilephone', 'None')
        #(15)传真
        if fax:
            item_list.add_value('fax', fax)
        else:
            item_list.add_value('fax', 'None')
        #(16)联系人
        if contact_name01:
            item_list.add_value('contact_name', contact_name01)
        elif contact_name02:
            contact_name = contact_name02
            item_list.add_value('contact_name', contact_name02)
        else:
            item_list.add_value('contact_name', 'None')
        #(17)联系QQ
        if qq01:
            item_list.add_value('qq', qq01)
        elif qq02:
            item_list.add_value('qq', qq02)
        else:
            item_list.add_value('qq', 'None')
        #(18)联系微信
        if wechat:
            item_list.add_value('wechat', wechat)
        else:
            item_list.add_value('wechat', 'None')
        #(19)地址
        if address01:
            item_list.add_value('address', address01)
        elif address02:
            item_list.add_value('address', address02)
        else:
            item_list.add_value('address', 'None')
        #(20)公司邮箱
        if mail01:
            item_list.add_value('mail', mail01)
        elif mail02:
            item_list.add_value('mail', mail02)
        else:
            item_list.add_value('mail', 'None')

	# 返回数据给itemloder处理
	return item_list.load_item()
	#print item_list.load_item()
