text_file = open("Output-eps.csv", "w+")
text_file.writelines('IMSI;ISDN;CardType;T-CSI;EPS-CNTXID1;EPS-CNTXID2;EPS-CNTXID3;EPS-CNTXID4;EPS-CNTXID5;EPS-CNTXID6\n')
with open('sample-eps.txt') as f_in:
  for line in f_in:
    if line == '':
      line = f_in.readline().strip()
    elif '+++    USCDB' in line:
      line = f_in.readline().strip()
      while 'There is together 1 report' not in line:
        variable = line[:line.find('=')-1]
        # get imsi
        if variable == 'IMSI':
          IMSI = line[line.find('=')+2:]
        elif variable == 'ISDN':
          ISDN = line[line.find('=')+2:]
        elif variable == 'CardType':
          CardType = line[line.find('=')+2:]
        elif 'T-CSI' in line:
          line = f_in.readline().strip()
          line = f_in.readline().strip()
          TCSI = line[line.find('=')+2:]
        elif 'EPS Data' in line:
          EPS_CNTXID1 = 'NONE'
          EPS_CNTXID2 = 'NONE'
          EPS_CNTXID3 = 'NONE'
          EPS_CNTXID4 = 'NONE'
          EPS_CNTXID5 = 'NONE'
          EPS_CNTXID6 = 'NONE'
          counterAPN  = 1
          while 'SMS INAP Service' not in line:
            if 'CNTXID' in line:
              if counterAPN == 1:
                EPS_CNTXID1 = line[line.find('=')+2:]
              elif counterAPN == 2:
                EPS_CNTXID2 = line[line.find('=') + 2:]
              elif counterAPN == 3:
                EPS_CNTXID3 = line[line.find('=') + 2:]
              elif counterAPN == 4:
                EPS_CNTXID4 = line[line.find('=') + 2:]
              elif counterAPN == 5:
                EPS_CNTXID5 = line[line.find('=') + 2:]
              elif counterAPN == 6:
                EPS_CNTXID6 = line[line.find('=') + 2:]
              counterAPN = counterAPN + 1
            line = f_in.readline().strip()
        line = f_in.readline().strip()
      text_file.writelines(IMSI +';' + ISDN + ';' + CardType + ';' + TCSI + ';' + EPS_CNTXID1 + ';' + EPS_CNTXID2 + ';' + EPS_CNTXID3 +
                           ';' + EPS_CNTXID4 +';' + EPS_CNTXID5 +';' + EPS_CNTXID6 + '\n')