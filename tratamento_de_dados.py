import csv
import re

ceps = {}
bairros = {}


with open("src/bairros_ceps.csv","r") as arquivo:
    arquivo_csv = csv.reader(arquivo, delimiter=',')
    for i, linha in enumerate(arquivo_csv):
        if i == 0:
            print(str(linha))
        else:
            txt_full = str(linha)
            cep = ''
            bairro = ''
            cep_regex = re.findall('[0-9]',txt_full)
            bairro_regex = re.findall('[a-z /A-Z]',txt_full)
        
            if(len(cep_regex) == 12):
                cep = cep_regex[4:]
                ceps[i] = cep
                bairros[i] = bairro_regex
            else:
                cep = cep_regex[3:]
                ceps[i] = cep
                bairros[i] = bairro_regex

new_cep = ''
new_bairro = ''
cep_list = []
bairro_list = []

for cep in ceps:
    x = new_cep.join(ceps[cep])
    cep_list.append(x.strip())

for bairro in bairros:
    x = new_bairro.join(bairros[bairro])
    bairro_list.append(x)

cep_list = list(set(cep_list))
bairro_list = list(set(bairro_list))

def append_no_txt():
    for cep in cep_list:
        f = open('bairros_ceps.txt','a')
        f.write('{}\n'.format(cep))
        f.close()

    for bairro in bairro_list:
        f = open('bairros_ceps.txt','a')
        f.write('{}\n'.format(bairro))
        f.close()

if __name__ == '__main__':
    append_no_txt()