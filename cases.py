cases = [
    # =========================
    # SECURITY
    # =========================

    {
        "name": "security_01",
        "state": "O usuário recebe HTTP 403 ao tentar acessar uma área protegida.",
        "expected": "security",
    },
    {
        "name": "security_02",
        "state": "O Keycloak rejeita o login do usuário por falta de permissão.",
        "expected": "security",
    },
    {
        "name": "security_03",
        "state": "A autenticação do usuário falha porque ele não possui a role necessária.",
        "expected": "security",
    },
    {
        "name": "security_04",
        "state": "O token JWT enviado pela aplicação está expirado e a API retorna 401.",
        "expected": "security",
    },
    {
        "name": "security_05",
        "state": "Um usuário autenticado não consegue acessar um recurso que exige autorização específica.",
        "expected": "security",
    },
    {
        "name": "security_06",
        "state": "O sistema bloqueia o acesso porque as credenciais fornecidas são inválidas.",
        "expected": "security",
    },
    {
        "name": "security_07",
        "state": "A aplicação recebe um token válido, mas o usuário não tem a permissão necessária para executar a operação.",
        "expected": "security",
    },
    {
        "name": "security_08",
        "state": "O login via Google não consegue concluir a autenticação no provedor de identidade.",
        "expected": "security",
    },
    {
        "name": "security_09",
        "state": "O acesso a uma funcionalidade administrativa é negado para um usuário sem perfil adequado.",
        "expected": "security",
    },
    {
        "name": "security_10",
        "state": "O servidor retorna HTTP 401 porque a requisição não contém credenciais de autenticação.",
        "expected": "security",
    },


    # =========================
    # BACKEND
    # =========================

    {
        "name": "backend_01",
        "state": "A API de pedidos retorna HTTP 500 ao processar uma requisição.",
        "expected": "backend",
    },
    {
        "name": "backend_02",
        "state": "O serviço backend lança uma exceção ao buscar os dados no PostgreSQL.",
        "expected": "backend",
    },
    {
        "name": "backend_03",
        "state": "Uma requisição para a API termina com erro porque uma regra de negócio falhou no servidor.",
        "expected": "backend",
    },
    {
        "name": "backend_04",
        "state": "O endpoint de clientes está retornando dados incorretos por causa de um erro no serviço.",
        "expected": "backend",
    },
    {
        "name": "backend_05",
        "state": "O controller recebe a requisição, mas o processamento do serviço lança uma exceção.",
        "expected": "backend",
    },
    {
        "name": "backend_06",
        "state": "A API não consegue salvar um novo pedido porque ocorreu um erro durante o processamento no servidor.",
        "expected": "backend",
    },
    {
        "name": "backend_07",
        "state": "O endpoint retorna HTTP 500 ao executar uma operação de negócio.",
        "expected": "backend",
    },
    {
        "name": "backend_08",
        "state": "O serviço Java falha ao consultar o banco de dados e a API retorna erro.",
        "expected": "backend",
    },
    {
        "name": "backend_09",
        "state": "A aplicação recebe corretamente a requisição, mas o serviço responsável pelo processamento apresenta uma falha.",
        "expected": "backend",
    },
    {
        "name": "backend_10",
        "state": "Uma regra de negócio implementada no servidor está produzindo uma exceção inesperada.",
        "expected": "backend",
    },


    # =========================
    # FRONTEND
    # =========================

    {
        "name": "frontend_01",
        "state": "O botão de salvar não aparece corretamente na interface React.",
        "expected": "frontend",
    },
    {
        "name": "frontend_02",
        "state": "A página apresenta um erro de renderização no navegador.",
        "expected": "frontend",
    },
    {
        "name": "frontend_03",
        "state": "O componente LoginForm apresenta um erro visual na aplicação web.",
        "expected": "frontend",
    },
    {
        "name": "frontend_04",
        "state": "Um campo do formulário não está sendo exibido corretamente na tela.",
        "expected": "frontend",
    },
    {
        "name": "frontend_05",
        "state": "A interface React quebra quando o usuário abre a tela de pedidos.",
        "expected": "frontend",
    },
    {
        "name": "frontend_06",
        "state": "O menu da aplicação não responde ao clique do usuário no navegador.",
        "expected": "frontend",
    },
    {
        "name": "frontend_07",
        "state": "Um componente da página não é renderizado e aparece vazio para o usuário.",
        "expected": "frontend",
    },
    {
        "name": "frontend_08",
        "state": "O layout da tela está quebrado e os elementos aparecem fora da posição esperada.",
        "expected": "frontend",
    },
    {
        "name": "frontend_09",
        "state": "O JavaScript da aplicação apresenta um erro durante a renderização de uma página.",
        "expected": "frontend",
    },
    {
        "name": "frontend_10",
        "state": "O problema acontece exclusivamente na interface web; a API está respondendo normalmente.",
        "expected": "frontend",
    },


    # =========================
    # INFRASTRUCTURE
    # =========================

    {
        "name": "infrastructure_01",
        "state": "O container da aplicação não consegue iniciar porque o servidor está sem memória.",
        "expected": "infrastructure",
    },
    {
        "name": "infrastructure_02",
        "state": "O servidor onde a aplicação está hospedada está indisponível.",
        "expected": "infrastructure",
    },
    {
        "name": "infrastructure_03",
        "state": "O container da aplicação foi encerrado porque o host ficou sem recursos.",
        "expected": "infrastructure",
    },
    {
        "name": "infrastructure_04",
        "state": "A máquina virtual que hospeda o sistema está fora do ar.",
        "expected": "infrastructure",
    },
    {
        "name": "infrastructure_05",
        "state": "O serviço não consegue iniciar porque o ambiente de execução está sem espaço em disco.",
        "expected": "infrastructure",
    },
    {
        "name": "infrastructure_06",
        "state": "O servidor perdeu conectividade de rede e a aplicação ficou indisponível.",
        "expected": "infrastructure",
    },
    {
        "name": "infrastructure_07",
        "state": "O Kubernetes não consegue agendar o pod porque não há recursos disponíveis no cluster.",
        "expected": "infrastructure",
    },
    {
        "name": "infrastructure_08",
        "state": "O ambiente de produção está indisponível porque o host apresentou uma falha.",
        "expected": "infrastructure",
    },
    {
        "name": "infrastructure_09",
        "state": "A aplicação não inicia porque o ambiente onde ela deveria executar está indisponível.",
        "expected": "infrastructure",
    },
    {
        "name": "infrastructure_10",
        "state": "O servidor está sobrecarregado e os containers da aplicação estão sendo reiniciados.",
        "expected": "infrastructure",
    },
]
