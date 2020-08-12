text_file = open("Output.csv", "w+")
text_file.writelines('IMSI;ISDN;NRBT;NRBTIndex;ALSNRBTIndex;ARBT\n')
with open('sample.txt') as f_in:
  for line in f_in:
    if '+++    USCDB' in line:
      line = f_in.readline().strip()
      while 'There is together 1 report' not in line:
        variable = line[:line.find('=')-1]
        # get imsi
        if variable == 'IMSI':
          IMSI = line[line.find('=')+2:]
        if variable == 'ISDN':
          ISDN = line[line.find('=')+2:]
        if variable == 'NRBT':
          NRBT = line[line.find('=')+2:]
        if variable == 'NRBTIndex':
          NRBTIndex = line[line.find('=')+2:]
        if variable == 'ALSNRBTIndex':
          ALSNRBTIndex = line[line.find('=')+2:]
        if variable == 'ARBT':
          ARBT = line[line.find('=')+2:]
        line = f_in.readline().strip()
      text_file.writelines(IMSI +';' + ISDN + ';' + NRBT + ';' + NRBTIndex + ';' + ALSNRBTIndex +';' + ARBT +'\n')