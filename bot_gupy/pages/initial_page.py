import traceback


class InitialPage:
    def __init__(self, page) -> None:
        # instância da página para todas as funções respectivas 
        self.page = page
        
    def extract_data(self) -> dict:
        """Descrição:
        ---------------
            `Executa o processo completo de extração de dados`
            
        Retorno:
        --------
            {'error': bool, 'type': str, 'data': str}
            - error: se há erro
            - type: tipo do erro
            - data: exception
        
        """
        try:
            site = self.go_to_site()
            if site['error']:
                return site
            
            self.check_modal()
            
            extract_jobs = self.extract_jobs()
            if extract_jobs['error']:
                return extract_jobs
            
            return {'error': False, 'type': '', 'data': extract_jobs['data']}
            
        except:
            error = traceback.format_exc()
            return {'error': True, 'type': 'Erro ao extrair dados', 'data': error}
            
    def go_to_site(self) -> dict:
        """Descrição:
        ---------------
            `Abre o site indicado`
        
        """
        try:
            self.page.goto("https://gruposeb.gupy.io/", timeout=30000)
            return {'error': False, 'type': '', 'data': ''}
        
        except:
            error = traceback.format_exc()
            return {'error': True, 'type': 'Site instável/indisponível', 'data': error}
        
    def check_modal(self) -> None:
        """Descrição:
        ---------------
            `Confere se há um modal. Se existente, é fechado`
        
        """
        try:
            self.page.get_by_role("button", name="Ok, entendi.").wait_for(timeout=2000)
            self.page.get_by_role("button", name="Ok, entendi.").click()
            pass
        
        except:
            pass
        
    def extract_jobs(self) -> dict:
        """Descrição:
        ---------------
            `Manipula e extrai os dados de forma completa`
        
        Retorno:
        --------
            ['data']: em caso de sucesso retornará uma lista
        """
        try:
            jobs_list = []
            
            while True:
                # Extração dos textos dos elementos
                items = self.page.eval_on_selector_all('li[data-testid="job-list__listitem"] a div div', 'elements => elements.map(element => element.textContent)')
                
                # Separação em conjuntos de 3
                for i in range(0, len(items), 3):
                    jobs_list.append(items[i:i + 3])
                
                # Verificação do botão de ir para a página seguinte
                next_page_btn = self.page.get_by_test_id("pagination-next-button")
                if next_page_btn.is_enabled():
                    next_page_btn.click()
                    continue
                break
            
            return {'error': False, 'type': '', 'data': jobs_list}

        except:
            error = traceback.format_exc()
            return {'error': True, 'type': 'Erro ao extrair dados', 'data': error}