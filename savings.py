def ruin_save():
    with open('ruin/amount.txt', 'r') as am:
        return 'ruin/' + str(int(am.readlines()[-1])) + '.jpg'


def ruin_send():
    with open('ruin/amount.txt', 'r') as am:
        return 'ruin/' + 'result' + str(int(am.readlines()[-1])) + '.jpg'


def segm_save():
    with open('segm/amount.txt', 'r') as am:
        return 'segm/' + str(int(am.readlines()[-1])) + '.jpg'


def segm_send():
    with open('segm/amount.txt', 'r') as am:
            a = str(int(am.readlines()[-1]))
            return 'runs/detect/exp' + a + '/' + a + '.jpg' 


def segm_sended():
    with open('segm/amount.txt', 'r') as am:
            a = str(int(am.readlines()[-2]))
            return 'runs/detect/exp' + a + '/' + a + '.jpg' 


def ruin_sended():
    with open('ruin/amount.txt', 'r') as am:
        return 'ruin/' + 'result' + str(int(am.readlines()[-2])) + '.jpg'