#!/usr/bin/python3
# -*- coding: utf-8 -*-
#Author: xu
import random

Europe = ['eBay',random.randint(100000,1000000),'许寿龙','France(法国FR)',
          'Liverpool','Lennon Studios，109 cambridge court L7 7AG，Liverpool，UK','L7 7AG']

Korea = ['11street',random.randint(100000,1000000),'许寿龙','South Korea(韩国KR)',
          '首尔市','서울시 강남구 논현동 63-13번지 2층','100-744']

China = ['AliExpress',random.randint(100000,1000000),'许寿龙','China(中国CN)',
          '广东省','民治街道790栋304','518000']

UAS = ['Amazon',random.randint(100000,1000000),'许寿龙','United States(美国US)',
          'Kansas','555 Lexington Avenue, 10th Floor, Room 202','92647']
information = random.choice([Europe,Korea,China,UAS])