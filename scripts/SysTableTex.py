
def tablefragment(m,table,signalRegions,skiplist,chanStr,showPercent):
  tableline = ''

  tableline += '''
\\begin{table}
\\begin{center}
\\setlength{\\tabcolsep}{0.0pc}
\\begin{tabular*}{\\textwidth}{@{\\extracolsep{\\fill}}l'''

  for region in signalRegions:
    tableline += "c"   
  tableline += '''}
\\noalign{\\smallskip}\\hline\\noalign{\\smallskip}
{\\bf %s channel}                                   ''' % (table)

  reg0=signalRegions[0].replace("_meff","").replace("_cuts","").replace("_disc","")
  for region in signalRegions:
    tmp=region.replace("_meff","").replace("_cuts","").replace("_disc","")
    if tmp==reg0:
      tmp += " (tot)"
    else:
      tmp = tmp.replace(reg0+"_","")
      pass
    tableline += " & " + tmp + "           "   

  tableline += ''' \\\\
\\noalign{\\smallskip}\\hline\\noalign{\\smallskip}
%%'''

  tableline += '''
Total statistical $(\\sqrt{N_{\\rm exp}})$             '''
  for region in signalRegions:
    tableline += " & $\\pm " + str(("%.2f" %m[region]['sqrtnfitted'])) + "$       "
  tableline += '''\\\\
%%'''

  tableline += '''
Total background systematic              '''

  for region in signalRegions:
    tableline += " & $\\pm " + str(("%.2f" %m[region]['totsyserr'])) + "$       "

  tableline += '''      \\\\
\\noalign{\\smallskip}\\hline\\noalign{\\smallskip}
\\noalign{\\smallskip}\\hline\\noalign{\\smallskip}
%%''' 



  doAsym=False
  m_listofkeys = m[signalRegions[0]].keys()
  m_listofkeys.sort()
  for name in m_listofkeys:
    if name not in skiplist:
      if name.startswith("syserr_gamma_") and not (reg0+"_" in name):
        continue
      
      printname = name
      printname = printname.replace('syserr_','')
      printname = printname.replace('_','\_')
      for index,region in enumerate(signalRegions):
        if index == 0:
          tableline += "\n" + printname + "      "
          
        if not showPercent:
          tableline += "   & $\\pm " + str(("%.2f" %m[region][name])) + "$       "
        else:
          percentage = m[region][name]/m[region]['totsyserr'] * 100.0
          if percentage <1:
            tableline += "   & $\\pm " + str(("%.2f" %m[region][name])) + " [" + str(("%.2f" %percentage)) + "\\%] $       "
          else:
            tableline += "   & $\\pm " + str(("%.2f" %m[region][name])) + " [" + str(("%.1f" %percentage)) + "\\%] $       "
                    
          
        if index == len(signalRegions)-1:
          tableline += '''\\\\
%%'''


  tableline += '''
\\noalign{\\smallskip}\\hline\\noalign{\\smallskip}
\\end{tabular*}
\\end{center}
\\caption[Breakdown of uncertainty on background estimates]{
Breakdown of the dominant systematic uncertainties on background estimates in the various signal regions.
Note that the individual uncertainties can be correlated, and do not necessarily add up quadratically to 
the total background uncertainty.
\\label{table.results.bkgestimate.uncertainties.%s}}
\\end{table}
%%''' % (chanStr) 
    
  return tableline

