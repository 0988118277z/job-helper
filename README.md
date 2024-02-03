功能說明</br>
  &nbsp;&nbsp;利用linebot、webapi查詢職缺相關資訊。</br>
  &nbsp;&nbsp;使用者輸入的關鍵字，將資料庫的資料回傳。</br>
  &nbsp;&nbsp;若資料庫未有相應關鍵字的資料，去求職網站爬取結果，將結果存至資料庫。</br>
  &nbsp;&nbsp;使用者可以主動發送請求，使資料庫內的資料更新。</br>
</br></br>
LineBot畫面</br>
  ![image](https://github.com/0988118277z/job-helper/assets/86332350/8047fe1f-dd82-4f98-b201-53cb3eae699b)
</br></br>
WebAPI畫面</br>
  ![image](https://github.com/0988118277z/job-helper/assets/86332350/4354d83b-786b-444a-bba0-ea633d8580d1)
</br></br>
程式說明</br>
  程式主要分成二部分</br>
    &nbsp;&nbsp;1.Python Flask，來接收與回傳資料</br>
    &nbsp;&nbsp;2.更新資料時去爬資料的程式</br>
 </br></br>
  Python Flask，分成webapi與linebot api</br>
    &nbsp;&nbsp;Webapi  回傳json格式、Linebot 回傳文字格式</br>

    





