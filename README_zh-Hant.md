# COPIKANA
[English version at README_zh-Hant.md](https://github.com/samhui96/COPIKANA/main/README.md)

COPIKAN建於[pykakasi](https://github.com/miurahr/pykakasi)之上，爲輕型日本漢字至平假名轉換器，並可供離線使用。
使用時，先反白選取漢字，再`按右鍵複製‵或按`Ctrl+C`皆可，轉換之結果將自動顯示。選取方法，**以雙按文字反白者爲佳**，以便包括完整詞語，因爲漢字單獨與否，會令日語讀音迥異。


If you you are happy to use, why not consider adding [the final touch](https://ko-fi.com/s/b8e4f06daa)?

> This repo was inited much later after COPIKANA 1.0 is created, as I found Git/Github is harder than Python to learn 😅
> 
> If you try to pack COPIKANA into an EXE file, Microsoft Defender may think it is malware 😕 Exempt the folder where you are going to store the executable helps prevent the inconvenience. I'm working on the issue and hopefully it can be solved.

- **v1.0.0**: for those who are already familiar with hiragana.
  - Slider: adjust the font size

- **v1.1.0**: for those who need more hints other than hiragana. Two modes available: the hiragana mode, and the romaji mode which **does not support** the special pronunciations of ‘は’, ‘を’ and extended and rare kana.
  - Very short slider: switch between 'hiragana mode' and 'romaji mode'
  - Long slider: adjust the font size

- **COPIKANA_proj**: all the experiments are done here. Recently let you directly paste the convertion result by `right-click & paste` or  `Ctrl+V`, but funny things happen when you switch between the two modes.
  - Very short slider: switch between 'hiragana mode' and 'romaji mode'
  - Long slider: adjust the font size
  - Button with the character '文': change font
