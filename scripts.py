# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "marimo",
#     "pandas==2.3.3",
# ]
# ///

import marimo

__generated_with = "0.18.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import pandas as pd
    print("hello from vim!")
    print("hi")
    return


@app.cell
def _():
    print('hello world!!')
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
