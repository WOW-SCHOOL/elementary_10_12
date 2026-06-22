Как пользоваться мини‑сайтом-плеером
=====================================

Этот архив подготовлен для GitHub Pages и вставки в Miro/Холст.

Что уже исправлено
------------------
1) `playlist.json` автоматически пересобран по реальным файлам из папки `tracks/`.
2) В плейлист добавлено треков: 54.
3) Добавлен `generate_playlist.py`, чтобы в будущем не прописывать треки вручную.
4) Добавлен `preview.jpg` для более корректного превью.
5) `index.html` и `style.css` настроены под удобный книжный формат iframe.

Как обновлять playlist.json
---------------------------
Если добавили или удалили аудио в папке `tracks/`, запустите:

python generate_playlist.py

После этого скрипт сам обновит `playlist.json`.

Как выложить на GitHub
----------------------
1) Распакуйте архив.
2) Откройте папку проекта в GitHub Desktop.
3) Проверьте, что файлы лежат в корне репозитория:
   - index.html
   - style.css
   - playlist.json
   - cover.jpg
   - preview.jpg
   - tracks/
4) Сделайте Commit.
5) Нажмите Push origin.
6) В Settings → Pages включите публикацию:
   - Source: Deploy from a branch
   - Branch: main
   - Folder: /root

iFrame для Miro/Холста
----------------------
<iframe
  src="https://wow-school.github.io/EF_elementary_2/"
  width="750"
  height="850"
  frameborder="0"
  scrolling="yes"
  allow="autoplay; fullscreen"
  allowfullscreen
  style="width:750px; height:850px; max-width:100%; border:0; border-radius:18px; overflow:hidden;">
</iframe>

Важно
-----
Если репозиторий будет называться иначе, поменяйте часть ссылки после `github.io/`.
Например:
https://wow-school.github.io/НАЗВАНИЕ_РЕПОЗИТОРИЯ/
