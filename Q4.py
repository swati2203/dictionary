Dic={
    1:"Navgurukul",
    2:"in",
    3:{'A':'Welcome',
    'B':'To',
    'c':'dharamshala'
    }
}
for i,j in Dic.items():
    if type(j)==dict:
        for x in Dic[j].keys():
            if x=='A':
                Dic[j].pop('A')
                print(x)
