# bitnami/redmineの標準コンテナの利用

## 事前準備

dockerとdocker-composeが利用可能であること。(Windows機の場合、DockerDesktopインストール済みであればよい）

## 元ファイル

https://raw.githubusercontent.com/bitnami/bitnami-docker-redmine/master/docker-compose.yml

## コンテナ起動コマンド
docker-compose up -d

## コンテナ終了コマンド
docker-compose down

## データ削除コマンド（ボリューム削除）
### MySQLのコンテナのデータ削除（登録データの削除等）
docker volume rm virtuale_mariadb_data

### Redmineのコンテナのデータ削除（プラグイン削除等）
docker volume rm virtuale_redmine_data

## 注意点
docker-compose.ymlを格納するフォルダおよび実行時のカレントディレクトリのフルパスには日本語が含まれていないこと。

## デフォルト設定
Redmine管理者ユーザ名：user
Redmine管理者パスワード：bitnami1
Redmine管理者メールアドレス：user@example.com
Redmine言語：英語
DBの管理者ユーザ名；bn_redmine
DBの管理者パスワード：
DB名：bitnami_redmine
MYSQLサーバのホスト名：mariadb
PostgreSQLサーバのホスト名：なし
DBサーバのポート番号：3306

以上