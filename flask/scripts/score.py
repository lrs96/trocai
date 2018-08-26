import numpy as np
import pandas as pd

def getSamples():
    score_base = pd.read_csv('sample_data\\sample.csv',delimiter=';')
    return score_base

def updateRatingComprador(score_base):
    #Calcula rating mediano atualizado para compras
    #Objetivo futuro utilizar scikit learn com modelo de decision tree
    score_base = score_base.assign(pont_trans_compradora = (score_base['negociacoes_compradora']/score_base['negociacoes_compradora'].max())*score_base['avaliacao_compradora'])
    return score_base

def updateRatingVendedor(score_base):
    #Calcura rating mediano atualizado para vendas
    #Objetivo futuro utilizar scikit learn com modelo de decision tree
    score_base = score_base.assign(pont_trans_vendedora = (score_base['negociacoes_vendedora']/score_base['negociacoes_vendedora'].max())*score_base['avaliacao_vendedora'])
    return score_base

def getCompradores(score_base):
    #lista compradores unicos da base
    return score_base.id_empresa_compradora.unique()

def getVendedores(score_base):
    #lista vendedores unicos da base
    return score_base.id_empresa_vendedora.unique()


def getScoreComprador(score_base, comprador):
    #atualiza calculo de rating do comprador
    updateRatingComprador(score_base)
    #retorna mediana dos valores ponderados e atualizados
    return score_base.query('id_empresa_compradora=='+str(comprador))['pont_trans_compradora'].median()

def getScoreVendedor(score_base, vendedor):
    #atualiza calculo de rating de vendedor
    updateRatingVendedor(score_base)
    
    #retorna mediana dos valores ponderados e atualizados
    return score_base.query('id_empresa_vendedora=='+str(vendedor))['pont_trans_vendedora'].median()

##### Exemplos de utilizacao

#Exemplo de chamada de lista de vendedores com dados de teste
getVendedores(getSamples())

#Exemplo de chamada de lista de compradores com dados de teste
getCompradores(getSamples())

#Busca de rating de comprador
getScoreComprador(getSamples(),2)

#Busca de rating de vendedor
getScoreVendedor(getSamples(),1)
