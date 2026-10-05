# Lab 01 — Primeiras decisões

## Objetivo

Executar as primeiras decisões com Laya e observar:

- tipos de decisão;
- roteamento;
- classificação;
- probabilidades;
- sinais de confiança.

## Experimento 1 — `noul`

Foi utilizado um estado simples sobre a cor do céu.

### Resultado

Para:

```text
The sky is blue.
```

o modelo retornou aproximadamente:

```text
noul: 0.749
confidence: 0.749
```

Para:

```text
The sky is green.
```

retornou aproximadamente:

```text
noul: 0.291
confidence: 0.709
```

Para:

```text
The sky is blue, but the statement says that the sky is green.
```

retornou aproximadamente:

```text
noul: 0.037
confidence: 0.963
```

O checkpoint também apresentou um aviso de que determinados valores relacionados à confiança estavam fora dos limites esperados e que a confiança afetada deveria ser considerada não calibrada.

---

## Experimento 2 — `choice` e roteamento em português

### Estado

```text
Usuário não consegue fazer login via Google.
O Keycloak retorna HTTP 403.
```

### Critérios

```text
security
backend
frontend
infrastructure
```

### Resultado

```text
choice: security

security:        99.38%
backend:          0.25%
frontend:         0.31%
infrastructure:   0.06%

confidence:       0.9687
answer_confidence: 0.9938
```

### Roteamento

```text
model: multilingual
repo: convaiinnovations/laya/multilingual
language: pt
is_english: false
```

O Router identificou português e selecionou o modelo multilingual.

---

## Experimento 3 — Caso de backend

### Estado

```text
A API de pedidos está retornando HTTP 500.
O banco PostgreSQL está funcionando normalmente.
```

### Resultado

```text
choice: backend

security:        7.62%
backend:        52.91%
frontend:       34.22%
infrastructure: 5.24%

confidence:       0.2393
answer_confidence: 0.5291
```

Apesar de escolher `backend`, a distribuição ficou bastante menos concentrada que no caso anterior.

O Router classificou o idioma como indeterminado e ainda assim selecionou o checkpoint multilingual:

```text
language: None
language_undecided: true
model: multilingual
```

---

## Experimento 4 — Caso ambíguo

### Estado

```text
O usuário não consegue acessar a aplicação.
Às vezes recebe HTTP 403 e às vezes HTTP 500.
Não sabemos ainda se o problema está no frontend, backend ou Keycloak.
```

### Resultado

```text
choice: security

security:        84.12%
backend:          4.22%
frontend:         8.95%
infrastructure:   2.71%

confidence:       0.5724
answer_confidence: 0.8412
```

A decisão continuou sendo `security`, porém com sinais de confiança inferiores ao caso claramente relacionado ao Keycloak.

---

## Observação importante

Os resultados são interessantes, mas esta bateria é pequena e não permite afirmar que o comportamento observado será consistente em geral.

O próximo passo será criar uma bateria de casos controlados e medir sistematicamente:

- acurácia;
- distribuição das probabilidades;
- confiança;
- comportamento em casos ambíguos;
- possíveis falsos positivos e falsos negativos.

## Conclusão do Lab 01

O primeiro laboratório confirmou que conseguimos:

1. executar Laya localmente;
2. utilizar `noul` e `choice`;
3. fornecer critérios para classificação;
4. observar probabilidades por categoria;
5. observar `confidence` e `answer_confidence`;
6. observar o Router identificando idioma e selecionando o checkpoint multilingual.

A principal hipótese para o Lab 02 é:

> **A confiança do sistema acompanha de alguma forma a dificuldade/ambiguidade da decisão?**

Essa hipótese ainda precisa ser testada.
