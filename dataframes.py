import marimo

__generated_with = "0.18.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return


@app.cell
def _():
    # do uv remove vega_datasets and run this cell
    from vega_datasets import data
    return (data,)


@app.cell
def _(data):
    df = data.list_datasets()
    return (df,)


@app.cell
def _(df):
    df
    return


@app.cell
def _(data):
    df = data.cars()
    return (df,)


@app.cell
def _(data):
    df_car = data.cars()
    return (df_car,)


@app.cell
def _(df_car):
    df_car
    return


@app.cell
def _(df_car):
    df_car.info()
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
