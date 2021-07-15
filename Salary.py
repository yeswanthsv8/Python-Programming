wag=int(input())
day=int(input())
bas=wag*day

hra=bas*0.10
da=bas*0.05
pf=bas*0.12
np=bas+hra+da-pf
print('BasicPay:%d HRA:%.2f DA:%.2f PF:%.2f NetPay:%.2f'%(bas,hra,da,pf,np))
