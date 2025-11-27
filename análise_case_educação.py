"""Análise Case Educação

# Imports
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import warnings
warnings.filterwarnings('ignore')

"""# Leitura inicial dos dados"""

dados = pd.read_csv("StudentsPerformance.csv")

dados.shape

dados.head()

"""# Inspeção da Base de Dados"""

nulos = dados.isnull()

plt.figure(figsize=(16, 5))
plt.title("Análise de Nulos")
sns.heatmap(nulos, cbar=False);

nulos.sum()

dados.nunique()

dados.duplicated().sum()

dados.info()

dados.describe()

"""# Análises Categóricas"""

dados["gender"].value_counts(normalize = True) * 100

dados["race/ethnicity"].value_counts(normalize = True) * 100

dados["parental level of education"].value_counts(normalize = True) * 100

dados["lunch"].value_counts(normalize = True) * 100

dados["test preparation course"].value_counts(normalize = True) * 100

"""# Análise de Distribuição de Notas"""

sns.boxplot(data =  dados, x = "math score", y = "gender");

sns.boxplot(data =  dados, x = "reading score", y = "gender");

sns.boxplot(data =  dados, x = "writing score", y = "gender");

dados.groupby("gender").describe()["math score"].reset_index()

dados.groupby("gender").describe()["reading score"].reset_index()

dados.groupby("gender").describe()["writing score"].reset_index()

"""# Análise de Distribuição de Raça e Etnia"""

sns.pairplot(dados, hue = "race/ethnicity");

sns.boxplot(data = dados, x = "math score", y = "race/ethnicity");

sns.boxplot(data = dados, x = "reading score", y = "race/ethnicity");

sns.boxplot(data = dados, x = "writing score", y = "race/ethnicity");

"""# Análise de Distribuição Parental"""

sns.boxplot(data = dados, x = "math score", y = "parental level of education");

sns.boxplot(data = dados, x = "reading score", y = "parental level of education");

sns.boxplot(data = dados, x = "writing score", y = "parental level of education");

dados.groupby("parental level of education").describe()["math score"].reset_index()

dados.groupby("parental level of education").describe()["reading score"].reset_index()

dados.groupby("parental level of education").describe()["writing score"].reset_index()

"""# Análise de Preparação Pré-Prova"""

sns.boxplot(data = dados, x = "math score", y = "test preparation course");

sns.boxplot(data = dados, x = "reading score", y = "test preparation course");

sns.boxplot(data = dados, x = "writing score", y = "test preparation course");

dados.groupby("test preparation course").describe()["math score"].reset_index()

dados.groupby("test preparation course").describe()["reading score"].reset_index()

dados.groupby("test preparation course").describe()["writing score"].reset_index()

"""# Análise de Relação de Notas"""

sns.relplot(dados, x = "math score", y = "reading score", hue = "writing score");