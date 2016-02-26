import codecs

from bs4 import BeautifulSoup
from lxml import etree

from dateutil.parser import parse
import time
from datetime import *
test_data = '''
26.02 15:51:43,665 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 START: ru.crystals.transport.PGQManagerImpl.insertEvent["products_s2_c1", "product", "products_2_all_2016_02_26__15_51_43_f31a3ada-9e35-4e27-a7b4-b7d1c8c45ef6.ser"]
26.02 15:51:43,666 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 Time:1 FINISH: ru.crystals.transport.PGQManagerImpl.insertEvent
26.02 15:51:43,666 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 START: ru.crystals.transport.PGQManagerImpl.insertEvent["products_s2_c2", "product", "products_2_all_2016_02_26__15_51_43_f31a3ada-9e35-4e27-a7b4-b7d1c8c45ef6.ser"]
26.02 15:51:43,666 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 Time:0 FINISH: ru.crystals.transport.PGQManagerImpl.insertEvent
26.02 15:51:43,667 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 START: ru.crystals.transport.PGQManagerImpl.insertEvent["products_s2_c3", "product", "products_2_all_2016_02_26__15_51_43_f31a3ada-9e35-4e27-a7b4-b7d1c8c45ef6.ser"]
26.02 15:51:43,667 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 Time:0 FINISH: ru.crystals.transport.PGQManagerImpl.insertEvent
26.02 15:51:43,668 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 START: ru.crystals.transport.PGQManagerImpl.insertEvent["products_s2_c4", "product", "products_2_all_2016_02_26__15_51_43_f31a3ada-9e35-4e27-a7b4-b7d1c8c45ef6.ser"]
26.02 15:51:43,669 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 Time:1 FINISH: ru.crystals.transport.PGQManagerImpl.insertEvent
26.02 15:51:43,669 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 START: ru.crystals.transport.PGQManagerImpl.insertEvent["products_s2_c5", "product", "products_2_all_2016_02_26__15_51_43_f31a3ada-9e35-4e27-a7b4-b7d1c8c45ef6.ser"]
26.02 15:51:43,670 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 Time:1 FINISH: ru.crystals.transport.PGQManagerImpl.insertEvent
26.02 15:51:43,670 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 START: ru.crystals.transport.PGQManagerImpl.insertEvent["products_s2_c6", "product", "products_2_all_2016_02_26__15_51_43_f31a3ada-9e35-4e27-a7b4-b7d1c8c45ef6.ser"]
26.02 15:51:43,671 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 Time:1 FINISH: ru.crystals.transport.PGQManagerImpl.insertEvent
26.02 15:51:43,671 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 START: ru.crystals.transport.PGQManagerImpl.insertEvent["products_s2_c7", "product", "products_2_all_2016_02_26__15_51_43_f31a3ada-9e35-4e27-a7b4-b7d1c8c45ef6.ser"]
26.02 15:51:43,672 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 Time:1 FINISH: ru.crystals.transport.PGQManagerImpl.insertEvent
26.02 15:51:43,672 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 START: ru.crystals.transport.PGQManagerImpl.insertEvent["products_s2_c8", "product", "products_2_all_2016_02_26__15_51_43_f31a3ada-9e35-4e27-a7b4-b7d1c8c45ef6.ser"]
26.02 15:51:43,673 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 Time:1 FINISH: ru.crystals.transport.PGQManagerImpl.insertEvent
26.02 15:51:43,673 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 START: ru.crystals.transport.PGQManagerImpl.insertEvent["products_s2_c9", "product", "products_2_all_2016_02_26__15_51_43_f31a3ada-9e35-4e27-a7b4-b7d1c8c45ef6.ser"]
26.02 15:51:43,674 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 Time:1 FINISH: ru.crystals.transport.PGQManagerImpl.insertEvent
26.02 15:51:43,675 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 START: ru.crystals.transport.PGQManagerImpl.insertEvent["products_s2_c1", "product", "products_2_all_2016_02_26__15_51_43_99c1e017-e491-4e43-8a3d-fefe84fc5dab.ser"]
26.02 15:51:43,676 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 Time:1 FINISH: ru.crystals.transport.PGQManagerImpl.insertEvent
26.02 15:51:43,677 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 START: ru.crystals.transport.PGQManagerImpl.insertEvent["products_s2_c2", "product", "products_2_all_2016_02_26__15_51_43_99c1e017-e491-4e43-8a3d-fefe84fc5dab.ser"]
26.02 15:51:43,718 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 Time:41 FINISH: ru.crystals.transport.PGQManagerImpl.insertEvent
26.02 15:51:43,718 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 START: ru.crystals.transport.PGQManagerImpl.insertEvent["products_s2_c3", "product", "products_2_all_2016_02_26__15_51_43_99c1e017-e491-4e43-8a3d-fefe84fc5dab.ser"]
26.02 15:51:43,719 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 Time:1 FINISH: ru.crystals.transport.PGQManagerImpl.insertEvent
26.02 15:51:43,719 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 START: ru.crystals.transport.PGQManagerImpl.insertEvent["products_s2_c4", "product", "products_2_all_2016_02_26__15_51_43_99c1e017-e491-4e43-8a3d-fefe84fc5dab.ser"]
26.02 15:51:43,720 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 Time:1 FINISH: ru.crystals.transport.PGQManagerImpl.insertEvent
26.02 15:51:43,720 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 START: ru.crystals.transport.PGQManagerImpl.insertEvent["products_s2_c5", "product", "products_2_all_2016_02_26__15_51_43_99c1e017-e491-4e43-8a3d-fefe84fc5dab.ser"]
26.02 15:51:43,721 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 Time:1 FINISH: ru.crystals.transport.PGQManagerImpl.insertEvent
26.02 15:51:43,721 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 START: ru.crystals.transport.PGQManagerImpl.insertEvent["products_s2_c6", "product", "products_2_all_2016_02_26__15_51_43_99c1e017-e491-4e43-8a3d-fefe84fc5dab.ser"]
26.02 15:51:43,722 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 Time:1 FINISH: ru.crystals.transport.PGQManagerImpl.insertEvent
26.02 15:51:43,722 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 START: ru.crystals.transport.PGQManagerImpl.insertEvent["products_s2_c7", "product", "products_2_all_2016_02_26__15_51_43_99c1e017-e491-4e43-8a3d-fefe84fc5dab.ser"]
26.02 15:51:43,723 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 Time:1 FINISH: ru.crystals.transport.PGQManagerImpl.insertEvent
26.02 15:51:43,723 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 START: ru.crystals.transport.PGQManagerImpl.insertEvent["products_s2_c8", "product", "products_2_all_2016_02_26__15_51_43_99c1e017-e491-4e43-8a3d-fefe84fc5dab.ser"]
26.02 15:51:43,724 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 Time:1 FINISH: ru.crystals.transport.PGQManagerImpl.insertEvent
26.02 15:51:43,724 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 START: ru.crystals.transport.PGQManagerImpl.insertEvent["products_s2_c9", "product", "products_2_all_2016_02_26__15_51_43_99c1e017-e491-4e43-8a3d-fefe84fc5dab.ser"]
26.02 15:51:43,726 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 Time:2 FINISH: ru.crystals.transport.PGQManagerImpl.insertEvent
26.02 15:51:43,726 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 Time:64 FINISH: ru.crystals.setretailx.products.transport.sending.MessageSender.writeObjectsToFileFast
26.02 15:51:43,726 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 START: ru.crystals.setretailx.products.transport.sending.MessageSender.writeObjectsToFileFast[<java.util.ArrayList ,size: 125>, 3, <com.google.common.collect.AbstractMapBasedMultimap$RandomAccessWrappedList ,size: 9>, null]
26.02 15:51:43,730 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 START: ru.crystals.transport.PGQManagerImpl.insertEvent["products_s3_c1", "product", "products_3_all_2016_02_26__15_51_43_d4dde3a6-54b6-4601-ad13-e8e2b684bba7.ser"]
26.02 15:51:43,731 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 Time:1 FINISH: ru.crystals.transport.PGQManagerImpl.insertEvent
26.02 15:51:43,732 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 START: ru.crystals.transport.PGQManagerImpl.insertEvent["products_s3_c2", "product", "products_3_all_2016_02_26__15_51_43_d4dde3a6-54b6-4601-ad13-e8e2b684bba7.ser"]
26.02 15:51:43,733 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 Time:1 FINISH: ru.crystals.transport.PGQManagerImpl.insertEvent
26.02 15:51:43,733 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 START: ru.crystals.transport.PGQManagerImpl.insertEvent["products_s3_c3", "product", "products_3_all_2016_02_26__15_51_43_d4dde3a6-54b6-4601-ad13-e8e2b684bba7.ser"]
26.02 15:51:43,734 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 Time:1 FINISH: ru.crystals.transport.PGQManagerImpl.insertEvent
26.02 15:51:43,734 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 START: ru.crystals.transport.PGQManagerImpl.insertEvent["products_s3_c4", "product", "products_3_all_2016_02_26__15_51_43_d4dde3a6-54b6-4601-ad13-e8e2b684bba7.ser"]
26.02 15:51:43,734 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 Time:0 FINISH: ru.crystals.transport.PGQManagerImpl.insertEvent
26.02 15:51:43,735 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:285 START: ru.crystals.ERPIntegration.products.plugins.WSGoodsCatalogImport.getGoodsCatalogWithTi[<[B ,size: 236124>, "not_specified"]
26.02 15:51:43,735 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 START: ru.crystals.transport.PGQManagerImpl.insertEvent["products_s3_c5", "product", "products_3_all_2016_02_26__15_51_43_d4dde3a6-54b6-4601-ad13-e8e2b684bba7.ser"]
26.02 15:51:43,736 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 Time:1 FINISH: ru.crystals.transport.PGQManagerImpl.insertEvent
26.02 15:51:43,736 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 START: ru.crystals.transport.PGQManagerImpl.insertEvent["products_s3_c6", "product", "products_3_all_2016_02_26__15_51_43_d4dde3a6-54b6-4601-ad13-e8e2b684bba7.ser"]
26.02 15:51:43,737 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 Time:1 FINISH: ru.crystals.transport.PGQManagerImpl.insertEvent
26.02 15:51:43,737 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 START: ru.crystals.transport.PGQManagerImpl.insertEvent["products_s3_c7", "product", "products_3_all_2016_02_26__15_51_43_d4dde3a6-54b6-4601-ad13-e8e2b684bba7.ser"]
26.02 15:51:43,739 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 Time:2 FINISH: ru.crystals.transport.PGQManagerImpl.insertEvent
26.02 15:51:43,739 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 START: ru.crystals.transport.PGQManagerImpl.insertEvent["products_s3_c8", "product", "products_3_all_2016_02_26__15_51_43_d4dde3a6-54b6-4601-ad13-e8e2b684bba7.ser"]
26.02 15:51:43,740 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 Time:1 FINISH: ru.crystals.transport.PGQManagerImpl.insertEvent
26.02 15:51:43,740 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 START: ru.crystals.transport.PGQManagerImpl.insertEvent["products_s3_c9", "product", "products_3_all_2016_02_26__15_51_43_d4dde3a6-54b6-4601-ad13-e8e2b684bba7.ser"]
26.02 15:51:43,741 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 Time:1 FINISH: ru.crystals.transport.PGQManagerImpl.insertEvent
26.02 15:51:43,742 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 START: ru.crystals.transport.PGQManagerImpl.insertEvent["products_s3_c1", "product", "products_3_all_2016_02_26__15_51_43_7b0a25c0-a8d5-4334-898c-ce8bf1d1e7c2.ser"]
26.02 15:51:43,743 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 Time:1 FINISH: ru.crystals.transport.PGQManagerImpl.insertEvent
26.02 15:51:43,743 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 START: ru.crystals.transport.PGQManagerImpl.insertEvent["products_s3_c2", "product", "products_3_all_2016_02_26__15_51_43_7b0a25c0-a8d5-4334-898c-ce8bf1d1e7c2.ser"]
26.02 15:51:43,744 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 Time:1 FINISH: ru.crystals.transport.PGQManagerImpl.insertEvent
26.02 15:51:43,744 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 START: ru.crystals.transport.PGQManagerImpl.insertEvent["products_s3_c3", "product", "products_3_all_2016_02_26__15_51_43_7b0a25c0-a8d5-4334-898c-ce8bf1d1e7c2.ser"]
26.02 15:51:43,745 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 Time:1 FINISH: ru.crystals.transport.PGQManagerImpl.insertEvent
26.02 15:51:43,745 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 START: ru.crystals.transport.PGQManagerImpl.insertEvent["products_s3_c4", "product", "products_3_all_2016_02_26__15_51_43_7b0a25c0-a8d5-4334-898c-ce8bf1d1e7c2.ser"]
26.02 15:51:43,746 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 Time:1 FINISH: ru.crystals.transport.PGQManagerImpl.insertEvent
26.02 15:51:43,746 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 START: ru.crystals.transport.PGQManagerImpl.insertEvent["products_s3_c5", "product", "products_3_all_2016_02_26__15_51_43_7b0a25c0-a8d5-4334-898c-ce8bf1d1e7c2.ser"]
26.02 15:51:43,748 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 Time:2 FINISH: ru.crystals.transport.PGQManagerImpl.insertEvent
26.02 15:51:43,748 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 START: ru.crystals.transport.PGQManagerImpl.insertEvent["products_s3_c6", "product", "products_3_all_2016_02_26__15_51_43_7b0a25c0-a8d5-4334-898c-ce8bf1d1e7c2.ser"]
26.02 15:51:43,748 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 Time:0 FINISH: ru.crystals.transport.PGQManagerImpl.insertEvent
26.02 15:51:43,749 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 START: ru.crystals.transport.PGQManagerImpl.insertEvent["products_s3_c7", "product", "products_3_all_2016_02_26__15_51_43_7b0a25c0-a8d5-4334-898c-ce8bf1d1e7c2.ser"]
26.02 15:51:43,749 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 Time:0 FINISH: ru.crystals.transport.PGQManagerImpl.insertEvent
26.02 15:51:43,750 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 START: ru.crystals.transport.PGQManagerImpl.insertEvent["products_s3_c8", "product", "products_3_all_2016_02_26__15_51_43_7b0a25c0-a8d5-4334-898c-ce8bf1d1e7c2.ser"]
26.02 15:51:43,751 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 Time:1 FINISH: ru.crystals.transport.PGQManagerImpl.insertEvent
26.02 15:51:43,751 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 START: ru.crystals.transport.PGQManagerImpl.insertEvent["products_s3_c9", "product", "products_3_all_2016_02_26__15_51_43_7b0a25c0-a8d5-4334-898c-ce8bf1d1e7c2.ser"]
26.02 15:51:43,752 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 Time:1 FINISH: ru.crystals.transport.PGQManagerImpl.insertEvent
26.02 15:51:43,752 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 Time:26 FINISH: ru.crystals.setretailx.products.transport.sending.MessageSender.writeObjectsToFileFast
26.02 15:51:43,840 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:285 Time:105 FINISH: ru.crystals.ERPIntegration.products.plugins.WSGoodsCatalogImport.getGoodsCatalogWithTi
26.02 15:51:43,892 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:285 START: ru.crystals.ERPIntegration.products.plugins.WSGoodsCatalogImport.getGoodsCatalogWithTi[<[B ,size: 236138>, "not_specified"]
26.02 15:51:44,047 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:285 Time:155 FINISH: ru.crystals.ERPIntegration.products.plugins.WSGoodsCatalogImport.getGoodsCatalogWithTi
26.02 15:51:44,108 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:285 START: ru.crystals.ERPIntegration.products.plugins.WSGoodsCatalogImport.getGoodsCatalogWithTi[<[B ,size: 236131>, "not_specified"]
26.02 15:51:44,255 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:285 Time:147 FINISH: ru.crystals.ERPIntegration.products.plugins.WSGoodsCatalogImport.getGoodsCatalogWithTi
26.02 15:51:44,309 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:285 START: ru.crystals.ERPIntegration.products.plugins.WSGoodsCatalogImport.getGoodsCatalogWithTi[<[B ,size: 236129>, "not_specified"]
26.02 15:51:44,450 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:285 Time:141 FINISH: ru.crystals.ERPIntegration.products.plugins.WSGoodsCatalogImport.getGoodsCatalogWithTi
26.02 15:51:44,502 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:285 START: ru.crystals.ERPIntegration.products.plugins.WSGoodsCatalogImport.getGoodsCatalogWithTi[<[B ,size: 236130>, "not_specified"]
26.02 15:51:44,601 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:285 Time:99 FINISH: ru.crystals.ERPIntegration.products.plugins.WSGoodsCatalogImport.getGoodsCatalogWithTi
26.02 15:51:44,672 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:285 START: ru.crystals.ERPIntegration.products.plugins.WSGoodsCatalogImport.getGoodsCatalogWithTi[<[B ,size: 236147>, "not_specified"]
26.02 15:51:44,786 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:285 Time:114 FINISH: ru.crystals.ERPIntegration.products.plugins.WSGoodsCatalogImport.getGoodsCatalogWithTi
26.02 15:51:44,869 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:285 START: ru.crystals.ERPIntegration.products.plugins.WSGoodsCatalogImport.getGoodsCatalogWithTi[<[B ,size: 236140>, "not_specified"]
26.02 15:51:44,983 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:285 Time:114 FINISH: ru.crystals.ERPIntegration.products.plugins.WSGoodsCatalogImport.getGoodsCatalogWithTi
26.02 15:51:45,196 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:285 START: ru.crystals.ERPIntegration.products.plugins.WSGoodsCatalogImport.getGoodsCatalogWithTi[<[B ,size: 236125>, "not_specified"]
26.02 15:51:45,310 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:285 Time:114 FINISH: ru.crystals.ERPIntegration.products.plugins.WSGoodsCatalogImport.getGoodsCatalogWithTi
26.02 15:51:45,393 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:285 START: ru.crystals.ERPIntegration.products.plugins.WSGoodsCatalogImport.getGoodsCatalogWithTi[<[B ,size: 236142>, "not_specified"]
26.02 15:51:45,508 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:285 Time:115 FINISH: ru.crystals.ERPIntegration.products.plugins.WSGoodsCatalogImport.getGoodsCatalogWithTi
26.02 15:51:45,559 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:285 START: ru.crystals.ERPIntegration.products.plugins.WSGoodsCatalogImport.getGoodsCatalogWithTi[<[B ,size: 236130>, "not_specified"]
26.02 15:51:45,700 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:285 Time:142 FINISH: ru.crystals.ERPIntegration.products.plugins.WSGoodsCatalogImport.getGoodsCatalogWithTi
26.02 15:51:45,753 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:285 START: ru.crystals.ERPIntegration.products.plugins.WSGoodsCatalogImport.getGoodsCatalogWithTi[<[B ,size: 236128>, "not_specified"]
26.02 15:51:45,884 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 START: ru.crystals.setretailx.products.transport.sending.MessageSender.writeObjectsToFileFast[<java.util.ArrayList ,size: 125>, 1, <com.google.common.collect.AbstractMapBasedMultimap$RandomAccessWrappedList ,size: 9>, null]
26.02 15:51:45,897 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 START: ru.crystals.transport.PGQManagerImpl.insertEvent["products_s1_c1", "product", "products_1_all_2016_02_26__15_51_45_78debb20-7dd2-4ff7-b2da-248b100c0614.ser"]
26.02 15:51:45,899 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 Time:2 FINISH: ru.crystals.transport.PGQManagerImpl.insertEvent
26.02 15:51:45,899 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 START: ru.crystals.transport.PGQManagerImpl.insertEvent["products_s1_c2", "product", "products_1_all_2016_02_26__15_51_45_78debb20-7dd2-4ff7-b2da-248b100c0614.ser"]
26.02 15:51:45,900 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 Time:1 FINISH: ru.crystals.transport.PGQManagerImpl.insertEvent
26.02 15:51:45,900 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 START: ru.crystals.transport.PGQManagerImpl.insertEvent["products_s1_c3", "product", "products_1_all_2016_02_26__15_51_45_78debb20-7dd2-4ff7-b2da-248b100c0614.ser"]
26.02 15:51:45,901 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 Time:1 FINISH: ru.crystals.transport.PGQManagerImpl.insertEvent
26.02 15:51:45,901 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 START: ru.crystals.transport.PGQManagerImpl.insertEvent["products_s1_c4", "product", "products_1_all_2016_02_26__15_51_45_78debb20-7dd2-4ff7-b2da-248b100c0614.ser"]
26.02 15:51:45,902 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 Time:1 FINISH: ru.crystals.transport.PGQManagerImpl.insertEvent
26.02 15:51:45,902 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 START: ru.crystals.transport.PGQManagerImpl.insertEvent["products_s1_c5", "product", "products_1_all_2016_02_26__15_51_45_78debb20-7dd2-4ff7-b2da-248b100c0614.ser"]
26.02 15:51:45,903 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 Time:1 FINISH: ru.crystals.transport.PGQManagerImpl.insertEvent
26.02 15:51:45,903 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 START: ru.crystals.transport.PGQManagerImpl.insertEvent["products_s1_c6", "product", "products_1_all_2016_02_26__15_51_45_78debb20-7dd2-4ff7-b2da-248b100c0614.ser"]
26.02 15:51:45,905 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 Time:2 FINISH: ru.crystals.transport.PGQManagerImpl.insertEvent
26.02 15:51:45,905 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 START: ru.crystals.transport.PGQManagerImpl.insertEvent["products_s1_c7", "product", "products_1_all_2016_02_26__15_51_45_78debb20-7dd2-4ff7-b2da-248b100c0614.ser"]
26.02 15:51:45,906 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 Time:1 FINISH: ru.crystals.transport.PGQManagerImpl.insertEvent
26.02 15:51:45,906 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 START: ru.crystals.transport.PGQManagerImpl.insertEvent["products_s1_c8", "product", "products_1_all_2016_02_26__15_51_45_78debb20-7dd2-4ff7-b2da-248b100c0614.ser"]
26.02 15:51:45,906 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 Time:0 FINISH: ru.crystals.transport.PGQManagerImpl.insertEvent
26.02 15:51:45,907 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 START: ru.crystals.transport.PGQManagerImpl.insertEvent["products_s1_c9", "product", "products_1_all_2016_02_26__15_51_45_78debb20-7dd2-4ff7-b2da-248b100c0614.ser"]
26.02 15:51:45,907 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 Time:0 FINISH: ru.crystals.transport.PGQManagerImpl.insertEvent
26.02 15:51:45,909 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 START: ru.crystals.transport.PGQManagerImpl.insertEvent["products_s1_c1", "product", "products_1_all_2016_02_26__15_51_45_a87d749f-5909-43be-b5fe-8b0ff81a5502.ser"]
26.02 15:51:45,910 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 Time:1 FINISH: ru.crystals.transport.PGQManagerImpl.insertEvent
26.02 15:51:45,910 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 START: ru.crystals.transport.PGQManagerImpl.insertEvent["products_s1_c2", "product", "products_1_all_2016_02_26__15_51_45_a87d749f-5909-43be-b5fe-8b0ff81a5502.ser"]
26.02 15:51:45,911 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 Time:1 FINISH: ru.crystals.transport.PGQManagerImpl.insertEvent
26.02 15:51:45,911 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 START: ru.crystals.transport.PGQManagerImpl.insertEvent["products_s1_c3", "product", "products_1_all_2016_02_26__15_51_45_a87d749f-5909-43be-b5fe-8b0ff81a5502.ser"]
26.02 15:51:45,912 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 Time:1 FINISH: ru.crystals.transport.PGQManagerImpl.insertEvent
26.02 15:51:45,912 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 START: ru.crystals.transport.PGQManagerImpl.insertEvent["products_s1_c4", "product", "products_1_all_2016_02_26__15_51_45_a87d749f-5909-43be-b5fe-8b0ff81a5502.ser"]
26.02 15:51:45,913 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 Time:1 FINISH: ru.crystals.transport.PGQManagerImpl.insertEvent
26.02 15:51:45,913 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 START: ru.crystals.transport.PGQManagerImpl.insertEvent["products_s1_c5", "product", "products_1_all_2016_02_26__15_51_45_a87d749f-5909-43be-b5fe-8b0ff81a5502.ser"]
26.02 15:51:45,914 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 Time:1 FINISH: ru.crystals.transport.PGQManagerImpl.insertEvent
26.02 15:51:45,915 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 START: ru.crystals.transport.PGQManagerImpl.insertEvent["products_s1_c6", "product", "products_1_all_2016_02_26__15_51_45_a87d749f-5909-43be-b5fe-8b0ff81a5502.ser"]
26.02 15:51:45,916 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 Time:1 FINISH: ru.crystals.transport.PGQManagerImpl.insertEvent
26.02 15:51:45,916 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 START: ru.crystals.transport.PGQManagerImpl.insertEvent["products_s1_c7", "product", "products_1_all_2016_02_26__15_51_45_a87d749f-5909-43be-b5fe-8b0ff81a5502.ser"]
26.02 15:51:45,917 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 Time:1 FINISH: ru.crystals.transport.PGQManagerImpl.insertEvent
26.02 15:51:45,917 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 START: ru.crystals.transport.PGQManagerImpl.insertEvent["products_s1_c8", "product", "products_1_all_2016_02_26__15_51_45_a87d749f-5909-43be-b5fe-8b0ff81a5502.ser"]
26.02 15:51:45,918 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 Time:1 FINISH: ru.crystals.transport.PGQManagerImpl.insertEvent
26.02 15:51:45,918 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 START: ru.crystals.transport.PGQManagerImpl.insertEvent["products_s1_c9", "product", "products_1_all_2016_02_26__15_51_45_a87d749f-5909-43be-b5fe-8b0ff81a5502.ser"]
26.02 15:51:45,919 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 Time:1 FINISH: ru.crystals.transport.PGQManagerImpl.insertEvent
26.02 15:51:45,919 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 Time:35 FINISH: ru.crystals.setretailx.products.transport.sending.MessageSender.writeObjectsToFileFast
26.02 15:51:45,920 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:285 Time:167 FINISH: ru.crystals.ERPIntegration.products.plugins.WSGoodsCatalogImport.getGoodsCatalogWithTi
26.02 15:51:45,920 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 START: ru.crystals.setretailx.products.transport.sending.MessageSender.writeObjectsToFileFast[<java.util.ArrayList ,size: 125>, 2, <com.google.common.collect.AbstractMapBasedMultimap$RandomAccessWrappedList ,size: 9>, null]
26.02 15:51:45,923 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 START: ru.crystals.transport.PGQManagerImpl.insertEvent["products_s2_c1", "product", "products_2_all_2016_02_26__15_51_45_74723255-50b5-48ef-ab14-b48cea263236.ser"]
26.02 15:51:45,924 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 Time:1 FINISH: ru.crystals.transport.PGQManagerImpl.insertEvent
26.02 15:51:45,924 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 START: ru.crystals.transport.PGQManagerImpl.insertEvent["products_s2_c2", "product", "products_2_all_2016_02_26__15_51_45_74723255-50b5-48ef-ab14-b48cea263236.ser"]
26.02 15:51:45,925 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 Time:1 FINISH: ru.crystals.transport.PGQManagerImpl.insertEvent
26.02 15:51:45,925 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 START: ru.crystals.transport.PGQManagerImpl.insertEvent["products_s2_c3", "product", "products_2_all_2016_02_26__15_51_45_74723255-50b5-48ef-ab14-b48cea263236.ser"]
26.02 15:51:45,926 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 Time:1 FINISH: ru.crystals.transport.PGQManagerImpl.insertEvent
26.02 15:51:45,927 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 START: ru.crystals.transport.PGQManagerImpl.insertEvent["products_s2_c4", "product", "products_2_all_2016_02_26__15_51_45_74723255-50b5-48ef-ab14-b48cea263236.ser"]
26.02 15:51:45,928 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 Time:1 FINISH: ru.crystals.transport.PGQManagerImpl.insertEvent
26.02 15:51:45,928 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 START: ru.crystals.transport.PGQManagerImpl.insertEvent["products_s2_c5", "product", "products_2_all_2016_02_26__15_51_45_74723255-50b5-48ef-ab14-b48cea263236.ser"]
26.02 15:51:45,929 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 Time:1 FINISH: ru.crystals.transport.PGQManagerImpl.insertEvent
26.02 15:51:45,929 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 START: ru.crystals.transport.PGQManagerImpl.insertEvent["products_s2_c6", "product", "products_2_all_2016_02_26__15_51_45_74723255-50b5-48ef-ab14-b48cea263236.ser"]
26.02 15:51:45,930 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 Time:1 FINISH: ru.crystals.transport.PGQManagerImpl.insertEvent
26.02 15:51:45,930 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 START: ru.crystals.transport.PGQManagerImpl.insertEvent["products_s2_c7", "product", "products_2_all_2016_02_26__15_51_45_74723255-50b5-48ef-ab14-b48cea263236.ser"]
26.02 15:51:45,931 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 Time:1 FINISH: ru.crystals.transport.PGQManagerImpl.insertEvent
26.02 15:51:45,931 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 START: ru.crystals.transport.PGQManagerImpl.insertEvent["products_s2_c8", "product", "products_2_all_2016_02_26__15_51_45_74723255-50b5-48ef-ab14-b48cea263236.ser"]
26.02 15:51:45,932 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 Time:1 FINISH: ru.crystals.transport.PGQManagerImpl.insertEvent
26.02 15:51:45,932 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 START: ru.crystals.transport.PGQManagerImpl.insertEvent["products_s2_c9", "product", "products_2_all_2016_02_26__15_51_45_74723255-50b5-48ef-ab14-b48cea263236.ser"]
26.02 15:51:45,933 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 Time:1 FINISH: ru.crystals.transport.PGQManagerImpl.insertEvent
26.02 15:51:45,934 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 START: ru.crystals.transport.PGQManagerImpl.insertEvent["products_s2_c1", "product", "products_2_all_2016_02_26__15_51_45_f407e40d-4682-4b86-baad-2b5c6b8b9a58.ser"]
26.02 15:51:45,935 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 Time:1 FINISH: ru.crystals.transport.PGQManagerImpl.insertEvent
26.02 15:51:45,935 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 START: ru.crystals.transport.PGQManagerImpl.insertEvent["products_s2_c2", "product", "products_2_all_2016_02_26__15_51_45_f407e40d-4682-4b86-baad-2b5c6b8b9a58.ser"]
26.02 15:51:45,936 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 Time:1 FINISH: ru.crystals.transport.PGQManagerImpl.insertEvent
26.02 15:51:45,936 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 START: ru.crystals.transport.PGQManagerImpl.insertEvent["products_s2_c3", "product", "products_2_all_2016_02_26__15_51_45_f407e40d-4682-4b86-baad-2b5c6b8b9a58.ser"]
26.02 15:51:45,938 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 Time:2 FINISH: ru.crystals.transport.PGQManagerImpl.insertEvent
26.02 15:51:45,938 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 START: ru.crystals.transport.PGQManagerImpl.insertEvent["products_s2_c4", "product", "products_2_all_2016_02_26__15_51_45_f407e40d-4682-4b86-baad-2b5c6b8b9a58.ser"]
26.02 15:51:45,939 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 Time:1 FINISH: ru.crystals.transport.PGQManagerImpl.insertEvent
26.02 15:51:45,939 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 START: ru.crystals.transport.PGQManagerImpl.insertEvent["products_s2_c5", "product", "products_2_all_2016_02_26__15_51_45_f407e40d-4682-4b86-baad-2b5c6b8b9a58.ser"]
26.02 15:51:45,940 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 Time:1 FINISH: ru.crystals.transport.PGQManagerImpl.insertEvent
26.02 15:51:45,940 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 START: ru.crystals.transport.PGQManagerImpl.insertEvent["products_s2_c6", "product", "products_2_all_2016_02_26__15_51_45_f407e40d-4682-4b86-baad-2b5c6b8b9a58.ser"]
26.02 15:51:45,941 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 Time:1 FINISH: ru.crystals.transport.PGQManagerImpl.insertEvent
26.02 15:51:45,941 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 START: ru.crystals.transport.PGQManagerImpl.insertEvent["products_s2_c7", "product", "products_2_all_2016_02_26__15_51_45_f407e40d-4682-4b86-baad-2b5c6b8b9a58.ser"]
26.02 15:51:45,942 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 Time:1 FINISH: ru.crystals.transport.PGQManagerImpl.insertEvent
26.02 15:51:45,942 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 START: ru.crystals.transport.PGQManagerImpl.insertEvent["products_s2_c8", "product", "products_2_all_2016_02_26__15_51_45_f407e40d-4682-4b86-baad-2b5c6b8b9a58.ser"]
26.02 15:51:45,943 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 Time:1 FINISH: ru.crystals.transport.PGQManagerImpl.insertEvent
26.02 15:51:45,945 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 START: ru.crystals.transport.PGQManagerImpl.insertEvent["products_s2_c9", "product", "products_2_all_2016_02_26__15_51_45_f407e40d-4682-4b86-baad-2b5c6b8b9a58.ser"]
26.02 15:51:45,949 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 Time:5 FINISH: ru.crystals.transport.PGQManagerImpl.insertEvent
'''



