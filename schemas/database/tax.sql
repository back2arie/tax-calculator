/*
 Navicat Premium Data Transfer

 Source Server         : Tax Calculator - Local
 Source Server Type    : PostgreSQL
 Source Server Version : 90606
 Source Host           : localhost
 Source Database       : tax
 Source Schema         : public

 Target Server Type    : PostgreSQL
 Target Server Version : 90606
 File Encoding         : utf-8

 Date: 08/24/2019 13:46:09 PM
*/

-- ----------------------------
--  Table structure for tax
-- ----------------------------
DROP TABLE IF EXISTS "public"."tax";
CREATE TABLE "public"."tax" (
	"name" varchar(255) COLLATE "default",
	"tax_code" int2,
	"price" int8
)
WITH (OIDS=FALSE);
ALTER TABLE "public"."tax" OWNER TO "tax";

