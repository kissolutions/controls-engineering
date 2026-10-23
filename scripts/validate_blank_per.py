#!/usr/bin/env python3
"""Check that a published PER is a BLANK initialization template (not a project archive)."""
import re,sys
from pathlib import Path
from openpyxl import load_workbook
DATA={'DASHBOARD':3,'SCOPE DASHBOARD':5,'WP PROGRESS':2,'BLOCKED ITEMS REPORT':5,'SCOPES':5,'WORK PACKAGES':2,'RFI LEGACY':3,'SYSTEM MODEL':5,'RFI REGISTER':5,'ISSUES':5,'PUNCH LIST':3,'SOURCES':5,'RECORDS':5,'LINKS':5,'CHANGE LOG':5,'BASELINES':5,'INTAKE QUEUE':5}
TEST={'REGISTRY GUIDE','SB1 FORMULA TESTS','SB2 CHECKS'}
LEAK=re.compile(r'https?://(?:drive|docs)\.google\.com/|file:///|\\\\[^\\]',re.I)
def seed(s,c):
    if s=='RFI LEGACY':return (c.column in (18,19,20) and c.value==1) or (c.coordinate=='B3' and c.value==1)
    if s=='PUNCH LIST':return (c.column in (20,21,22) and c.value==1) or (c.column==17 and c.value=='Open') or (c.coordinate=='B3' and c.value==1)
    return False
def validate(path):
    w=load_workbook(path);issues=[];fcount=0
    for name in (set(DATA)|TEST)-set(w.sheetnames):issues.append('Missing sheet '+name)
    if w._external_links:issues.append('External workbook links remain')
    for s in w:
        for row in s:
            for c in row:
                if c.value is None:continue
                if c.data_type=='f':
                    fcount+=1
                    if '#REF!' in c.value:issues.append(s.title+'!'+c.coordinate+' broken formula')
                    continue
                if s.title in DATA and c.row>=DATA[s.title] and not seed(s.title,c):issues.append(s.title+'!'+c.coordinate+' contains nonformula data')
                if LEAK.search(str(c.value)) or c.hyperlink:issues.append(s.title+'!'+c.coordinate+' private link')
                if c.comment and s.title in DATA:issues.append(s.title+'!'+c.coordinate+' comment')
    if w.properties.lastModifiedBy not in (None,'KIS Solutions'):issues.append('Personal author metadata')
    if fcount<10000:issues.append('Unexpected formula loss '+str(fcount))
    if w['DASHBOARD']['U2'].value!='Engineering Scope / Scope of Work':issues.append('Dashboard v1.2 layout mismatch')
    print(('FAIL' if issues else 'PASS'),Path(path).name, fcount,'formulas')
    for s in issues[:30]:print(' -',s)
    if len(issues)>30:print(' - and',len(issues)-30,'more')
    return int(bool(issues))
if __name__=='__main__':
    if len(sys.argv)!=2:sys.exit('Usage: validate_blank_per.py PATH.xlsx')
    sys.exit(validate(sys.argv[1]))
