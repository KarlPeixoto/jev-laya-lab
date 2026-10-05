# JEV / Laya Lab

Laboratório prático para estudar o paradigma **JEV / System 1** por meio do projeto open-source **Laya**.

A proposta deste repositório não é apenas reproduzir exemplos: é experimentar, medir resultados, registrar limitações e entender onde uma camada de decisão especializada pode ser útil em sistemas reais.

## Objetivos

- Entender na prática decisões do tipo `noul`, `choice` e `score`.
- Explorar roteamento de modelos/checkpoints.
- Observar confiança e distribuição de probabilidades.
- Testar decisões claras e ambíguas.
- Comparar posteriormente decisões especializadas com LLMs.
- Investigar integração com APIs e workflows, especialmente n8n.
- Construir conhecimento suficiente para avaliar um possível uso profissional de JEV/System 1.

## Ambiente

- Linux / Omarchy
- Python 3.14.7
- CPU-only
- PyTorch 2.14.1+cpu
- Laya 0.3.28

O laboratório foi executado sem GPU NVIDIA.

## Estrutura

```text
jev-laya-lab/
├── README.md
├── LEARNINGS.md
├── lab01.py
├── .gitignore
└── results/
    └── lab01.md
```

## Labs

### Lab 01 — Primeiras decisões

Primeiros experimentos com:

- `noul`
- `choice`
- `Router`
- detecção de idioma
- checkpoint multilingual
- probabilidades de escolha
- `confidence` e `answer_confidence`

[Resultados do Lab 01](results/lab01.md)

### Lab 02 — Em breve

Avaliação sistemática de classificações claras e ambíguas.

## Princípio do laboratório

A intenção é descobrir empiricamente onde o paradigma funciona bem e onde falha.

Não estamos tentando provar que Laya/JEV é melhor que LLMs. A pergunta é:

> **Em quais tipos de decisão uma abordagem System 1 especializada pode ser útil, mais previsível ou mais eficiente?**

## Status

**Lab 01 concluído. Lab 02 em preparação.**
