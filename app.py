import logging
logging.basicConfig(filename='login.log',level=logging.DEBUG,format='%(asctime)s %(levelname)s %(message)s')

def fibo(n):
    if n<0:
        logging.error(f'N is negative. please enter positive value of n')
        return
    
    logging.info(f"running fibonacci till {n} nos")
    a=0
    b=1
    logging.debug(f'assigning a=0 and b=1')
    for i in range(2,n):
        c=a+b
        logging.debug(f'for i = {i} , fibo={c}')
        a=b
        b=c
    return c
    
print(fibo(10))