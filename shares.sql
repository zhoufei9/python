/*
Navicat MySQL Data Transfer

Source Server         : 192.168.10.10
Source Server Version : 80021
Source Host           : 192.168.10.10:3306
Source Database       : homestead

Target Server Type    : MYSQL
Target Server Version : 80021
File Encoding         : 65001

Date: 2021-01-10 22:21:42
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for shares
-- ----------------------------
DROP TABLE IF EXISTS `shares`;
CREATE TABLE `shares` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `code` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  `hotTop100_count` int unsigned DEFAULT '0' COMMENT '人气每日排名前100次数统计',
  PRIMARY KEY (`id`),
  UNIQUE KEY `code` (`code`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=402 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of shares
-- ----------------------------
INSERT INTO `shares` VALUES ('302', '002340', '格林美', '1');
INSERT INTO `shares` VALUES ('303', '300059', '东方财富', '1');
INSERT INTO `shares` VALUES ('304', '600519', '贵州茅台', '1');
INSERT INTO `shares` VALUES ('305', '600104', '上汽集团', '1');
INSERT INTO `shares` VALUES ('306', '601012', '隆基股份', '1');
INSERT INTO `shares` VALUES ('307', '002466', '天齐锂业', '1');
INSERT INTO `shares` VALUES ('308', '600585', '海螺水泥', '1');
INSERT INTO `shares` VALUES ('309', '601727', '上海电气', '1');
INSERT INTO `shares` VALUES ('310', '000977', '浪潮信息', '1');
INSERT INTO `shares` VALUES ('311', '300999', '金龙鱼', '1');
INSERT INTO `shares` VALUES ('312', '000725', '京东方Ａ', '1');
INSERT INTO `shares` VALUES ('313', '000591', '太阳能', '1');
INSERT INTO `shares` VALUES ('314', '002594', '比亚迪', '1');
INSERT INTO `shares` VALUES ('315', '601908', '京运通', '1');
INSERT INTO `shares` VALUES ('316', '600143', '金发科技', '1');
INSERT INTO `shares` VALUES ('317', '300750', '宁德时代', '1');
INSERT INTO `shares` VALUES ('318', '002475', '立讯精密', '1');
INSERT INTO `shares` VALUES ('319', '000767', '晋控电力', '1');
INSERT INTO `shares` VALUES ('320', '000938', '紫光股份', '1');
INSERT INTO `shares` VALUES ('321', '600655', '豫园股份', '1');
INSERT INTO `shares` VALUES ('322', '600887', '伊利股份', '1');
INSERT INTO `shares` VALUES ('323', '600031', '三一重工', '1');
INSERT INTO `shares` VALUES ('324', '000625', '长安汽车', '1');
INSERT INTO `shares` VALUES ('325', '600893', '航发动力', '1');
INSERT INTO `shares` VALUES ('326', '600362', '江西铜业', '1');
INSERT INTO `shares` VALUES ('327', '600703', '三安光电', '1');
INSERT INTO `shares` VALUES ('328', '002429', '兆驰股份', '1');
INSERT INTO `shares` VALUES ('329', '603993', '洛阳钼业', '1');
INSERT INTO `shares` VALUES ('330', '601360', '三六零', '1');
INSERT INTO `shares` VALUES ('331', '002007', '华兰生物', '1');
INSERT INTO `shares` VALUES ('332', '000063', '中兴通讯', '1');
INSERT INTO `shares` VALUES ('333', '002555', '三七互娱', '1');
INSERT INTO `shares` VALUES ('334', '002129', '中环股份', '1');
INSERT INTO `shares` VALUES ('335', '300459', '金科文化', '1');
INSERT INTO `shares` VALUES ('336', '000858', '五 粮 液', '1');
INSERT INTO `shares` VALUES ('337', '600438', '通威股份', '1');
INSERT INTO `shares` VALUES ('338', '000333', '美的集团', '1');
INSERT INTO `shares` VALUES ('339', '601919', '中远海控', '1');
INSERT INTO `shares` VALUES ('340', '002415', '海康威视', '1');
INSERT INTO `shares` VALUES ('341', '601318', '中国平安', '1');
INSERT INTO `shares` VALUES ('342', '601899', '紫金矿业', '1');
INSERT INTO `shares` VALUES ('343', '002714', '牧原股份', '1');
INSERT INTO `shares` VALUES ('344', '002177', '御银股份', '1');
INSERT INTO `shares` VALUES ('345', '600059', '古越龙山', '1');
INSERT INTO `shares` VALUES ('346', '600276', '恒瑞医药', '1');
INSERT INTO `shares` VALUES ('347', '600522', '中天科技', '1');
INSERT INTO `shares` VALUES ('348', '002460', '赣锋锂业', '1');
INSERT INTO `shares` VALUES ('349', '000157', '中联重科', '1');
INSERT INTO `shares` VALUES ('350', '600559', '老白干酒', '1');
INSERT INTO `shares` VALUES ('351', '600309', '万华化学', '1');
INSERT INTO `shares` VALUES ('352', '002497', '雅化集团', '1');
INSERT INTO `shares` VALUES ('353', '002241', '歌尔股份', '1');
INSERT INTO `shares` VALUES ('354', '600110', '诺德股份', '1');
INSERT INTO `shares` VALUES ('355', '600189', '泉阳泉', '1');
INSERT INTO `shares` VALUES ('356', '300038', '数知科技', '1');
INSERT INTO `shares` VALUES ('357', '601311', '骆驼股份', '1');
INSERT INTO `shares` VALUES ('358', '601888', '中国中免', '1');
INSERT INTO `shares` VALUES ('359', '600036', '招商银行', '1');
INSERT INTO `shares` VALUES ('360', '600776', '东方通信', '1');
INSERT INTO `shares` VALUES ('361', '002603', '以岭药业', '1');
INSERT INTO `shares` VALUES ('362', '000570', '苏常柴Ａ', '1');
INSERT INTO `shares` VALUES ('363', '300122', '智飞生物', '1');
INSERT INTO `shares` VALUES ('364', '002617', '露笑科技', '1');
INSERT INTO `shares` VALUES ('365', '601633', '长城汽车', '1');
INSERT INTO `shares` VALUES ('366', '300274', '阳光电源', '1');
INSERT INTO `shares` VALUES ('367', '002342', '巨力索具', '1');
INSERT INTO `shares` VALUES ('368', '600030', '中信证券', '1');
INSERT INTO `shares` VALUES ('369', '300015', '爱尔眼科', '1');
INSERT INTO `shares` VALUES ('370', '300418', '昆仑万维', '1');
INSERT INTO `shares` VALUES ('371', '000651', '格力电器', '1');
INSERT INTO `shares` VALUES ('372', '600161', '天坛生物', '1');
INSERT INTO `shares` VALUES ('373', '002017', '东信和平', '1');
INSERT INTO `shares` VALUES ('374', '600677', '*ST航通', '1');
INSERT INTO `shares` VALUES ('375', '603195', '公牛集团', '1');
INSERT INTO `shares` VALUES ('376', '002230', '科大讯飞', '1');
INSERT INTO `shares` VALUES ('377', '002008', '大族激光', '1');
INSERT INTO `shares` VALUES ('378', '688981', '中芯国际-U', '1');
INSERT INTO `shares` VALUES ('379', '000538', '云南白药', '1');
INSERT INTO `shares` VALUES ('380', '000002', '万  科Ａ', '1');
INSERT INTO `shares` VALUES ('381', '600460', '士兰微', '1');
INSERT INTO `shares` VALUES ('382', '600844', '丹化科技', '1');
INSERT INTO `shares` VALUES ('383', '603019', '中科曙光', '1');
INSERT INTO `shares` VALUES ('384', '600711', '盛屯矿业', '1');
INSERT INTO `shares` VALUES ('385', '002371', '北方华创', '1');
INSERT INTO `shares` VALUES ('386', '300894', '火星人', '1');
INSERT INTO `shares` VALUES ('387', '002382', '蓝帆医疗', '1');
INSERT INTO `shares` VALUES ('388', '002709', '天赐材料', '1');
INSERT INTO `shares` VALUES ('389', '600690', '海尔智家', '1');
INSERT INTO `shares` VALUES ('390', '000100', 'TCL科技', '1');
INSERT INTO `shares` VALUES ('391', '603799', '华友钴业', '1');
INSERT INTO `shares` VALUES ('392', '603087', '甘李药业', '1');
INSERT INTO `shares` VALUES ('393', '002625', '光启技术', '1');
INSERT INTO `shares` VALUES ('394', '002580', '圣阳股份', '1');
INSERT INTO `shares` VALUES ('395', '002197', '证通电子', '1');
INSERT INTO `shares` VALUES ('396', '002585', '双星新材', '1');
INSERT INTO `shares` VALUES ('397', '002385', '大北农', '1');
INSERT INTO `shares` VALUES ('398', '002624', '完美世界', '1');
INSERT INTO `shares` VALUES ('399', '600660', '福耀玻璃', '1');
INSERT INTO `shares` VALUES ('400', '600760', '中航沈飞', '1');
INSERT INTO `shares` VALUES ('401', '603259', '药明康德', '1');

-- ----------------------------
-- Table structure for sharesHotTop100
-- ----------------------------
DROP TABLE IF EXISTS `sharesHotTop100`;
CREATE TABLE `sharesHotTop100` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `code` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '股票代码',
  `price` varchar(10) DEFAULT NULL COMMENT '股票价格',
  `up_or_down` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '涨跌幅',
  `hot_ranking` tinyint unsigned DEFAULT NULL COMMENT '人气排名 最大100',
  `hot` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT 'hot说明',
  `date` char(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '日期格式2020-10-10',
  PRIMARY KEY (`id`),
  UNIQUE KEY `code_date` (`code`,`date`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=401 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of sharesHotTop100
-- ----------------------------
INSERT INTO `sharesHotTop100` VALUES ('101', '002340', '9.15', '9.98%', '1', '', '2021-01-08');
INSERT INTO `sharesHotTop100` VALUES ('102', '300059', '33.90', '-2.31%', '2', '', '2021-01-08');
INSERT INTO `sharesHotTop100` VALUES ('103', '600519', '2090.00', '-2.34%', '3', '#茅台和五粮液创历史新高#', '2021-01-08');
INSERT INTO `sharesHotTop100` VALUES ('104', '600104', '25.55', '9.99%', '4', '', '2021-01-08');
INSERT INTO `sharesHotTop100` VALUES ('105', '601012', '110.40', '-2.77%', '5', '', '2021-01-08');
INSERT INTO `sharesHotTop100` VALUES ('106', '002466', '54.34', '10.00%', '6', '#天齐锂业控股股东拟减持股份#', '2021-01-08');
INSERT INTO `sharesHotTop100` VALUES ('107', '600585', '56.45', '2.77%', '7', '', '2021-01-08');
INSERT INTO `sharesHotTop100` VALUES ('108', '601727', '6.08', '9.95%', '8', '', '2021-01-08');
INSERT INTO `sharesHotTop100` VALUES ('109', '000977', '29.21', '10.02%', '9', '', '2021-01-08');
INSERT INTO `sharesHotTop100` VALUES ('110', '300999', '145.00', '4.22%', '10', '', '2021-01-08');
INSERT INTO `sharesHotTop100` VALUES ('111', '000725', '6.43', '4.21%', '11', '', '2021-01-08');
INSERT INTO `sharesHotTop100` VALUES ('112', '000591', '7.51', '-4.57%', '12', '', '2021-01-08');
INSERT INTO `sharesHotTop100` VALUES ('113', '002594', '227.51', '1.10%', '13', '#比亚迪半导体筹划分拆上市#', '2021-01-08');
INSERT INTO `sharesHotTop100` VALUES ('114', '601908', '14.51', '10.01%', '14', '', '2021-01-08');
INSERT INTO `sharesHotTop100` VALUES ('115', '600143', '20.14', '7.64%', '15', '', '2021-01-08');
INSERT INTO `sharesHotTop100` VALUES ('116', '300750', '404.50', '-2.11%', '16', '#宁德时代总市值超9000亿元#', '2021-01-08');
INSERT INTO `sharesHotTop100` VALUES ('117', '002475', '60.01', '2.58%', '17', '', '2021-01-08');
INSERT INTO `sharesHotTop100` VALUES ('118', '000767', '4.73', '10.00%', '18', '', '2021-01-08');
INSERT INTO `sharesHotTop100` VALUES ('119', '000938', '22.24', '9.99%', '19', '', '2021-01-08');
INSERT INTO `sharesHotTop100` VALUES ('120', '600655', '14.32', '9.98%', '20', '', '2021-01-08');
INSERT INTO `sharesHotTop100` VALUES ('121', '600887', '49.27', '-4.68%', '21', '#伊利股份市值突破3000亿#', '2021-01-08');
INSERT INTO `sharesHotTop100` VALUES ('122', '600031', '40.37', '-0.05%', '22', '', '2021-01-08');
INSERT INTO `sharesHotTop100` VALUES ('123', '000625', '23.43', '3.26%', '23', '', '2021-01-08');
INSERT INTO `sharesHotTop100` VALUES ('124', '600893', '74.22', '-1.49%', '24', '', '2021-01-08');
INSERT INTO `sharesHotTop100` VALUES ('125', '600362', '24.84', '8.90%', '25', '', '2021-01-08');
INSERT INTO `sharesHotTop100` VALUES ('126', '600703', '31.68', '2.46%', '26', '', '2021-01-08');
INSERT INTO `sharesHotTop100` VALUES ('127', '002429', '6.53', '9.93%', '27', '', '2021-01-08');
INSERT INTO `sharesHotTop100` VALUES ('128', '603993', '7.40', '0.54%', '28', '', '2021-01-08');
INSERT INTO `sharesHotTop100` VALUES ('129', '601360', '17.51', '9.92%', '29', '', '2021-01-08');
INSERT INTO `sharesHotTop100` VALUES ('130', '002007', '50.39', '6.15%', '30', '', '2021-01-08');
INSERT INTO `sharesHotTop100` VALUES ('131', '000063', '33.90', '3.76%', '31', '', '2021-01-08');
INSERT INTO `sharesHotTop100` VALUES ('132', '002555', '33.86', '7.53%', '32', '', '2021-01-08');
INSERT INTO `sharesHotTop100` VALUES ('133', '002129', '30.31', '4.05%', '33', '', '2021-01-08');
INSERT INTO `sharesHotTop100` VALUES ('134', '300459', '3.42', '20.00%', '34', '', '2021-01-08');
INSERT INTO `sharesHotTop100` VALUES ('135', '000858', '317.00', '-3.94%', '35', '', '2021-01-08');
INSERT INTO `sharesHotTop100` VALUES ('136', '600438', '42.10', '-4.45%', '36', '', '2021-01-08');
INSERT INTO `sharesHotTop100` VALUES ('137', '000333', '103.01', '-1.73%', '37', '', '2021-01-08');
INSERT INTO `sharesHotTop100` VALUES ('138', '601919', '15.29', '6.85%', '38', '', '2021-01-08');
INSERT INTO `sharesHotTop100` VALUES ('139', '002415', '57.34', '-1.63%', '39', '', '2021-01-08');
INSERT INTO `sharesHotTop100` VALUES ('140', '601318', '86.10', '-0.19%', '40', '', '2021-01-08');
INSERT INTO `sharesHotTop100` VALUES ('141', '601899', '11.35', '1.52%', '41', '', '2021-01-08');
INSERT INTO `sharesHotTop100` VALUES ('142', '002714', '96.68', '-1.22%', '42', '', '2021-01-08');
INSERT INTO `sharesHotTop100` VALUES ('143', '002177', '5.63', '9.96%', '43', '', '2021-01-08');
INSERT INTO `sharesHotTop100` VALUES ('144', '600059', '18.01', '10.02%', '44', '', '2021-01-08');
INSERT INTO `sharesHotTop100` VALUES ('145', '600276', '113.22', '-1.55%', '45', '', '2021-01-08');
INSERT INTO `sharesHotTop100` VALUES ('146', '600522', '11.30', '6.00%', '46', '', '2021-01-08');
INSERT INTO `sharesHotTop100` VALUES ('147', '002460', '123.67', '-1.85%', '47', '', '2021-01-08');
INSERT INTO `sharesHotTop100` VALUES ('148', '000157', '11.86', '2.95%', '48', '', '2021-01-08');
INSERT INTO `sharesHotTop100` VALUES ('149', '600559', '35.16', '5.27%', '49', '', '2021-01-08');
INSERT INTO `sharesHotTop100` VALUES ('150', '600309', '109.00', '1.88%', '50', '', '2021-01-08');
INSERT INTO `sharesHotTop100` VALUES ('151', '002497', '28.44', '-4.82%', '51', '', '2021-01-08');
INSERT INTO `sharesHotTop100` VALUES ('152', '002241', '39.24', '0.62%', '52', '', '2021-01-08');
INSERT INTO `sharesHotTop100` VALUES ('153', '600110', '11.09', '10.02%', '53', '', '2021-01-08');
INSERT INTO `sharesHotTop100` VALUES ('154', '600189', '15.96', '9.99%', '54', '', '2021-01-08');
INSERT INTO `sharesHotTop100` VALUES ('155', '300038', '4.00', '20.12%', '55', '', '2021-01-08');
INSERT INTO `sharesHotTop100` VALUES ('156', '601311', '11.06', '7.48%', '56', '', '2021-01-08');
INSERT INTO `sharesHotTop100` VALUES ('157', '601888', '291.00', '-6.43%', '57', '', '2021-01-08');
INSERT INTO `sharesHotTop100` VALUES ('158', '600036', '46.60', '1.53%', '58', '', '2021-01-08');
INSERT INTO `sharesHotTop100` VALUES ('159', '600776', '12.06', '10.04%', '59', '', '2021-01-08');
INSERT INTO `sharesHotTop100` VALUES ('160', '002603', '30.30', '6.09%', '60', '', '2021-01-08');
INSERT INTO `sharesHotTop100` VALUES ('161', '000570', '6.48', '10.02%', '61', '', '2021-01-08');
INSERT INTO `sharesHotTop100` VALUES ('162', '300122', '151.84', '1.47%', '62', '', '2021-01-08');
INSERT INTO `sharesHotTop100` VALUES ('163', '002617', '9.46', '3.73%', '63', '', '2021-01-08');
INSERT INTO `sharesHotTop100` VALUES ('164', '601633', '42.50', '2.71%', '64', '', '2021-01-08');
INSERT INTO `sharesHotTop100` VALUES ('165', '300274', '85.23', '-4.24%', '65', '', '2021-01-08');
INSERT INTO `sharesHotTop100` VALUES ('166', '002342', '5.87', '-4.55%', '66', '', '2021-01-08');
INSERT INTO `sharesHotTop100` VALUES ('167', '600030', '30.06', '1.04%', '67', '', '2021-01-08');
INSERT INTO `sharesHotTop100` VALUES ('168', '300015', '75.93', '-1.90%', '68', '', '2021-01-08');
INSERT INTO `sharesHotTop100` VALUES ('169', '300418', '21.17', '11.72%', '69', '', '2021-01-08');
INSERT INTO `sharesHotTop100` VALUES ('170', '000651', '64.70', '0.00%', '70', '', '2021-01-08');
INSERT INTO `sharesHotTop100` VALUES ('171', '600161', '44.99', '10.00%', '71', '', '2021-01-08');
INSERT INTO `sharesHotTop100` VALUES ('172', '002017', '9.52', '10.06%', '72', '', '2021-01-08');
INSERT INTO `sharesHotTop100` VALUES ('173', '600677', '--', '--', '73', '', '2021-01-08');
INSERT INTO `sharesHotTop100` VALUES ('174', '603195', '242.65', '7.84%', '74', '', '2021-01-08');
INSERT INTO `sharesHotTop100` VALUES ('175', '002230', '43.05', '0.70%', '75', '', '2021-01-08');
INSERT INTO `sharesHotTop100` VALUES ('176', '002008', '47.40', '0.85%', '76', '', '2021-01-08');
INSERT INTO `sharesHotTop100` VALUES ('177', '688981', '61.59', '3.98%', '77', '', '2021-01-08');
INSERT INTO `sharesHotTop100` VALUES ('178', '000538', '140.97', '-2.70%', '78', '', '2021-01-08');
INSERT INTO `sharesHotTop100` VALUES ('179', '000002', '29.34', '1.91%', '79', '', '2021-01-08');
INSERT INTO `sharesHotTop100` VALUES ('180', '600460', '29.14', '0.21%', '80', '', '2021-01-08');
INSERT INTO `sharesHotTop100` VALUES ('181', '600844', '3.85', '10.00%', '81', '', '2021-01-08');
INSERT INTO `sharesHotTop100` VALUES ('182', '603019', '35.90', '5.81%', '82', '', '2021-01-08');
INSERT INTO `sharesHotTop100` VALUES ('183', '600711', '9.46', '-2.17%', '83', '', '2021-01-08');
INSERT INTO `sharesHotTop100` VALUES ('184', '002371', '187.25', '-1.73%', '84', '', '2021-01-08');
INSERT INTO `sharesHotTop100` VALUES ('185', '300894', '58.13', '16.05%', '85', '', '2021-01-08');
INSERT INTO `sharesHotTop100` VALUES ('186', '002382', '22.81', '6.74%', '86', '', '2021-01-08');
INSERT INTO `sharesHotTop100` VALUES ('187', '002709', '117.80', '2.12%', '87', '', '2021-01-08');
INSERT INTO `sharesHotTop100` VALUES ('188', '600690', '33.00', '0.98%', '88', '', '2021-01-08');
INSERT INTO `sharesHotTop100` VALUES ('189', '000100', '7.47', '1.63%', '89', '', '2021-01-08');
INSERT INTO `sharesHotTop100` VALUES ('190', '603799', '94.90', '-0.73%', '90', '', '2021-01-08');
INSERT INTO `sharesHotTop100` VALUES ('191', '603087', '168.00', '6.34%', '91', '', '2021-01-08');
INSERT INTO `sharesHotTop100` VALUES ('192', '002625', '27.38', '0.66%', '92', '', '2021-01-08');
INSERT INTO `sharesHotTop100` VALUES ('193', '002580', '7.41', '9.94%', '93', '', '2021-01-08');
INSERT INTO `sharesHotTop100` VALUES ('194', '002197', '8.50', '9.96%', '94', '', '2021-01-08');
INSERT INTO `sharesHotTop100` VALUES ('195', '002585', '10.88', '10.01%', '95', '', '2021-01-08');
INSERT INTO `sharesHotTop100` VALUES ('196', '002385', '10.90', '-3.37%', '96', '', '2021-01-08');
INSERT INTO `sharesHotTop100` VALUES ('197', '002624', '30.43', '4.86%', '97', '', '2021-01-08');
INSERT INTO `sharesHotTop100` VALUES ('198', '600660', '51.48', '1.04%', '98', '', '2021-01-08');
INSERT INTO `sharesHotTop100` VALUES ('199', '600760', '95.45', '-1.09%', '99', '', '2021-01-08');
INSERT INTO `sharesHotTop100` VALUES ('200', '603259', '146.21', '0.18%', '100', '', '2021-01-08');
