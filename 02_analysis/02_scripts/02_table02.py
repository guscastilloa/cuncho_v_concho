import pandas as pd

df = pd.read_csv("01_build/03_output/concho.csv")

freq_table = df.vote.value_counts().reset_index()

freq_table.columns = ['Respuesta', 'Frec.']

tex_file_path = '02_analysis/03_output/Tables/table02.tex'

freq_table.style.to_latex(
        tex_file_path,
        caption = 'Resultados Encuesta',
        label='tab:results_freq',
        column_format = '|c|c|',
        hrules = True
        )


