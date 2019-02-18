# -*- coding: utf-8 -*-
# <nbformat>4</nbformat>

# <markdowncell>

# # Building a portfolio with data from disk
#
# ## Building a portfolio with `build_portfolio()` with data obtained from data files.
#
# Note: The stock data is provided in two data files. The stock data was previously pulled from quandl.

# <codecell>

import pathlib
import pandas as pd
import datetime
# importing FinQuant's function to automatically build the portfolio
from finquant.portfolio import build_portfolio

# <markdowncell>

# ### Get data from disk/file
# Here we use `pandas.read_cvs()` method to read in the data.

# <codecell>

# stock data was previously pulled from quandl and stored in ex1-stockdata.csv
# commands used to save data:
# pf.getPortfolio().to_csv("ex1-portfolio.csv", encoding='utf-8', index=False, header=True)
# pf.getPfStockData().to_csv("ex1-stockdata.csv", encoding='utf-8', index=True, index_label="Date")
# read data from files:
df_pf_path = pathlib.Path.cwd() / ".." / "data" / "ex1-portfolio.csv"
df_data_path = pathlib.Path.cwd() / ".." / "data" / "ex1-stockdata.csv"
df_pf = pd.read_csv(df_pf_path)
df_data = pd.read_csv(df_data_path, index_col="Date", parse_dates=True)

# <markdowncell>

# ### Examining the DataFrames

# <codecell>

df_pf

# <codecell>

df_data.head(3)

# <markdowncell>

# ## Building a portfolio with `build_portfolio()`
# `build_portfolio()` is an interface that can be used in different ways. Two of which is shown below. For more information the docstring is shown below as well.
#
# In this example `build_portfolio()` is being passed `df_data`, which was read in from file above.

# <codecell>

print(build_portfolio.__doc__)

# <markdowncell>

# ## Building a portfolio with data only
# Below is an example of only passing a `DataFrame` containing data (e.g. stock prices) to `build_portfolio()` in order to build an instance of `Portfolio`. In this case, the allocation of stocks is automatically generated by equally distributing the weights across all stocks.

# <codecell>

# building a portfolio by providing stock data
pf = build_portfolio(data=df_data)

# <markdowncell>

# ### Portfolio is successfully built
# Below it is shown how the allocation of the stocks and the data (e.g. prices) of the stocks can be obtained from the object `pf`.

# <codecell>

# the portfolio information DataFrame
print(pf.portfolio.name)
pf.portfolio

# <codecell>

# the portfolio stock data, prices DataFrame
pf.data.head(3)

# <markdowncell>

# ## Building a portfolio with data and desired allocation
# If a specific allocation of stocks in the portfolio is desired, a `DataFrame` such as `df_pf` (which was read from file above) can be passed to `build_portfolio()` as shown below.

# <codecell>

# building a portfolio by providing stock data
# and a desired allocation
pf2 = build_portfolio(data=df_data, pf_allocation=df_pf)

# <codecell>

# the portfolio information DataFrame
print(pf2.portfolio.name)
pf2.portfolio

# <codecell>

# the portfolio stock data, prices DataFrame
pf2.data.head(3)
