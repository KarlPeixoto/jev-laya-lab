# Learnings

Registro incremental das descobertas feitas durante o laboratório.

> Este arquivo privilegia observações experimentais. Hipóteses ainda não comprovadas são tratadas como hipóteses.

## Lab 01

### 1. API atual do Laya

A API Python utilizada no laboratório expõe:

```python
from laya import Router

router = Router()
result = router.predict(state, questions)
```

Para perguntas do tipo `choice`, a propriedade utilizada pela API é `criteria`, e não `choices`.

Exemplo:

```python
questions = {
    "category": {
        "type": "choice",
        "instructions": "Qual categoria melhor descreve o problema?",
        "criteria": [
            "security",
            "backend",
            "frontend",
            "infrastructure",
        ],
    }
}
```

### 2. Primeiro teste com `noul`

Estado:

> The sky is blue.

A decisão retornou um valor `noul` de aproximadamente `0.749`.

Um segundo teste com:

> The sky is green.

retornou aproximadamente `0.291`.

Um terceiro estado mais explícito, afirmando que o céu é azul mas a frase diz que ele é verde, retornou aproximadamente `0.037`.

Esses resultados sugerem sensibilidade ao conteúdo do estado, mas ainda não são suficientes para concluir como o valor deve ser interpretado ou calibrado.

### 3. Primeira classificação `choice`

Estado:

> Usuário não consegue fazer login via Google. O Keycloak retorna HTTP 403.

Critérios:

- security
- backend
- frontend
- infrastructure

Resultado:

```text
choice: security

security:        99.38%
backend:          0.25%
frontend:         0.31%
infrastructure:   0.06%

confidence:       0.9687
answer_confidence: 0.9938
```

### 4. Roteamento por idioma

Nesse mesmo experimento, o Router detectou:

```text
language: pt
model: multilingual
reason: Latin script but language looks like 'pt', not English
```

Portanto, o Router não apenas recebeu o texto e executou uma classificação. Houve uma etapa de roteamento que identificou o idioma e selecionou o checkpoint multilingual.

### 5. Caso claramente de backend

Estado utilizado:

> A API de pedidos está retornando HTTP 500. O banco PostgreSQL está funcionando normalmente.

Resultado:

```text
choice: backend

security:        7.62%
backend:        52.91%
frontend:       34.22%
infrastructure: 5.24%

confidence:       0.2393
answer_confidence: 0.5291
```

Esse resultado foi especialmente interessante porque o modelo escolheu `backend`, mas a distribuição foi muito menos concentrada do que no caso de segurança.

### 6. Caso ambíguo

Estado utilizado:

> O usuário não consegue acessar a aplicação. Às vezes recebe HTTP 403 e às vezes HTTP 500. Não sabemos ainda se o problema está no frontend, backend ou Keycloak.

Resultado:

```text
choice: security

security:        84.12%
backend:          4.22%
frontend:         8.95%
infrastructure:   2.71%

confidence:       0.5724
answer_confidence: 0.8412
```

O resultado indica que a decisão ficou menos concentrada do que no caso claramente relacionado ao Keycloak.

### 7. Cuidado com `confidence`

O checkpoint utilizado apresentou um aviso indicando que determinados valores de temperatura/confiança estavam fora dos limites esperados e que a confiança afetada deveria ser considerada **não calibrada**.

Portanto:

> Não devemos tratar `confidence` ou `answer_confidence` como uma probabilidade calibrada de acerto sem realizar experimentos específicos de calibração.

Essa é uma questão para os próximos labs.

## Próximas perguntas

1. A confiança diminui de forma consistente quando o caso fica ambíguo?
2. O modelo mantém boa separação entre categorias claramente diferentes?
3. O `confidence` pode ser utilizado como sinal para decidir entre automação e fallback?
4. Como o comportamento muda com diferentes formulações do mesmo problema?
5. Como Laya/System 1 se compara com uma decisão feita por um LLM?
