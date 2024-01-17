from playwright.sync_api import Playwright
import logging, traceback

from .pages.initial_page import InitialPage
from bot_forms.file_controller import read_file, write_file


class Bot:
    def __init__(self) -> None:
        # conexão com DB
        pass

    def run(self, playwright: Playwright, import_id) -> None:
        """Descrição:
        -------------
            `Função principal para execução completa do processo`

        Argumentos:
            - playwright (Playwright): objeto de navegação do playwright
            - import_id (str): id da importação
        """
        try:
            browser = playwright.chromium.launch(headless=False, args=["--start-maximized"])
            context = browser.new_context(no_viewport=True)
            page = context.new_page()
            
            # Instâncias de todas as páginas do fluxo
            initial = InitialPage(page)
            
            # leitura de arquivo modelo
            get_items = read_file()
            if get_items['error']:
                logging.error(f"ERRO NO CADASTRO: {get_items['data']} | IMPORT_ID: {import_id}")
                print(get_items['type'])
                # update DB - {"status" : items['type']}
                return
            
            logging.info('PROCESSANDO')
            
            items = get_items['data']
            
            for index, item in enumerate(items):
                make_register = initial.make_register(*item)
                
                if make_register['error']:
                    logging.error(f"ERRO NO CADASTRO: {make_register['data']} | IMPORT_ID: {import_id}")
                    print(make_register['type'])
                    
                    # create DB - {"status" : make_register['type']}
                    items[index] = (*item, make_register['type'])
                    continue
                                
                items[index] = (*item, 'SUCESSO')
                # create DB - {"status" : 'success'}
                
            file_result = write_file(items, import_id)
            if file_result['error']:
                logging.error(f"ERRO NA ESCRITA DO ARQUIVO: {file_result['data']} | IMPORT_ID: {import_id}")
                print(file_result['type'])
                # update DB - {"status" : file_result['type']}
                return
                
            logging.info(f'PROCESSO CONCLUÍDO | IMPORT_ID: {import_id}')

            # ---------------------
            context.close()
            browser.close()
            return
            
        except:
            error = traceback.format_exc()
            logging.error(f"ERRO NO PROCESSO: {error} | IMPORT_ID: {import_id}")
            return