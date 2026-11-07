# CoffeeITmac

Сайт-статья об истории операционных систем Apple: **«Версии macOS по годам — от System 1.0 (1984) до macOS Sequoia (2024)»**.

Google Drive: **CoffeeITmac — рабочее пространство**
https://drive.google.com/drive/folders/1U1XwyYbCm-x1sSj522GXBRqCiG8Byl7b

## Файлы

| Путь | Что это |
|------|---------|
| `index.html` | Готовый сайт — открывается в браузере, 26 разделов, 26 галерей со слайд-шоу, лайтбокс по клику на скриншот, оглавление, кнопка «наверх». Автономный: без сборки, без CDN и внешних зависимостей. |
| `macos-history.html` | Исходная версия статьи (тот же текст без доработок сайта). |
| `shots/` | 78 изображений в папке `shots/` — скриншоты и обои каждой версии ОС (puma-1.jpg, sequoia-3.png и т. д.). |
| `tools/build-shots.sh` | Скрипт сборки `shots/` из папки `image-search/` (ImageMagick: ресайз до 1400 px, конвертация в нужный формат). |
| `tools/build-site.py` | Скрипт сборки `index.html` из `macos-history.html` (мета-теги, favicon, лайтбокс, кнопка «наверх», подписи источников). |

## Как открыть локально

```bash
python3 -m http.server 8000
# затем http://localhost:8000
```

Просто открыть `index.html` двойным кликом тоже работает — все пути относительные.

## Как пересобрать

```bash
bash tools/build-shots.sh    # пересобрать картинки из image-search/
python3 tools/build-site.py  # пересобрать index.html из macos-history.html
```

Папка `image-search/` (сырые загрузки, ~18 МБ) в репозиторий не попадает — см. `.gitignore`.

## Источники изображений

Wikimedia Commons, 512 Pixels, OSXDaily, Ars Technica, Apple Newsroom, VersionMuseum, PCMag, iMore, Cult of Mac, blog.alexseifert.com — материалы используются в учебных целях. Текст статьи — [Yablyk.com](https://yablyk.com), Дмитрий Михневич, 11 августа 2024.
