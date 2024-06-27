import pandas as pd

df = pd.read_csv("01_build/03_output/concho.csv")
df.from_cali = df.from_cali.replace({0:"No", 1:"Sí"})

t = pd.crosstab(df.from_cali, df.vote, margins = True)

tex_file_path = '02_analysis/03_output/Tables/table01.tex'

t.style.to_latex(
        tex_file_path,
        caption = '¿Cuncho o concho?',
        label='tab:crosstab1',
        column_format = '|c|c|c|c|',
        hrules = True
        )

