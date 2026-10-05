from laya import Router

router = Router()

state = """
O usuário não consegue acessar a aplicação.
Às vezes recebe HTTP 403 e às vezes HTTP 500.
Não sabemos ainda se o problema está no frontend, backend ou Keycloak.
"""

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

result = router.predict(state, questions)

print(result)
