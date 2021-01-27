#!/usr/bin/python3
# -*-: coding: utf-8 -*-
"""
:author: lubosson
:date: 2019-04-15
:desc:
"""
import logging as log
from qichacha.client import QichachaClient
from qichacha.manager import QichachaManager
from db.models import Company

# 企查查客户端
qcc_client = QichachaClient()
manager = QichachaManager()


def start():
    keywords = globals().get('keywords')
    for keyword in keywords:
        raw_companies = qcc_client.search(keyword)
        log.info('正在处理爬取[%s]' % keyword)
        # company对象
        company = Company()
        for raw_company in raw_companies:
            company.keyword = keyword
            # 组装公司信息
            manager.assembly(company, raw_company)
            raw_company_detail = qcc_client.search_detail(raw_company.get('KeyNo'))
            # 补充公司详细信息
            manager.assembly_detail(company, raw_company_detail)
            # 保存到数据库
            # save(company.__dict__)
            log.info(company)
            company.clear()
    log.info('completed')


def load_keys(keys: list):
    globals().setdefault('keywords', keys)