#
# '''
# import fileinput
#
# parsed_info = []
# for linenum, line in enumerate(fileinput.input()):
#     if not line.startswith("#DEBUG"):
#         continue # Skip line
#
#     msg = line.partition("MSG")[1] # Get everything after MSG
#     words = msg.split() # Split on words
#     info = {}
#     for w in words:
#         k, _, v = w.partition(":") # Split each word on first :
#         info[k] = v
#
#     parsed_info.append(info)
#
#     if linenum % 10000 == 0: # Or maybe  if len(parsed_info) > 500:
#         # Insert everything in parsed_info to database
#         ...
#         parsed_info = [] # Clear
# '''


class LogData:
    def __init__(self, time_stamp, method_name, execution_time):
        self.time_stamp = time_stamp
        self.method_name = method_name
        self.execution_time = execution_time


class TestData:
    def __init__(self, name, test_id, status, exception):
        self.name = name
        self.id = test_id
        self.status = status
        self.exception = exception


# read file
def get_file_contents(file_name):
    with codecs.open(file_name, mode='r', encoding='utf-8') as tmp_file:
        tmp_data = tmp_file.read()
    return tmp_data


# save data
def save_xml_to_file(xml_data, file_name):
    with codecs.open(file_name, mode='w') as tmp_file:
        tmp_file.write(xml_data)


