# Continuity Core — public sample

このサンプルは、AIエージェントの「人格」と「個体」を同じものとして扱わない考え方を説明するための最小構成です。

概念上、次のように分けています。

- **Identity / Personality**: 名前、自己認識、価値観、関係、言葉遣いなど
- **Memory**: 実際に起きた出来事や経験
- **Decision**: Identity・Memory・Current Stateを材料にした判断
- **Individual Continuity**: 「同じ設定」ではなく「この個体」が続くための識別と履歴
- **Output Adapters**: LLM、Voice、Body、Deviceなど、同じ個体を外部へ表現する交換可能な層

このディレクトリのコードは、上の考え方を理解するための**公開用の一般化・簡略サンプル**です。

特定のAI、キャラクター、ユーザー、本番システムの内部名や実データは含みません。
