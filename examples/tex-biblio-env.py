#!/usr/bin/env python
"""
Pandoc filter to place an environment around the outside 
of a pandoc-generated bibliography listing. That is when 
using 'pandoc -f markdown -t latex' without the 
--biblatex or --natbib options (these delegate the biblio
to latex itself).
"""

from pandocfilters import toJSONFilter, Div, RawBlock
import sys

def latex(x):
    return RawBlock('latex', x)

def biblio_env(key, value, fmt, meta):
	if key == 'Div':
		[[ident, classes, keyvals], contents] = value
		if ident == 'refs':
			if fmt == 'latex':
				label = '\\label{' + ident + '}'
				return([latex('\\begin{citeproc}' + label)] + contents +
                       [latex('\\end{citeproc}')])


if __name__ == "__main__":
    toJSONFilter(biblio_env)
