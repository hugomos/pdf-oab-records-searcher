def calc_execution_time(callback):
  """
    Um decorator que calcula o tempo de execução de uma função.

    Args:
        callback: a função a ser decorada.

    Returns:
        A função decorada.

    Exemplo:
        @calc_execution_time
        def minha_funcao(arg1, arg2):
            # Código da função
            pass
  """
  from time import time, strftime, gmtime
  
  def wrapper(*args, **kwargs):
    """
      Função que envolve a função original e calcula o tempo de execução.

      Args:
          *args: argumentos posicionais da função original.
          **kwargs: argumentos nomeados da função original.

      Returns:
          O valor de retorno da função original.
    """
    t1 = time()
    callback_return = callback(*args, **kwargs)
    t2 = time() - t1

    final = strftime("%H:%M:%S", gmtime(t2))
    print('Execution time: {0}'.format(final))
    
    return callback_return
  return wrapper