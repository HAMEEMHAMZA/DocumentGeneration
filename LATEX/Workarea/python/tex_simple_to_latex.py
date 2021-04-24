 
document_name = ''

#do not change - header
out1 =''

out1+= str( r" \documentclass[11pt]{article} " )
out1+= str(" \n ")
out1+= str(  r" \usepackage[margin=1in]{geometry} " )
out1+= str(" \n ")
out1+= str( r" \usepackage{amsfonts,amsmath,amssymb} " )
out1+= str(" \n ")
out1+= str( r" \usepackage[none]{hyphenat} " )
out1+= str(" \n ")
out1+= str( r" \usepackage{fancyhdr} " )
out1+= str(" \n ")
out1+= str( r" %\usepackage{xcolor} " )
out1+= str(" \n ")
out1+= str( r" \usepackage[dvipsnames]{xcolor} " )
out1+= str(" \n ")
out1+= str( r" \usepackage{array} " )
out1+= str(" \n ")
out1+= str( r" \newcolumntype{L}{>{\centering \arraybackslash}m{6cm}} " )
out1+= str(" \n ")

out1+= str( r" \begin{document} " )
out1+= str(" \n ")
out1+= str( r" \begin{titlepage} " )
out1+= str(" \n ")
out1+= str( r" \begin{center} " )
out1+= str(" \n ")
out1+= str( r" \vspace*{10cm} " )
out1+= str(" \n ")

out1 += str(r" \huge \textbf{ " )
out1 += str(r"introduction 123" )
out1 += str(" } \\ " )

print(out1)