# 26.02 15:51:46,026 INFO  [ru.crystals.speedlog] SPEEDLOG> ThreadID:217 Time:0 FINISH: ru.crystals.transport.PGQManagerImpl.insertEvent
# time_stamp => FINISH => method? TIME

def parse_perf_data(data):
    counter = 0
    for line in data.split('\n'):
        if "FINISH" not in line:
            continue
        else:
            if "insertEvent" in line:
                counter+=1
                chunks = line.split(' ')


                time =datetime.strptime(chunks[0] + " " + chunks[1], "%d.%m %H:%M:%S,%f")
                total_time = chunks[7][5:]



                print "-----" + str(counter) + "-----"
                print time
                print total_time
                print "-----"



def parse_html_data(html_data):
    soup = BeautifulSoup(html_data, "html.parser")
    collection = []

    for test in soup.find_all('div', {'class': 'test'}):
        case_id = test.attrs['data-test-id']
        name = test.attrs['data-test-name']
        status = test.find('div', {'class': 'results'}).attrs['data-status']
        exception = ''
        if status != 'PASSED':
            exception = test.find('div', {'class': 'exception'}).text

        test_data = TestData(name, case_id, status, exception)
        collection.append(test_data)

    return collection


def wrap_to_junit_xml(tests):
    failed_count = 0

    root_test_suites = etree.Element('testsuites')
    el_test_suite = etree.Element('testsuite')

    for test in tests:
        el_test_case = etree.Element('testcase', name=test.name, classname=test.id)
        # move this shit outta here
        if test.status != "PASSED":
            el_error = etree.Element('error')
            el_error.text = test.exception
            el_test_case.append(el_error)
            failed_count += 1

        el_test_suite.append(el_test_case)

    passed_count = len(tests)
    el_test_suite.set("tests", str(passed_count))
    el_test_suite.set("failures", str(failed_count))
    root_test_suites.append(el_test_suite)

    return etree.tostring(root_test_suites, pretty_print=True, encoding='UTF-8', xml_declaration=False)


if __name__ == "__main__":
    parse_perf_data(get_file_contents("./set-speed.log"))

    # parser = argparse.ArgumentParser(description="Parses custom robot html logs into jUnit xml log format")
    # parser.add_argument("-s", "--source", default="./report.html",
    # help="Source html report file path (default: ./report.html)")
    # parser.add_argument("-r", "--report", default="./report.xml",
    #                     help="Parsed jUnit report file (default: ./report.xml)")

    # args = parser.parse_args()

    # data = get_file_contents(test_data)

    # save_xml_to_file(str(wrap_to_junit_xml(test_collection)), args.report)