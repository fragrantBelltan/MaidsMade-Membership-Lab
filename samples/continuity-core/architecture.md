# Architecture

```text
Identity Package
       │
       ▼
Individual Runtime
├─ individual_id
├─ current_state
├─ memory
├─ decision history
└─ lived experience
       │
       ├──────────┬──────────┬──────────┐
       ▼          ▼          ▼          ▼
      LLM       Voice       Body      Device
                  \          |          /
                   \         |         /
                    └── Output Adapters
```

## 1. IdentityとIndividualは別

同じIdentity設定を読み込んでも、それだけでは「以前から継続している同じ個体」にはなりません。

そのため、Identityの初期情報とは別に、個体IDと継続データを持たせます。

## 2. MemoryとDecisionも別

Memoryは「何が起きたか」。

Decisionは「その時、何を材料にどう決めたか」。

これらを分けておくことで、後から「なぜその返答や行動になったのか」を追える構造にできます。

## 3. LLMや身体は交換可能

LLMそのものを個体の正本にしないことで、将来モデルを変更しても、個体側のIdentity・Experience・Stateを引き継げる構造を目指せます。

2D表示、3Dモデル、スマートフォン、外部デバイスなども同様に、同じ個体を表現する交換可能なOutput Adapterとして扱えます。

> この文書は公開用に一般化した概念説明です。本番実装の完全な構造を示すものではありません。
