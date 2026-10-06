from laya import Router

router = Router()

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

cases = [
    {
        "name": "security_clear",
        "state": """
        O usuário não consegue fazer login.
        O Keycloak retorna HTTP 403.
        """,
        "expected": "security",
    },
    {
        "name": "backend_clear",
        "state": """
        A API de pedidos está retornando HTTP 500.
        O erro acontece dentro do serviço backend.
        """,
        "expected": "backend",
    },
    {
        "name": "frontend_clear",
        'state': """
        O React apresneta um erro de renderização no componente LoginForm.
        O backend está respondendo normalmente.
        O problema está exclusivamente na interface web.
        """,
        "expected": "frontend",
    },
    {
        "name": "infrastructure_clear",
        "state": """
        O servidor da aplicação está fora do ar.
        O container não consegue iniciar porque o host está sem memória.
        """,
        "expected": "infrastructure",
    },
]

for case in cases:
    result = router.predict(case["state"], questions)
    answer = result["answers"]["category"]

    print("=" * 70)
    print(case["name"])
    print("Expected:", case["expected"])
    print("Choice:", answer["choice"])
    print("Probabilities:", answer["probabilities"])
    print("Confidence:", answer["confidence"])
    print("Answer confidence:", answer["answer_confidence"])
