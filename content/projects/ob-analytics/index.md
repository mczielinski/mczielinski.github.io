+++
author = "Mark Zielinski"
title = "ob-analytics — limit order book analytics in Python"
date = "2024-08-17"
description = "Reconstruct trades, classify orders, and visualize market microstructure from raw exchange events — a Python port of the R obAnalytics CRAN package, on PyPI."
tags = ["python", "quant", "market-microstructure", "order-book", "visualization", "open-source"]
[cover]
  image = "cover.png"
  alt = "ob-analytics price-levels visualization of a reconstructed limit order book"
  caption = "Price-level view of a reconstructed limit order book, rendered by ob-analytics."
  relative = true
  hidden = false
  hiddenInList = false
  hiddenInSingle = false
+++

**Limit order book analytics and visualization for Python.** Reconstruct trades
from raw exchange events, classify order types, compute depth metrics, and
visualize market microstructure — from Bitstamp-style CSVs or
[LOBSTER](https://lobsterdata.com/) message and order-book files.

It's a standalone port of the R
[obAnalytics](https://cran.r-project.org/package=obAnalytics) CRAN package, with
a pipeline API, pluggable data formats, flow-toxicity metrics, and both
Matplotlib and Plotly backends.

[**View on GitHub&nbsp;→**](https://github.com/mczielinski/ob-analytics) ·
[**Documentation&nbsp;→**](https://mczielinski.github.io/ob-analytics/) ·
[**PyPI&nbsp;→**](https://pypi.org/project/ob-analytics/)

```bash
pip install ob-analytics
```
