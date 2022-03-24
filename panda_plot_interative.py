#con una array de ejemplo (panda uede realizar dataframe de varios archivos de intercambio como CSV, etc) realiza un grafico intertactivo con la libreria plotly para la visualización
#comoda del usuario

import plotly.express as px
fig = px.bar(x=["a", "b", "c"], y=[1, 3, 2])
fig.write_html('first_figure.html', auto_open=True)