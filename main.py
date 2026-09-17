from config import API_TOKEN
import telebot
import yt_dlp
import os
import re

bot = telebot.TeleBot(token=API_TOKEN)


DOWNLOAD_FOLDER = "downloads"
if not os.path.exists(DOWNLOAD_FOLDER):
    os.makedirs(DOWNLOAD_FOLDER)


# 3. НАСТРОЙКИ ДЛЯ yt-dlp
ydl_opts = {
    'outtmpl': os.path.join(DOWNLOAD_FOLDER, '%(title)s.%(ext)s'),  # Путь и имя файла
    'quiet': True,           # Не выводить лишнего в консоль
    'no_warnings': True,
    'format': 'best',        # Скачать лучшее качество
}

# 4. ФУНКЦИЯ ДЛЯ ПОИСКА ССЫЛКИ НА TIKTOK В ТЕКСТЕ
def extract_tiktok_url(text):
    # Ищет ссылки, начинающиеся с https://www.tiktok.com/ или https://vm.tiktok.com/
    pattern = r'(https?://(?:www\.|vm\.)?tiktok\.com/\S+)'
    match = re.search(pattern, text)
    return match.group(0) if match else None


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    # Проверяем, есть ли в сообщении ссылка на TikTok
    video_url = extract_tiktok_url(message.text)
    if not video_url:
        # Если ссылки нет, просто игнорируем сообщение
        return
    
    bot.reply_to(message, "🔄 Начинаю скачивать видео с TikTok...")
    
    try:
        # 7. СКАЧИВАЕМ ВИДЕО
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(video_url, download=True)
            video_filename = ydl.prepare_filename(info)

        # 8. ОТПРАВЛЯЕМ ВИДЕО В ЧАТ
        with open(video_filename, 'rb') as video_file:
            bot.send_video(
                message.chat.id,
                video_file,
                reply_to_message_id=message.message_id,
                caption=f"🎬 Видео с TikTok"
            )

        # 9. УДАЛЯЕМ ВРЕМЕННЫЙ ФАЙЛ
        os.remove(video_filename)

    except Exception as e:
        bot.reply_to(message, f"❌ Произошла ошибка при скачивании: {e}")

# 10. ЗАПУСКАЕМ БОТА
print("Бот запущен и готов скачивать видео с TikTok!")
bot.infinity_polling()
    
bot.infinity_polling()