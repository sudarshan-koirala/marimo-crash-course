# Copyright 2024 Marimo. All rights reserved.

import marimo

__generated_with = "0.18.0"
app = marimo.App()


@app.cell(hide_code=True)
def firstcell():
    import marimo as mo

    mo.md("# Welcome to marimo! 🌊🍃")
    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""
    ## Some examples about markdown
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    # Hello
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    # Hello
    """)
    return


@app.cell
def _(mo):
    text_input = "Sudarshan"
    mo.md(f"My name is: {text_input}")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Slider example
    """)
    return


@app.cell
def _(mo):
    slider = mo.ui.slider(1, 22)
    return (slider,)


@app.cell
def _(mo, slider):
    mo.md(f"""
    marimo is a **reactive** Python notebook.

    This means that unlike traditional notebooks, marimo notebooks **run
    automatically** when you modify them or
    interact with UI elements, like this slider: {slider}.

    {"##" + "🍃" * slider.value}
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "Tip: disabling automatic execution": mo.md(
                rf"""
            marimo lets you disable automatic execution: in the notebook
            footer, change "On Cell Change" to "lazy".

            When the runtime is lazy, after running a cell, marimo marks its
            descendants as stale instead of automatically running them. The
            lazy runtime puts you in control over when cells are run, while
            still giving guarantees about the notebook state.
            """
            )
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        Tip: This is a tutorial notebook. You can create your own notebooks
        by entering `marimo edit` at the command line.
        """
    ).callout()
    return


@app.cell
def _(mo):
    mo.md(text="This is warning").callout(kind="danger")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## 1. Reactive execution

    A marimo notebook is made up of small blocks of Python code called
    cells.

    marimo reads your cells and models the dependencies among them: whenever
    a cell that defines a global variable  is run, marimo
    **automatically runs** all cells that reference that variable.

    Reactivity keeps your program state and outputs in sync with your code,
    making for a dynamic programming environment that prevents bugs before they
    happen.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    **Global names must be unique.** To enable reactivity, marimo imposes a
    constraint on how names appear in cells: no two cells may define the same
    variable.
    """)
    return


@app.cell
def _():
    a = 10
    return (a,)


@app.cell
def _():
    b = 200
    return (b,)


@app.cell
def _(a, b):
    a + b 
    return


@app.cell
def _():
    a = 3
    return (a,)


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "Tip: private variables": (
                """
                Variables prefixed with an underscore are "private" to a cell, so
                they can be defined by multiple cells.
                """
            )
        }
    )
    return


@app.cell
def _():
    _a = 5
    return


@app.cell
def _():
    _a = 40
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 2. Lazy mode
    """)
    return


@app.cell
def _():
    y = 36
    return (y,)


@app.cell
def _():
    z = 20
    return (z,)


@app.cell
def _(y, z):
    y + z
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## 3. UI elements

    Cells can output interactive UI elements. Interacting with a UI
    element **automatically triggers notebook execution**: when
    you interact with a UI element, its value is sent back to Python, and
    every cell that references that element is re-run.

    marimo provides a library of UI elements to choose from under
    `marimo.ui`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## 4. The `marimo` command-line tool

    **Creating and editing notebooks.** Use

    ```
    marimo edit
    ```

    in a terminal to start the marimo notebook server. From here
    you can create a new notebook or edit existing ones.


    **Running as apps.** Use

    ```
    marimo run notebook.py
    ```

    to start a webserver that serves your notebook as an app in read-only mode,
    with code cells hidden.

    **Convert a Jupyter notebook.** Convert a Jupyter notebook to a marimo
    notebook using `marimo convert`:

    ```
    marimo convert your_notebook.ipynb > your_app.py
    ```

    **Tutorials.** marimo comes packaged with tutorials:

    - `dataflow`: more on marimo's automatic execution
    - `ui`: how to use UI elements
    - `markdown`: how to write markdown, with interpolated values and
       LaTeX
    - `plots`: how plotting works in marimo
    - `sql`: how to use SQL
    - `layout`: layout elements in marimo
    - `fileformat`: how marimo's file format works
    - `markdown-format`: for using `.md` files in marimo
    - `for-jupyter-users`: if you are coming from Jupyter

    Start a tutorial with `marimo tutorial`; for example,

    ```
    marimo tutorial dataflow
    ```

    In addition to tutorials, we have examples in our
    [our GitHub repo](https://www.github.com/marimo-team/marimo/tree/main/examples).
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    **🌊 Some UI elements.** Try interacting with the below elements.
    """)
    return


@app.cell
def _(mo):
    icon = mo.ui.dropdown(["🍃", "🌊", "✨"], value="🍃")
    return (icon,)


@app.cell
def _(icon, mo):
    repetitions = mo.ui.slider(1, 16, label=f"number of {icon.value}: ")
    return (repetitions,)


@app.cell
def _(icon, repetitions):
    icon, repetitions
    return


@app.cell
def _(icon, mo, repetitions):
    mo.md("# " + icon.value * repetitions.value)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## 5. Running notebooks as apps

    marimo notebooks can double as apps. Click the app window icon in the
    bottom-right to see this notebook in "app view."

    Serve a notebook as an app with `marimo run` at the command-line.
    Of course, you can use marimo just to level-up your
    notebooking, without ever making apps.
    """)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
