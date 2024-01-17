1- Acesso ao Site de Vagas (https://gruposeb.gupy.io/):
- Objetivo: Coletar informações sobre as vagas disponíveis (Cargo, Localidade, Efetividade)

2-  Acesso ao Formulário (https://forms.office.com/r/zfipx2RFsY):
- Objetivo: Preencher as informações e selecionar o flag apropriado



Em ambos:
- Utilização da ferramenta Playwright. Buscando o visual gráfico e otimização
- Design patterns de Page Objects para melhor e mais fácil leitura de código (divisão de páginas na pasta "pages")
- Arquitetura de logs pelo módulo de log buscando todos os retornos possíveis do processo, etapas e erros.
- Escrita de arquivo final (pasta "documents") com a ferramente openpyxl para manipulação de arquivos .xlsx

Bot Forms:
- Criação de arquivo modelo para iniciação do robô

Iniciar Bot Forms:

    python run_bot_forms.py

Iniciar Bot Gupy:

    python run_bot_gupy.py


Uso do módulo pipenv para ambientes:
1. pipenv shell
2. pipenv sync
3. playwright install
4. playwright install --dry-run (se necessário)