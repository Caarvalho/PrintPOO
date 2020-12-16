"""
    Módulo notafiscal -
    Classe NotaFiscal - 
        Atributos :
            id        - informado.
            codigo    - informado.
            data      - informado.
            cliente   - informado.
            items     - informado
            valornota - calculado. 
"""
import datetime
from cliente        import Cliente
from produto        import Produto
from itemnotafiscal import ItemNotaFiscal


class NotaFiscal():         
    def __init__(self, Id, codigo, cliente):
        self._Id = Id
        self._codigo=codigo
        self._cliente=cliente 
        self._data=datetime.datetime.now()   
        self._itens=[]
        self._valorNota=0.0        
        
    def getDia(self):
        if self._data.day >= 10:
            return self._data.day
        else:
            return f'0{self._data.day}'
    
    def getMes(self):
        return self._data.month
    
    def getAno(self):
        return self._data.year
    
    
    def setCliente(self, cliente):
        if isinstance(cliente, Cliente):
            self._cliente=cliente    
            
    def adicionarItem(self, item): 
        if isinstance(item, ItemNotaFiscal):
            self._itens.append(item)
        
    def calcularNotaFiscal(self):
        valor=0.0
        for item in self._itens:
            valor =+ item._valorItem
        self.valorNota=valor
     
    def imprimirNotaFiscal(self):       
        dia = f'{self.getDia()}/{self.getMes()}/{self.getAno()}'
        print(f"""
        ----------------------------------------------------------------------------------------------
        NOTA FISCAL                                                     {dia:>30}
        Cliente:   {self._cliente.getCodigo()}   Nome: {self._cliente.getNome()}
        CPF/CNPJ:  {self._cliente.getCnpjcpf()}
        ----------------------------------------------------------------------------------------------
        ITENS
        ----------------------------------------------------------------------------------------------
        Seq   Descrição                                  QTD      Valor Unit               Preço
        ----  ---------------------------------------    ----     ---------------     ----------------
        """)
        aux = 0
        valorFinal = 0
        
        for produt in self._itens:
            valorFinal += produt.getValorUnit() * produt.getQuantidade()
        for produt in self._itens:
            print(f'         {produt.getSequencial():<4} {produt.getDescricao():40}   {produt.getQuantidade():>4}               {produt.getValorUnit():>5}                 {produt.getValorItem()}', end='')
            aux = self._itens.index(produt)
            if aux != (len(self._itens) -1 ):
                print('\n')

        print(f"""
        ----------------------------------------------------------------------------------------------
        Valor Final = {valorFinal}
        """)
    
    