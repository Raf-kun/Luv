from loguru import logger
from parser import Parser

def main():
    # https://www.52shuku.vip/yanqing/am/h2QX.html
    logger.add('file.log',
               format='{time:YYYY-MN-DO at HH:mm:ss} | {level} | {messeage}',
               rotation='3 days',
               backtrace=True,
               diagnose=True)


    title = input("Введите название новеллы: ")
    url = input("Введите ссылку: ")
    pars = Parser(title, url)
    print(pars.get_novel())


if __name__ == '__main__':
    main()
