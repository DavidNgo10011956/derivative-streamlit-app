import streamlit as st
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Derivative Analyser", layout="wide")

st.title("Derivative Analyser for Students")

x = sp.symbols("x")

func_str = st.text_input(
    "Enter f(x):",
    value="x**4*(x**2 + 8*x - 10)"
)

order = st.slider("Derivative order", 1, 5, 2)
xmin = st.number_input("x min", value=-6.0)
xmax = st.number_input("x max", value=6.0)

if st.button("Analyse"):
    try:
        expr = sp.sympify(func_str, locals={"x": x})
        derivatives = [sp.diff(expr, x, i) for i in range(1, order + 1)]

        st.subheader("Derivative Results")
        st.write("f(x) =", expr)

        for i, d in enumerate(derivatives, start=1):
            st.write(f"Derivative {i}:", sp.expand(d))

        f = sp.lambdify(x, expr, "numpy")
        xs = np.linspace(xmin, xmax, 1000)
        ys = f(xs)

        fig, ax = plt.subplots(figsize=(10, 5))
        ax.plot(xs, ys, label="f(x)")
        ax.axhline(0, linestyle="--")
        ax.axvline(0, linestyle="--")
        ax.grid(True)
        ax.legend()

        st.pyplot(fig)

    except Exception as e:
        st.error(f"Input error: {e}")