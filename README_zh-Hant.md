# COPIKANA
[English version at README_zh-Hant.md](https://github.com/samhui96/COPIKANA/main/README.md)

COPIKAN建於[pykakasi](https://github.com/miurahr/pykakasi)之上，爲輕型日本漢字至平假名轉換器，並可供離線使用。

使用時，先反白選取漢字，再`按右鍵複製‵或按`Ctrl+C`皆可，轉換之結果將隨即顯示。選取方法**以雙按文字反白者爲佳**，以便包括完整詞語，因爲漢字單獨與否，會令日語讀音迥異。由於漢字讀音於日語中千萬變化，本轉換器僅顯示最普通讀法，至於精確讀法，留待日後臻善。以下簡介各式版本，及其介面機關作用。

- **COPIKANA_1.0**：適用於熟讀五十音者，介面精簡，務求低調。
  - 滑桿：拖動滑子以調節文字大小。

- **COPIKANA_1.1**：適用於未熟讀五十音者，附加羅馬字模式，惟未能轉換「は」、「を」作助詞時以及特殊或罕見假名之讀音。
  - 超短滑桿：拖動滑子於「平假名模式」或「羅馬字模式」之間來回切換。
  - 長滑桿：拖動滑子以調節文字大小。
    
- **COPIKANA_proj**：實驗用，包含最多功能。最新功能可將轉換結果直接傳送至剪貼板，只消`按右鍵貼上‵或按`Ctrl+Ｖ`即可貼上，惟轉換結果無法於模式間變化。
  - 超短滑桿：拖動滑子於「平假名模式」或「羅馬字模式」之間來回切換。
  - 長滑桿：拖動滑子以調節文字大小。
  - 「文」字鍵：按下以變換字型

If you you are happy to use, why not consider adding [the final touch](https://ko-fi.com/s/b8e4f06daa)?

> This repo was inited much later after COPIKANA 1.0 is created, as I found Git/Github is harder than Python to learn 😅
> 
> If you try to pack COPIKANA into an EXE file, Microsoft Defender may think it is malware 😕 Exempt the folder where you are going to store the executable helps prevent the inconvenience. I'm working on the issue and hopefully it can be solved.

