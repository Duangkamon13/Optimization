def cam_expos(neutral, chosen):
    apertures = ['f/1.4', 'f/2', 'f/2.8', 'f/4', 'f/5.6', 'f/8', 'f/11', 'f/16', 'f/22']
    shutters = ['1/4', '1/8', '1/15', '1/30', '1/60', '1/125', '1/250', '1/500', '1/1000', '1/2000', '1/4000']
    isos = ['100', '200', '400', '800', '1600', '3200']
    
    diff_aperture = apertures.index(neutral[0]) - apertures.index(chosen[0])  
    diff_shutter = shutters.index(neutral[1]) - shutters.index(chosen[1])    
    diff_iso = isos.index(chosen[2]) - isos.index(neutral[2])                 
    total = diff_aperture + diff_shutter + diff_iso
    return (diff_aperture, diff_shutter, diff_iso, total)

if __name__ == '__main__':
    res = cam_expos(['f/2.8', '1/500', '400'], ['f/5.6', '1/125', '200'])
    print(res)  
    res = cam_expos(['f/2.8', '1/500', '400'], ['f/1.4', '1/60', '100'])
    print(res)
