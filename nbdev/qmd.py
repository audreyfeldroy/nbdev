# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/api/15_qmd.ipynb.

# %% ../nbs/api/15_qmd.ipynb 2
from __future__ import annotations
import sys,os,inspect

from fastcore.utils import *
from fastcore.meta import delegates

# %% auto 0
__all__ = ['meta', 'div', 'img', 'btn', 'tbl_row', 'tbl_sep']

# %% ../nbs/api/15_qmd.ipynb 4
def meta(md,  # Markdown to add meta to
         classes=None,  # List of CSS classes to add
         style=None,  # Dict of CSS styles to add
         **kwargs):   # Additional attributes to add to meta
    "A metadata section for qmd div in `{}`"
    if style: kwargs['style'] = "; ".join(f'{k}: {v}' for k,v in style.items())
    props = ' '.join(f'{k}="{v}"' for k,v in kwargs.items())
    classes = ' '.join('.'+c for c in L(classes))
    meta = []
    if classes: meta.append(classes)
    if props: meta.append(props)
    meta = ' '.join(meta)
    return md + ("{" + meta + "}" if meta else "")

# %% ../nbs/api/15_qmd.ipynb 5
def div(txt,  # Markdown to add meta to
        classes=None,  # List of CSS classes to add
        style=None,  # Dict of CSS styles to add
        **kwargs):
    "A qmd div with optional metadata section"
    return meta("::: ", classes=classes, style=style, **kwargs) + f"\n\n{txt}\n\n:::\n\n"

# %% ../nbs/api/15_qmd.ipynb 6
def img(fname,  # Image to link to
        classes=None,  # List of CSS classes to add
        style=None,   # Dict of CSS styles to add
        height=None,  # Height attribute
        relative=None,  # Tuple of (position,px)
        link=False,   # Hyperlink to this image
        **kwargs):
    "A qmd image"
    kwargs,style = kwargs or {}, style or {}
    if height: kwargs["height"]= f"{height}px"
    if relative:
        pos,px = relative
        style["position"] = "relative"
        style[pos] = f"{px}px"
    res = meta(f'![]({fname})', classes=classes, style=style, **kwargs)
    return  f'[{res}]({fname})' if link else res

# %% ../nbs/api/15_qmd.ipynb 7
def btn(txt, # Button text
        link,  # Button link URL
        classes=None,  # List of CSS classes to add
        style=None,    # Dict of CSS styles to add
        **kwargs):
    "A qmd button"
    return meta(f'[{txt}]({link})', classes=classes, style=style, role="button")

# %% ../nbs/api/15_qmd.ipynb 8
def tbl_row(cols:list,  # Auto-stringified columns to show in the row
           ):
    "Create a markdown table row from `cols`"
    return '|' + '|'.join(str(c or '') for c in cols) + '|'

# %% ../nbs/api/15_qmd.ipynb 9
def tbl_sep(sizes:int|list=3  # List of column sizes, or single `int` if all sizes the same
           ):
    "Create a markdown table separator with relative column size `sizes`"
    if isinstance(sizes,int): sizes = [3]*sizes
    return tbl_row('-'*s for s in sizes)

# %% ../nbs/api/15_qmd.ipynb 10
def _install_nbdev():
    return div('''#### pip

```sh
pip install -U nbdev
```

#### conda

```sh
conda install -c fastai nbdev
```
''', ['panel-tabset'])
