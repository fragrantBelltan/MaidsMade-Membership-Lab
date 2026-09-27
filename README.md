# MaidsMade Membership Lab

MaidsMadeで実際に開発している仕組みのうち、**公開しても本体の資産性を損なわない範囲**だけを、一般化・簡略化して置く技術補足リポジトリです。

主にnoteのメンバーシップ記事から参照するために使います。

## 公開方針

公開サンプルでは、本番固有の名前・人格名・役割名・内部構成名をそのまま出さず、可能な限り一般名へ置き換えます。

例:

- 固有のAI名 → `Agent` / `AI Agent`
- 固有のBrain名 → `Identity Package`
- 固有の個体runtime名 → `Individual Runtime`
- 固有の身体・音声実装 → `Output Adapter` / `Body Adapter` / `Voice Adapter`

目的は本番コードを再配布することではなく、記事で扱った考え方を第三者が理解できる程度の最小サンプルとして示すことです。

## このリポジトリに置くもの

- 記事の理解を助ける最小コード
- 一般化した構造図
- 実装思想が分かる小さなサンプル
- 本番実装とは切り離した検証用コード
- 公開して問題ない技術メモ

## 置かないもの

- MaidsMade本番Brainそのもの
- 実際の個体runtime / memory DB
- 実ユーザーやキャラクターの実データ
- 本番固有の人格名・内部識別名
- 自律判断・記憶選択などの中核実装の完全版
- APIキー、Cookie、token、認証情報
- 本番環境固有の設定やパス

## Samples

### continuity-core

AIエージェントを「LLMのセッション内だけに存在する設定」ではなく、Identity・Memory・Decision・Individual Continuityを分けて持つ存在として扱う考え方の最小サンプルです。

- [概要](samples/continuity-core/README.md)
- [構造](samples/continuity-core/architecture.md)
- [個体IDの例](samples/continuity-core/identity_example.py)
- [記憶 / 判断の分離例](samples/continuity-core/memory_schema.sql)

## 注意

このリポジトリはMaidsMade本番システムの完全なソースコードではありません。

掲載コードは記事の理解を目的として一般化・簡略化した公開用サンプルです。本番側では、ここに含まれない永続化、整合性、復旧、権限、記憶管理、状態管理などの処理があります。

現時点ではライセンスを設定していません。
