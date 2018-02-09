# 1. 專案說明
* 描述：此專案，用於學習Python Flask框架
* 網址：
	* 前台：http://bigdatainsight.herokuapp.com/
	* 後台：http://bigdatainsight.herokuapp.com/back/login
* 現狀
	* 後台：上傳方式，只完善自動爬取上傳文章，36dsj部份


# 2. 版本紀錄

#### version 1
-------
* 時間：2017.02.08-2017.02.31
* 前端
	* 網站模板，簡單套用bootstrap框架
	* 添加文章動態顯示
		* 說明：ajax讀json檔 + scroll事件綁定
	* 添加ga追蹤碼
* 後端
	* 使用flask，做為web框架
	* 添加文章上傳模塊
		* 說明：json文檔作為儲存
		* 流程：上傳.md檔 → 格式轉換成.html檔並儲存
* 建置
	* 2017.02.26 建置於pythonanywhere.com，網址為http://vivian.pythonanywhere.com/

* 學習點
	* 理解 bootstrap ＆ flask & javascript 基本 



#### version 2
-------
* 時間：2017.03.01-2017.04.15
* 前端
	* 轉換rwd
	* 添加輪播carousel
	* 添加頁尾

* 學習點
	* less
	* jquery & bootstrap.js:carousel.js




#### version 3
--------
* 時間：2017.04.16-2017.05.12

* 前端 
	* 修改文章動態生成方式：javascript → jquery，依據bootstrap插件形式撰寫
	* 模板化：猜你喜歡模板：_article.like.html
	* 添加：文章上傳模式選擇頁板

* 後端
	* 儲存方式轉移：json文檔 → mysql數據庫
	* 添加登入模塊
	* 添加簡轉繁模塊
	* 添加文章上傳：crawler模式
	* 添加文章上傳：markdown模式
	* 添加預覽模式
	* 添加開源文字編譯器模式-CKeditor：https://segmentfault.com/a/1190000002436865
	* 添加三種文章修改模板
	* 添加文章整理頁

* 建置
	* 2017.04.25 遷移至heroku.com，網址為http://bigdatainsight.herokuapp.com/
	* 將程式遷入版本管理工具git


* bug紀錄：
	* crawler路徑問題優化（已）
	* 登入需限制只使用https
	* https請求，ajax出現問題
	* jquery報錯問題修復（已）



#### version 4
--------
* 修改紀錄：
	* 2017.06.01
		* 修改文章顯示方式，移除../static/custom.js，修改成動態顯示

	* 2017.06.02
		* 修改postgres表結構

	* 2017.07.03
		* 修復bootstrap font
		* 添加more.js

	* 待更新項目	
		* facebook 社群api
		* 基本seo優化
		* spark技術日報爬蟲撰寫 http://chuansong.me/account/SparkDaily?start=336
		* 穿插上傳演算法設計
		* markdown特效修復
		* 添加多圖檔上傳 http://blog.csdn.net/deepwine/article/details/47277093
		* 添加服務器圖片庫查看