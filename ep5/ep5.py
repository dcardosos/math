def main():
    """
        ...complete...
    """

def verifica_representacao(b, n):
    """ (int, int) --> bool

        Recebe um inteiro positivo n e um inteiro b, 2 <= b <= 10.
        Esta função retorna True se n é a representação de algum 
        inteiro na base b. Em caso contrário, retorna False.   
    """
    
    numbers = [int(d) for d in str(n)] 
    retorno = True

    for num in numbers:

        if num >=0 and num < b:
            retorno = True

        else:
            retorno = False
            break

    return(retorno)       


def decimal_para_outra_base(n, b):
    """ (int, int) --> int

        Recebe um inteiro positivo n na base 10 e um inteiro b, 2 <= b < 10.
        Esta função constrói e retorna o número inteiro k que é a representação
        de n na base b.
    """


def outra_base_para_decimal(b, n):
    """ (int, int) --> int

        Recebe um inteiro b, 2 <= b < 10, e um inteiro positivo n na base b.
        Esta função constrói e retorna o número inteiro k que é a representação
        de n na base 10.   
    """
    
def adicao_dois_inteiros_mesma_base(b, m, n):
    """ (int, int, int) --> int

        Recebe um inteiro b, 2 <= b <= 10, e dois inteiros positivos m e n na base b.
        Esta função constrói e retorna o número inteiro soma que é o inteiro resultante 
        da adição na base b dos inteiros m e n.
    """