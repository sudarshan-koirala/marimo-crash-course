import marimo

__generated_with = "0.18.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import asyncio
    return asyncio, mo


@app.cell
def _(mo):
    rerun = mo.ui.button(label="Rerun")
    rerun
    return (rerun,)


@app.cell
async def _(asyncio, mo, rerun):
    rerun
    for _ in mo.status.progress_bar(
        range(10),
        title="Loading",
        subtitle="Please wait",
        show_eta=True,
        show_rate=True,
    ):
        await asyncio.sleep(0.5)
    return


@app.cell
def _(mo):
    rerun_slow = mo.ui.button(label="Rerun Slow")
    rerun_slow
    return (rerun_slow,)


@app.cell
async def _(asyncio, mo, rerun_slow):
    rerun_slow
    for _ in mo.status.progress_bar(
        range(2), title="Loading", subtitle="Please wait", show_eta=True, show_rate=True
    ):
        await asyncio.sleep(12)
    return


@app.cell
def _():
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Progress bar one more example
    """)
    return


@app.cell
def _():
    return


@app.cell
def _():
    #import marimo as mo ( if it is already imported once, it will throw error 🔥)
    import pandas as pd
    import time
    return pd, time


@app.cell
def _(pd):
    df = pd.DataFrame(
            {
                "id": range(1, 11),
                "value": [x * 10 for x in range(1, 11)],
            }
        )
    df  # show the dataframe
    return (df,)


@app.cell
def _(df, mo, time):
    # Process dataframe rows with a progress bar
    results = []

    # df.iterrows() is an iterator, so pass total=len(df)
    for idx, row in mo.status.progress_bar(
        df.iterrows(),
        title="Processing dataframe",
        subtitle="Computing squares",
        total=len(df),           # important for iterators like iterrows()
        show_eta=True,
        show_rate=True,
    ):
        # Simulate a slow operation per row
        time.sleep(0.3)

        # Example "loading/processing" logic
        processed = {
            "id": row["id"],
            "value": row["value"],
            "value_sq": row["value"] ** 2,
        }
        results.append(processed)

    results  # displayed after loop finishes
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
