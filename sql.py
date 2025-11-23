import marimo

__generated_with = "0.18.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""
    ## Using SQL
    marimo lets you mix and match Python and SQL: Use SQL to query Python dataframes (or databases like SQLite and Postgres), and get the query result back as a Python dataframe.
    """)
    return


@app.cell
def _():
    import pandas as pd
    import random

    df = pd.DataFrame(
        {
            "category": [random.choice(["A", "B", "C"]) for _ in range(20)],
            "value": list(range(20)),
        }
    )
    return (df,)


@app.cell
def _(df):
    df
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Now how to query using SQL ??
    """)
    return


@app.cell
def _(df, mo):
    _df = mo.sql(
        f"""
        SELECT category, MEAN(value) as mean FROM df GROUP BY category ORDER BY mean;
        """
    )
    return


@app.cell
def _(df, mo):
    _df = mo.sql(
        f"""
        SELECT category, MEAN(value) as mean FROM df GROUP BY category ORDER BY mean;
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Show the connection to custom database via "+" from DB icon
    """)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
