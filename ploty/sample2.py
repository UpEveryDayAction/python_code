import pandas as pd
import numpy as np
import plotly.express as px

df = pd.DataFrame(np.arange(12).reshape(3, 4))
fig = px.scatter(df)
# fig = px.scatter(x=[0, 1, 2, 3, 4], y=[0, 1, 4, 9, 16])
fig.show()