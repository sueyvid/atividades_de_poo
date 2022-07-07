'''
Análise de dados do Youtube (YTDA)
Projeto final de POO - ECT/UFRN

Módulo com funções utilitárias para
gráficos

Prof. Bruno Silva
'''

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def grafico_barras(df, col_x, col_y, leg_x, leg_y):
    '''
    Mostra gráfico de barras
    de um dataframe Pandas.
    '''
    sns.catplot(data=df, x=col_x, y=col_y, kind='bar',
                ci=None, legend_out=False, aspect=2)

    plt.ylabel(leg_y)
    plt.xlabel(leg_x)
    plt.xticks(rotation=90)
    plt.ticklabel_format(style='plain', axis='y')
    plt.show()

    # os warnings são por causa de caracteres 'estranhos' presentes 
    # nos títulos