from playwright.sync_api import Playwright
import logging, traceback

from .pages.initial_page import InitialPage
from .write_file import write_file


class Bot:
    def __init__(self) -> None:
        # conexão com DB
        pass

    def run(self, playwright: Playwright, import_id) -> None:
        try:
            browser = playwright.chromium.launch(headless=False, args=["--start-maximized"])
            context = browser.new_context(no_viewport=True)
            page = context.new_page()
            
            logging.info('PROCESSANDO')
            
            # Instâncias de todas as páginas do fluxo
            initial = InitialPage(page)
            
            extract_data = initial.extract_data()
            if extract_data['error']:
                logging.error(f"ERRO NA EXTRAÇÃO: {extract_data['data']} | IMPORT_ID: {import_id}")
                print(extract_data['type'])
                # update DB - {"status" : extract_data['type']}
                return
            
            logging.info('EXTRAÇÃO FINALIZADA')
            items = extract_data['data']
            
            file_result = write_file(items, import_id)
            if file_result['error']:
                logging.error(f"ERRO NA ESCRITA DO ARQUIVO: {file_result['data']} | IMPORT_ID: {import_id}")
                print(file_result['type'])
                # update DB - {"status" : file_result['type']}
                return

            logging.info(f'PROCESSO CONCLUÍDO | IMPORT_ID: {import_id}')
            # update DB - {"status" : Finalizado}
            
            # ---------------------
            context.close()
            browser.close()
            return
        
        except:
            error = traceback.format_exc()
            logging.error(f"ERRO NO PROCESSO: {error} | IMPORT_ID: {import_id}")
            return