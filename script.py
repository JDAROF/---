money=int(input('Введите сумму'))
per_cent={'ТКБ':5.6,'СКВ':5.9,'ВТБ':4.28,'СБЕР':4.0}
ТКБ=int((per_cent['ТКБ'])*(money/100))
СКВ=int((per_cent['СКВ'])*(money/100))
ВТБ=int((per_cent['ВТБ'])*(money/100))
СБЕР=int((per_cent['СБЕР'])*(money/100))
deposit=[ТКБ,СКВ,ВТБ,СБЕР]
print(deposit)
i=max(iter(per_cent))
print(i)