工能說明</br>
  利用linebot、webapi查詢職缺相關資訊
  使用者輸入的關鍵字，將資料庫的資料回傳。
  若資料庫未有相應關鍵字的資料，去求職網站爬取結果，將結果存至資料庫。
  使用者可以主動發送請求，使資料庫內的資料更新

LineBot畫面
  ![image](https://github.com/0988118277z/job-helper/assets/86332350/8047fe1f-dd82-4f98-b201-53cb3eae699b)

WebAPI畫面
  ![image](https://github.com/0988118277z/job-helper/assets/86332350/4354d83b-786b-444a-bba0-ea633d8580d1)

程式說明
  程式主要分成三部分
    1.Python Flask，來接收與回傳資料
    2.第一次查詢時去爬資料的程式
    3.更新資料時去爬資料的程式

  Python Flask，分成webapi與linebot api
    ![image](https://github.com/0988118277z/job-helper/assets/86332350/9868f775-585e-4138-8720-9f08977b14dc)
    Webapi  回傳json格式、Linebot 回傳文字格式
    ![image](https://github.com/0988118277z/job-helper/assets/86332350/3fe025cf-f6f7-4024-979d-0126129c49f3)





