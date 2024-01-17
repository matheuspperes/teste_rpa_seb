import traceback


class InitialPage:
    def __init__(self, page) -> None:
        # instância da página para todas as funções respectivas 
        self.page = page
        
    def make_register(self, job='cargo', city='Bauru', is_effective='Sim'):
        """Descrição:
        ---------------
            `Executa o processo completo cadastro de resposta`
        
        Argumentos:
        -----------
            - job (str)
            - is_effetive (str): "Sim" ou "Não"
            - city (str)
        
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
            
            input_job = self.input_job(job)
            if input_job['error']:
                return input_job
            
            input_city = self.input_city(city)
            if input_city['error']:
                return input_city
            
            select_job_effective = self.select_job_effective(is_effective)
            if select_job_effective['error']:
                return select_job_effective
            
            send_answer_and_check = self.send_answer_and_check()
            if send_answer_and_check['error']:
                return send_answer_and_check
            
            return {'error': False, 'type': '', 'data': ''}
            
        except:
            error = traceback.format_exc()
            return {'error': True, 'type': 'Erro ao completar cadastro de resposta', 'data': error}
            
    def go_to_site(self):
        """Descrição:
        ---------------
            `Abre o site indicado`
        
        """
        try:
            self.page.goto("https://forms.office.com/pages/responsepage.aspx?id=QhQEvrbz4UuFCeypyBdSj7tyC7WzU59DoUmUzzgLXidUNllOQ0JYNjVMSDZSN1Q4MUFZWlVXQkw0UC4u", timeout=30000)
            return {'error': False, 'type': '', 'data': ''}
        
        except:
            error = traceback.format_exc()
            return {'error': True, 'type': 'Site instável/indisponível', 'data': error}
        
    def input_job(self, job='cargo'):
        """Descrição:
        ---------------
            `Insere o cargo`
        
        Argumentos:
        -----------
            - job (str)
        """
        try:
            self.page.get_by_role("textbox", name="CargoRequer resposta").fill(job)
            return {'error': False, 'type': '', 'data': ''}
        
        except:
            error = traceback.format_exc()
            return {'error': True, 'type': 'Erro ao colocar cargo', 'data': error}
        
    def select_job_effective(self, is_effective="Sim"):
        """Descrição:
        ---------------
            `Seleciona a opção de efetividade do cargo`
        
        Argumentos:
        -----------
            - is_effetive (str): "Sim" ou "Não"
        
        """
        try:
            self.page.locator("label").filter(has_text=f"{is_effective}").get_by_role("radio", name="Efetivo?Requer resposta").check()
            return {'error': False, 'type': '', 'data': ''}
        
        except:
            error = traceback.format_exc()
            return {'error': True, 'type': 'Erro ao selecionar efetividade do cargo', 'data': error}
        
    def input_city(self, city='Bauru'):
        """Descrição:
        ---------------
            `Insere cidade`
        
        Argumentos:
        -----------
            - city (str)
        """
        try:
            self.page.get_by_role("textbox", name="CidadeRequer resposta").fill(city)
            return {'error': False, 'type': '', 'data': ''}
        
        except:
            error = traceback.format_exc()
            return {'error': True, 'type': 'Erro ao colocar cidade', 'data': error}
    
    def send_answer_and_check(self):
        """Descrição:
        ---------------
            `Envia resposta e faz a sua confirmação`
        """
        try:
            self.page.get_by_role("button", name="Enviar").click()
            self.page.get_by_text("Sua resposta foi gravada com êxito.").wait_for(timeout=10000)
            return {'error': False, 'type': '', 'data': ''}
        
        except:
            error = traceback.format_exc()
            return {'error': True, 'type': 'Erro ao enviar resposta', 'data': error}
