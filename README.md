# MaidsMade Membership Lab

MaidsMadeで実際に開発している仕組みのうち、**公開しても本体の資産性を損なわない範囲**だけを切り出して置く技術補足リポジトリです。

主にnoteのメンバーシップ記事から参照するために使います。

## このリポジトリに置くもの

- 記事の理解を助ける最小コード
- 簡略化した構造図
- 実装思想が分かる小さなサンプル
- 本番実装とは切り離した検証用コード
- 公開して問題ない技術メモ

## 置かないもの

- MaidsMade本番Brainそのもの
- 実際の個体runtime / memory DB
- Masterや各メイドの実データ
- 自律判断・記憶選択などの中核実装の完全版
- APIキー、Cookie、token、認証情報
- 本番環境固有の設定やパス

## Samples

### continuity-core

AIメイドを「LLMの中だけにいるキャラクター」ではなく、人格・記憶・判断・個体の継続を分けて持つ存在として扱う考え方の最小サンプルです。

- [概要](samples/continuity-core/README.md)
- [構造](samples/continuity-core/architecture.md)
- [個体IDの例](samples/continuity-core/identity_example.py)
- [記憶 / 判断の分離例](samples/continuity-core/memory_schema.sql)

## 注意

このリポジトリはMaidsMade本番システムの完全なソースコードではありません。

掲載コードは記事の理解を目的として簡略化・切り出した公開用サンプルです。本番側では、ここに含まれない永続化、整合性、復旧、権限、記憶管理、状態管理などの処理があります。

現時点ではライセンスを設定していません。
