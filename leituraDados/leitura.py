import pandas as pd

def leitor(csv, dataJson, cols):
    df = pd.read_csv(csv, sep=";", encoding="ISO-8859-1") 
    # dfFilter = df.query("SG_UF == 'PB'")
    # dfFilter = dfFilter[cols]
    dfFilter = df.loc[df["SG_UF"] == "PB", cols] 
    dfFilter.to_json(dataJson, orient="records", indent=4, force_ascii=False)


colunas = ["NO_REGIAO", "SG_UF", "NO_MUNICIPIO", "NO_MESORREGIAO", "NO_MICRORREGIAO", "NO_ENTIDADE", "QT_MAT_BAS", "QT_MAT_INF", "QT_MAT_FUND", "QT_MAT_MED", "QT_MAT_PROF", "QT_MAT_EJA"]
leitor("microdados_ed_basica_2023.csv", "dataBase.json", colunas)

# O QT_MAT_BAS já é a soma de todos os outros. Apenas adicionei os outros que o senhor pediu em sala.

