#coding=gbk
import cv2
import numpy as np
import sys
cn_character_gray = [u'畾',u'晶',u'唱',u'昌',u'田',u'曰',u'口',u'二',u'一']
if __name__ == '__main__':
    imname = 'Lenna.jpg'
    title = 'Lenna'
    if len(sys.argv)>1:
        imname = sys.argv[1]
        title = imname.split('.')[0]
    gray = cv2.imread(imname,0)
    print gray.shape
    txt_np = np.zeros(gray.shape,dtype=unicode)#
    
    
    print txt_np.shape
    step = int(255/len(cn_character_gray))
    for i in range(len(cn_character_gray)):
        if i == len(cn_character_gray) - 1:
            txt_np[(gray>=step*i)] = cn_character_gray[i]
        else:
            txt_np[(gray>=step*i) & (gray<step*(i+1))] = cn_character_gray[i]
    
    

   
    with open("%s.txt"%title,"w") as f:
        for i in txt_np:
            for j in i:
                j=j.encode('utf-8')
                f.write(j)
            f.write('\r\n')
