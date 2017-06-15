# v1
-------
* 時間：2017.02.08-2017.02.31
* 前端
	* 網站模板，簡單套用bootstrap框架
	* 添加文章動態顯示
		＊ 說明：ajax讀json檔 + scroll事件綁定
	* 添加ga追蹤碼
* 後端
	* 使用flask，做為web框架
	* 添加文章上傳模塊
		＊ 說明：json文檔作為儲存
		＊ 流程：上傳.md檔 → 格式轉換成.html檔並儲存
* 建置
	* 2017.02.26 建置於pythonanywhere.com，網址為http://vivian.pythonanywhere.com/

＊學習點
	* 理解 bootstrap ＆ flask & javascript 基本 




# v2
-------
* 時間：2017.03.01-2017.04.15
* 前端
	* 轉換rwd
	* 添加輪播carousel
	* 添加頁尾

* 學習點
	* less
	* jquery & bootstrap.js:carousel.js




# v3
--------
* 時間：2017.04.16-2017.05.12

* 前端 
	＊ 修改文章動態生成方式：javascript → jquery，依據bootstrap插件形式撰寫
	＊ 模板化：猜你喜歡模板：_article.like.html
	＊ 添加：文章上傳模式選擇頁板

* 後端
	＊ 儲存方式轉移：json文檔 → mysql數據庫
	＊ 添加登入模塊
	＊ 添加簡轉繁模塊
	＊ 添加文章上傳：crawler模式
	＊ 優化crawler.py
	＊ 添加文章上傳：markdown模式
	＊ 添加預覽模式
	＊ 添加開源文字編譯器模式-CKeditor：https://segmentfault.com/a/1190000002436865
	＊ 添加三種文章修改模板


* 建置
	* 2017.04.25 遷移至heroku.com，網址為http://bigdatainsight.herokuapp.com/
	* 將程式遷入版本管理工具git



# v4
--------
* 時間：2017.06.01
* 前端
	* 頁面優化
	* 修改ajax顯示
	* 後台：上傳動態顯示
	* seo優化 & 運用ga
	* 串接社群api(facebook)

* 後端
	* 文章整理器
	* 多文件上傳實現
	* 添加權限功能
	* 文章自動生成
		＊ http://chuansong.me/account/SparkDaily?start=336
		＊ http://www.36dsj.com/archives/17187
	
＊bug紀錄：
	＊ crawler路徑問題優化
	＊ 登入需限制只使用https
	＊ https請求，ajax出現問題
	＊ jquery報錯問題修復


* 建置：
	＊ 遷移至AWS



# v5
--------
* 修改紀錄：
	* 2017.06.01
		*	修改文章顯示方式，移除../static/custom.js，修改成動態顯示

	* 2017.06.02
		* 修改postgres表結構
		* 完成外部添加文章

	* 2017.06.03
		* 首頁，文章頁,css優化
		* 文章鏈結爬取更新演算法

	* 2017.06.04
		* 文章修改模式更新

	* 2017.06.12
		* 文章後台顯示

	* 2017.06.13
		* 分頁顯示

	* 2017.06.14
		＊滑動顯示
		* 上傳特效

	* 2017.06.15
		* 權限功能

	* 2017.06.16-2017.06.18
		* facebook 社群api
		* 基本seo優化

		* spark技術日報爬蟲撰寫
		* 穿插上傳演算法設計
		* markdown特效修復