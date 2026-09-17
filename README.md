# Телеграм бот для скачивания видео с тиктока
> [!NOTE]
> Бот полностью вайбкод.

При отправке ссылки на тикток данному боту в ответ он присылает видео.
Бота также можно добавить в групповой чат.

Иногда бот выдаёт ошибки:

### Ошибка №1
```
ERROR: [TikTok] 7683967723621141773: This post may not be comfortable for some audiences. Log in for access.
```

Она означает, что видео не было скачано из-за ограничений на этом видео. Для его скачивания необходима авторизация.


### Ошибка №2
```
[0;31mERROR: [0m [TikTok] 7680143784692256007: Unexpected response from webpage request; please report this issue on  https://github.com/yt-dlp/yt-dlp/issues?q= , filling out the appropriate issue template. Confirm you are on the latest version using  yt-dlp -U
```

Это ошибка на стороне библиотеки для скачивания (yt-dlp). С ней ждать только фикса от разрабов или иногда просто сама по себе проходит (с чем это связано, не понятно)

---

Бот поддерживает ссылки формата: https://www.tiktok.com/ или https://vm.tiktok.com/

```python
    # Ищет ссылки, начинающиеся с https://www.tiktok.com/ или https://vm.tiktok.com/
    pattern = r'(https?://(?:www\.|vm\.)?tiktok\.com/\S+)'
```
 Если нужны другие ссылки, то отправьте код в нейронку и попросите добавить ссылку вашего формата
