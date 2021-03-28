# sameersbn/redmineイメージの利用法

## 利用方法
docker-compose up -d

## 初期アカウント
userid:admin
password:admin

## 手動バックアップコマンド
docker exec -it sameersbnredmine_redmine_1 redmine-backup-create

- バックアップファイルはタイムスタンプが先頭につく。
- 現在のタイムスタンプの算出コマンド
date "+%s"

- バックアップのタイムスタンプから日時を算出するコマンド
date --date @タイムスタンプ "+%m/%d/%Y %H:%M"

## 手動リストアコマンド(Windowsだとエラー)
docker stop sameersbnredmine_redmine_1 && docker rm sameersbnredmine_redmine_1
docker run --name sameersbnredmine_redmine_1 -it --rm sameersbn/redmine:4.1.1-9 app:backup:restore BACKUP = バックアップファイル

## OSアップデート
- 下記コマンドを実行してコンテナのOSをLTS版にアップデートしておく。
apt update
apt upgrade
apt install update-manager
apt dist-upgrade
do-release-upgrade

以上
