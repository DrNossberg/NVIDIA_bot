#!/usr/bin/env python
# -*- coding: utf-8 -*-

class PCcomponents(object):
    """docstring for PCcomponents"""
    def __init__(self,Card_list, manufacturer):
        super(PCcomponents, self).__init__()
        PCC_URL ='https://www.pccomponentes.com/tarjetas-graficas/geforce-rtx-{GPU}-series'
        for FE in Card_list:
            FE.add_url(PCC_URL.replace("{GPU}", FE.name))
        self.brand_list = manufacturer

    def search_GPU(self):
        for FE in Card_list:
            if FE.get_status(LDLC_FE_link) != 0 :
                ping_FE_page(FE)

        PrixMax=900
            EnStock=Espagnol3080(lienes,PrixMax)
            if len(EnStock)>0:
                if len(StockEspagnol3080)==0:
                    StockEspagnol3080=[EnStock[0]]
                    alert(['y a du stock de 3080 sur componentes!!',str(EnStock[0])+' '+str(EnStock[1])+' '+str(EnStock[2])])
                # AFinir=1
            else:
                if len(StockEspagnol3080)>0:
                    alert(['Fin du stock pour ',str(StockEspagnol3070[0])])
                    StockEspagnol3080=[]
            sleep(5)
            lienes='https://www.pccomponentes.com/tarjetas-graficas/geforce-rtx-3060-series'
            PrixMax=500
            EnStock=Espagnol3080(lienes,PrixMax)
            if len(EnStock)>0:
                if len(StockEspagnol3060)==0:
                    print(EnStock)
                    StockEspagnol3060=[EnStock[0]]
                    alert(['y a du stock de 3060 sur componentes!!',str(EnStock[0])+' '+str(EnStock[1])+' '+str(EnStock[2])])
            else:
                if len(StockEspagnol3060)>0:
                    alert(['Fin du stock pour ',str(StockEspagnol3060[0])])
                    StockEspagnol3060=[]
            sleep(5)
            lienes='https://www.pccomponentes.com/tarjetas-graficas/geforce-rtx-3070-series'
            PrixMax=700
            EnStock=Espagnol3080(lienes,PrixMax)
            if len(EnStock)>0:
                if len(StockEspagnol3070)==0:
                    StockEspagnol3070=[EnStock[0]]
                    alert(['y a du stock de 3070 sur componentes!!',str(EnStock[0])+' '+str(EnStock[1])+' '+str(EnStock[2])])
                # AFinir=1
            else:
                if len(StockEspagnol3070)>0:
                    alert(['Fin du stock pour ',str(StockEspagnol3070[0])])
                    StockEspagnol3070=[]
            # if AFinir==1:
            #     alert(['Le bot a bien travailler',' et se déconnecte à présent'])
            #     break


def scrap_search_gpu(self, FE):
    LaBase='https://www.pccomponentes.com'
    r = requests.get(lienes)
    print(r)
    EnStock=[]
    if '200' in str(r):
        soup = BeautifulSoup(r.content,'html.parser')
        Search=soup.findAll('div', id='articleListContent')
        Search2=Search[0].findAll('a', {'class':'GTM-productClick enlace-superpuesto cy-product-hover-link'})
        for GPU in Search2:
            Stock=GPU['data-stock-web']
            if Stock!='4' and Stock !='9999':
                NomDeLaCarte=str(GPU['data-name'])
                Prix=float(GPU['data-price'])
                print(Prix)
                LienHyperText=LaBase+str(GPU['href'])
                if 'Reacondicionado' in NomDeLaCarte:
                    pass
                else:
                    if Prix<PrixMax:
                        # r2 = requests.get(LienHyperText,timeout=(3.05, 27))
                        # soup2 = BeautifulSoup(r2.content,'html.parser')
                        # Search33=soup2.findAll('button', id='notify-me')
                        # Search38=soup2.findAll('div', {'class':'ficha-producto__acciones white-card-movil hidden-sm-down'})
                        # print(Search38)
                        # if len(Search33)==0:
                        print(NomDeLaCarte,Prix,LienHyperText)
                        EnStock=[NomDeLaCarte,Prix,LienHyperText]
                        # else:
                        #     print('pas de comprar')
                        #     print(NomDeLaCarte,Prix,LienHyperText)

    return EnStock