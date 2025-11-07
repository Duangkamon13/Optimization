"""
Given a flow chart below 
(simplified from: https://www.radcliffecardiology.com/image-gallery/figure-1-flow-chart-suggested-strategies-coronary-artery-disease-management), 
write a program to suggest the Transcatheter Aortic Valve Implantation (TAVI) management strategy 
for Coronary Artery Disease (CAD).
"""

obstructive = input('Is CAD obstructive (yes/no)? ')

if obstructive.casefold()== "no" :
    print('Non-obstructive CAD.')
    print('TAVI alone.')
elif obstructive.casefold()=="yes":
    print('Obstructive CAD.')
    risk_area = input('Is area of myocardium at risk large (yes/no)? ')
    if risk_area.casefold()== "no":
        print('Small area of myocardium at risk.')
        print('Consider TAVI first, then ischemia-driven revascularization.')
    elif risk_area.casefold()== "yes" :
        print('Large area of myocardium at risk.')
        CS = float(input('How is coronary stenosis (%)? '))
        if CS > 75:
            print('Severe CAD.')
            print('Staged upfront or concomitant PCI and TAVI.')
        elif CS <= 75 :
            print('Moderate CAD.')
            print('Consider TAVI first, then CAD functional assessment.')

