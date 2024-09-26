#im
import os
import shutil
maindir = os.listdir('120img/')
try:
    os.mkdir('coco/')
except:
    pass
try:
    os.mkdir('coco/images/')
except:
    pass
try:
    os.mkdir('coco/labels/')
except:
    pass
try:
    os.mkdir('coco/images/Train/')
except:
    pass
try:
    os.mkdir('coco/images/Valid/')
except:
    pass
try:
    os.mkdir('coco/labels/Train/')
except:
    pass
try:
    os.mkdir('coco/labels/Valid/')
except:
    pass
j = 0
for i in maindir:
    OriginalName = os.path.splitext(i)[0]
    print(OriginalName)
    extensionsss = os.path.splitext(i)[1]
    print(extensionsss)
    if(extensionsss == '.jpg' or extensionsss == '.png' or extensionsss == '.PNG' or extensionsss == '.jpeg' ):
        print(OriginalName+extensionsss)
        try:
            if(j%5):
                shutil.copy2(f'120img/{OriginalName+extensionsss}',f'coco/images/Train/{OriginalName+extensionsss}')
                shutil.copy2(f'120img/{OriginalName}.txt',f'coco/labels/Train/{OriginalName}.txt')
            else:
                shutil.copy2(f'120img/{OriginalName+extensionsss}',f'coco/images/Valid/{OriginalName+extensionsss}')
                shutil.copy2(f'120img/{OriginalName}.txt',f'coco/labels/Valid/{OriginalName}.txt')
        except Exception as e:
            print(e)
            pass
    else:
        pass

    j+=1
