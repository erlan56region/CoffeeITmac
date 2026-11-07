#!/usr/bin/env bash
# Собирает папку shots/ из скачанных изображений image-search/
set -euo pipefail
SRC=image-search
OUT=shots
mkdir -p "$OUT"

map=(
"system1-1.png|system-1-0-macintosh-finder-screenshot-1-1.jpg"
"system1-2.png|system-1-0-macintosh-finder-screenshot-1-2.png"
"system1-3.gif|system-1-0-macintosh-finder-screenshot-1-3.png"
"system6-1.jpg|system-6-0-8-macintosh-desktop-screensho-1.webp"
"system6-2.png|system-6-0-8-macintosh-desktop-screensho-2.webp"
"system6-3.jpg|system-6-0-8-macintosh-desktop-screensho-3.webp"
"system7-1.png|system-7-macintosh-desktop-screenshot-19-1.png"
"system7-2.png|system-7-macintosh-desktop-screenshot-19-2.png"
"system7-3.png|system-7-macintosh-desktop-screenshot-19-3.png"
"system8-1.png|mac-os-8-desktop-screenshot-1997-1.png"
"system8-2.png|mac-os-8-desktop-screenshot-1997-2.png"
"system8-3.jpg|mac-os-8-desktop-screenshot-1997-3.png"
"macos9-1.jpg|mac-os-9-desktop-screenshot-1.jpg"
"macos9-2.png|mac-os-9-desktop-screenshot-2.jpg"
"macos9-3.png|mac-os-9-desktop-screenshot-3.webp"
"cheetah-1.png|mac-os-x-10-0-cheetah-desktop-screenshot-1.png"
"cheetah-2.png|mac-os-x-10-0-cheetah-aqua-screenshot-2.jpg"
"cheetah-3.png|mac-os-x-10-0-cheetah-aqua-screenshot-3.jpg"
"puma-1.jpg|mac-os-x-10-1-puma-screenshot-1024x768-d-3.jpg"
"puma-2.jpg|mac-os-x-10-1-puma-screenshot-1024x768-d-1.jpg"
"puma-3.png|mac-os-x-10-1-puma-desktop-screenshot-3.png"
"jaguar-1.png|mac-os-x-10-2-jaguar-full-desktop-screen-2.jpg"
"jaguar-2.jpg|mac-os-x-10-2-jaguar-desktop-screenshot-2.png"
"jaguar-3.png|mac-os-x-10-2-jaguar-desktop-screenshot-3.jpg"
"panther-1.jpg|mac-os-x-10-3-panther-desktop-screenshot-1.jpg"
"panther-2.png|mac-os-x-panther-10-3-screenshot-1024x76-1.jpg"
"panther-3.jpg|mac-os-x-panther-10-3-screenshot-1024x76-2.jpg"
"tiger-1.jpg|mac-os-x-10-4-tiger-dashboard-desktop-sc-1.jpg"
"tiger-2.png|mac-os-x-10-4-tiger-dashboard-desktop-sc-2.jpg"
"tiger-3.png|mac-os-x-10-4-tiger-dashboard-desktop-sc-3.jpg"
"leopard-1.png|mac-os-x-10-5-leopard-desktop-screenshot-1.jpg"
"leopard-2.jpg|mac-os-x-10-5-leopard-desktop-screenshot-2.jpg"
"leopard-3.jpg|mac-os-x-10-5-leopard-desktop-screenshot-3.jpg"
"snowleopard-1.jpg|mac-os-x-snow-leopard-10-6-desktop-scree-1.jpg"
"snowleopard-2.jpg|mac-os-x-snow-leopard-10-6-desktop-scree-2.webp"
"snowleopard-3.jpg|mac-os-x-snow-leopard-10-6-desktop-scree-3.webp"
"lion-1.png|mac-os-x-lion-10-7-launchpad-desktop-scr-1.jpg"
"lion-2.jpg|mac-os-x-lion-10-7-launchpad-desktop-scr-2.jpg"
"lion-3.jpg|mac-os-x-lion-10-7-desktop-screenshot-sp-1.jpg"
"mountainlion-1.png|os-x-mountain-lion-10-8-desktop-screensh-1.png"
"mountainlion-2.png|os-x-mountain-lion-10-8-desktop-screensh-2.jpg"
"mountainlion-3.png|os-x-mountain-lion-10-8-desktop-screensh-3.jpg"
"mavericks-1.jpg|os-x-mavericks-10-9-default-wallpaper-de-1.jpg"
"mavericks-2.jpg|os-x-mavericks-10-9-default-wallpaper-de-2.jpg"
"mavericks-3.jpg|os-x-mavericks-10-9-default-wallpaper-de-3.jpg"
"yosemite-1.jpg|os-x-yosemite-10-10-default-wallpaper-de-2.jpg"
"yosemite-2.jpg|os-x-yosemite-10-10-default-wallpaper-de-3.jpg"
"yosemite-3.jpg|os-x-yosemite-10-10-default-wallpaper-de-1.jpg"
"elcapitan-1.png|os-x-el-capitan-10-11-desktop-screenshot-1.jpg"
"elcapitan-2.png|os-x-el-capitan-10-11-desktop-screenshot-2.jpg"
"elcapitan-3.png|os-x-el-capitan-10-11-desktop-screenshot-3.jpg"
"sierra-1.jpg|macos-sierra-10-12-default-wallpaper-des-2.jpg"
"sierra-2.jpg|macos-sierra-10-12-default-wallpaper-des-1.jpg"
"sierra-3.jpg|macos-sierra-10-12-default-wallpaper-des-3.jpg"
"highsierra-1.png|macos-high-sierra-10-13-default-wallpape-1.jpg"
"highsierra-2.jpg|macos-high-sierra-10-13-default-wallpape-2.jpg"
"highsierra-3.jpg|macos-high-sierra-10-13-default-wallpape-3.jpg"
"mojave-1.png|macos-mojave-desktop-screenshot-full-scr-3.jpg"
"mojave-2.jpg|macos-mojave-desktop-screenshot-full-scr-2.jpg"
"mojave-3.jpg|macos-mojave-desktop-screenshot-full-scr-4.jpg"
"catalina-1.png|macos-catalina-10-15-default-wallpaper-d-3.jpg"
"catalina-2.png|macos-catalina-10-15-default-wallpaper-d-1.jpg"
"catalina-3.jpg|macos-catalina-10-15-default-wallpaper-d-2.jpg"
"bigsur-1.png|macos-big-sur-11-default-wallpaper-deskt-1.jpg"
"bigsur-2.jpg|macos-big-sur-11-default-wallpaper-deskt-2.jpg"
"bigsur-3.jpg|macos-big-sur-11-default-wallpaper-deskt-3.jpg"
"monterey-1.png|macos-monterey-12-default-wallpaper-desk-1.jpg"
"monterey-2.png|macos-monterey-12-default-wallpaper-desk-2.png"
"monterey-3.jpg|macos-monterey-12-default-wallpaper-desk-3.jpg"
"ventura-1.png|macos-ventura-13-default-wallpaper-deskt-3.jpg"
"ventura-2.jpg|macos-ventura-13-default-wallpaper-deskt-2.jpg"
"ventura-3.jpg|macos-ventura-13-default-wallpaper-deskt-1.jpg"
"sonoma-1.png|macos-sonoma-14-default-wallpaper-deskto-1.gif[0]"
"sonoma-2.png|macos-sonoma-14-default-wallpaper-deskto-2.png"
"sonoma-3.png|macos-sonoma-14-default-wallpaper-deskto-3.png"
"sequoia-1.png|macos-sequoia-15-wallpaper-apple-intelli-1.png"
"sequoia-2.jpg|macos-sequoia-15-wallpaper-apple-intelli-2.png"
"sequoia-3.png|macos-sequoia-15-wallpaper-apple-intelli-3.png"
)

n=0
for pair in "${map[@]}"; do
  target="${pair%%|*}"
  source="${pair#*|}"
  out="$OUT/$target"
  case "$target" in
    *.jpg) convert "$SRC/$source" -auto-orient -resize '1400x1400>' -strip -quality 82 "$out" ;;
    *.png) convert "$SRC/$source" -auto-orient -resize '1400x1400>' -strip -colors 256 "$out" ;;
    *.gif) convert "$SRC/$source" -auto-orient -resize '1100x1100>' -strip -colors 256 "$out" ;;
  esac
  n=$((n+1))
done

echo "готово: $n файлов"
ls -1 "$OUT" | wc -l
du -sh "$OUT"
