import matplotlib as plt
import numpy as np
import math

def solvingMono(T, l, i):
    m = 1/T
    if i == 0:
        p_serve = m/(l+m)
        p_refuse = 1-p_serve
        A = l*p_serve

        n_serve = A*60
        n_refuse = l*p_refuse*60
        relation = n_serve/n_refuse

        print("Вероятность отказа " + str(p_refuse))
        print("Вероятность обслуживания " + str(p_serve))
        print("Отношение числа обслуженных к числу необслуженных " + str(relation))
    else:
        p0 = l/m
        if p0 == 1:
            p_serve = 1/(i+2)
            p_refuse = p_serve*p0*(i+2)
            qlen = (i*(i+1))/(2*i+2)
            qtime = qlen/l
            A_rel = 1 - p_refuse
            avg_appl = 1 + qlen
            avg_time = (i+1)/(2*m)
        else:
            p_serve = (1-p0)/(1-p0**(i+2))
            p_refuse = p_serve*p0**(i+2)
            qlen = (p0**2)*((1-(p0**i)*(i-i*p0+1))/((1-p0)**2))
            qtime = qlen/l
            A_rel = 1 - p_refuse
            avg_appl = 1 + qlen
            avg_time = avg_appl/l
        print("Вероятность обслуживания " + str(p_serve))
        print("Вероятность отказа " + str(p_refuse))
        print("Cр. длина очереди " + str(qlen))
        print("Cр. время ожидания в очереди " + str(qtime))
        print("Относ. пропуск. способность " + str(A_rel))
        print("Ср. время нахождения заявки в СМО " + str(avg_appl))
        print("Ср. число заявок в СМО " + str(avg_time))

def summArr(x,n,m,a):
    S = 0
    i = 0
    while i < len(a):
        S = S + a[i]*x**(n+i*m)
        i = i + 1
    return S

# Т - время обслуживания
# l - лямбда
# n - кол-во рабочих
def solvingMulti(T, l, n, mi):
    m = 1/T
    p0 = l/m
    p0n = p0/n

    i = 0
    k=[]
    while i <= n:
        k.append(1/math.factorial(i))
        i = i + 1
    S = summArr(p0,0,1,k)
    print(S)

    if (mi != 0):
        if (p0n!=1):
            p_serve = 1/(S+(p0**(n+1))*(1-p0n**mi)/(math.factorial(n)*(n-p0)))
            print("Hi!")
        else:
            p_serve = 1/(S+(mi*p0**(n+1))/(n*math.factorial(n)))
        p_refuse = p0**(n+mi)*p_serve/(n**mi*math.factorial(n))
        avg_num = l*(1-p_refuse)/mi
        coef_occ = avg_num/n
        temp = p0**(n+1)*p_serve/(n * math.factorial(n))
        if(p0n==1):
            avg_qlen = temp*mi*(mi+1)/2
        else:
            avg_qlen = temp*(1-p0n**mi*(mi+1-mi*p0n))/(1-p0n)**2
        avg_qwait = avg_qlen/l
        avg_smo = avg_qwait+(1-p_refuse)/m
        print("Вероятность обслуживания " + str(p_serve))
        print("Вероятность отказа " + str(p_refuse))
        print("Сред. число зан. " + str(avg_num))
        print("Коэфф. занятости " + str(coef_occ))
        print("Сред. длина очереди " + str(avg_qlen))
        print("Сред. время ожид. в очереди " + str(avg_qwait))
        print("Сред. время прибыв. в СМО " + str(avg_smo))
        return
    
    if (p0n < 1):
        p_refuse = (S + p0**(n+1)/(math.factorial(n)*(n-p0)))**(-1)
        p_wait = p0**(n+1) * p_refuse/(math.factorial(n)*(n-p0))
        avg_qlen = n*p_wait/(n-p0)
        avg_qwait = avg_qlen/l
        avg_smo = avg_qwait+1/m
        avg_occupied = p0
        coef = avg_occupied/n
        avg_appl = avg_qlen+avg_occupied
        print("Вероятность обслуживания " + str(p_refuse))
        print("Вероятность ожидания " + str(p_wait))
        print("Сред. длина очереди " + str(avg_qlen))
        print("Сред. время ожид. в очереди " + str(avg_qwait))
        print("Сред. время прибыв. в СМО " + str(avg_smo))
        print("Сред. число занят. каналов " + str(avg_occupied))
        print("Коэф. занятости " + str(coef))
        print("Сред. число заявок в СМО " + str(avg_appl))
    else:
        print("Результата нет, p0/n > 1")

def main():
        print("Введите номер задачи (1...6): ")
        task = input()
        #СМО с очередью
        if task == '1':
            T = 1
            l = 0.95
            solvingMono(T,l,0)
            return
        if task == '2':
            T = 1.25
            l = 0.7
            solvingMono(T,l,3)
            return
        if task == '4':
            T = 1.2
            l = 0.5
            solvingMono(T,l,0)
            return
        #СМО многоканальные
        if task == '3':
            T = 1
            l = 0.8
            solvingMulti(T,l,3,0)
            return
        if task == '5':
            T = 3
            l = 1
            solvingMulti(T,l,3,0)
            return
        if task == '6':
            T = 2 #hours
            l = 1/3
            solvingMulti(T,l,2,5)
            return
        if task == 'exit':
            exit(0)
        else:
            print("Введите корректный номер задачи")
        
while True:
    main()