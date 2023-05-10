import os
import sys
import re

import pandas as pd
from PyPDF2 import PdfReader

from helpers.decorators.calc_execution_time import calc_execution_time

from typing import List

class Main:
  BASE_PATH = os.path.dirname(os.path.abspath(__file__))
  ASSETS_PATH = os.path.join(BASE_PATH, 'assets')
  
  def __init__(self, data) -> None:
    self.__oab_records = data.get('oab_records', None)

    if(self.__oab_records is None):
      raise ValueError('No oab_records provided')

  def get_files_from_path(self, path: str, type:str='pdf') -> List[str]:
    """
      Retorna uma lista de caminhos completos de arquivos que correspondem a um determinado tipo 
      (por padrão, arquivos com extensão .pdf) dentro de um diretório especificado.

      Args:
          path (str): O caminho completo para o diretório a ser verificado.
          type (str, opcional): A extensão do tipo de arquivo a ser procurado (por padrão, 'pdf').

      Returns:
          List[str]: Uma lista contendo os caminhos completos dos arquivos encontrados.

      Exemplo:
          >>> get_files_from_path('/path/to/directory', 'txt')
          ['/path/to/directory/file1.txt', '/path/to/directory/file2.txt']
    """
    return [os.path.join(path, file) for file in os.listdir(path) if file.endswith(type)]

  def get_all_matches(self, files: List[str]) -> List[object]:
    """
      Retorna uma lista de objetos representando todas os matchs encontrados nos arquivos PDF fornecidos que correspondem aos registros da OAB.

      Args:
          files (List[str]): uma lista contendo o caminho para os arquivos PDF.

      Returns:
          List[object]: uma lista de objetos contendo informações sobre cada match encontrado, incluindo o registro da OAB correspondente, o nome do arquivo PDF em que o match foi encontrado e o número da página em que o match aparece.

      Raises:
          Exception: se nenhum match for encontrado nos arquivos PDF.

      Exemplo:
          get_all_matches(['file1.pdf', 'file2.pdf', 'file3.pdf'])
    """
    matchs = []
    
    for file in files:
      pdf = PdfReader(file)
      n_pages = len(pdf.pages)

      for page in range(1, n_pages):
        page_content = pdf.pages[page].extract_text()

        for oab in self.__oab_records:
          if(re.findall(oab, page_content)):
            matchs.append({'oab_record': oab, 'file': file, 'page': page + 1})

    if(len(matchs) <= 0):
      raise Exception("No matches found")

    return matchs

  def generate_matches_report(self, matches: List[object]) -> None:
    """
      Gera um relatório em formato Excel contendo informações sobre uma lista de matchs.

      Args:
          matches (List[object]): uma lista contendo objetos que representam os matchs.

      Returns:
          None: a função não retorna nenhum valor, apenas salva o arquivo Excel no caminho especificado.

      Exemplo:
          generate_matches_report([match1, match2, match3])
    """
    
    df = pd.DataFrame(matches)
    df.sort_values(by=['file', 'page'], inplace=True)
  
    df.to_excel(os.path.join(Main.ASSETS_PATH, 'xlsx', 'matches.xlsx'), index=False)
    return None
    
  @calc_execution_time
  def execute(self) -> None:
    files = self.get_files_from_path(os.path.join(Main.ASSETS_PATH, 'pdf'))    
    self.generate_matches_report(self.get_all_matches(files))
    return None

def main(parameters):
    data = {}
    for parameter in parameters:
        key, value = None, None

        if(len(parameter.split("=")) == 1):
            pass
        else:
            key = parameter.split("=")[0]
            value = parameter.split("=")[1]

        if(key == 'oab_records'):
            if(value != 'null'):
                data.update(
                    {'oab_records': [str(value).strip() for value in value.split(',')]})
                  
    Main(data).execute()

if __name__ == "__main__":
    try:
        main(parameters=sys.argv[1:])
    except Exception as e:
        print(e)