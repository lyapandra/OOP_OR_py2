#https://pythonworld.ru/tipy-dannyx-v-python/isklyucheniya-v-python-konstrukciya-try-except-dlya-obrabotki-isklyuchenij.html
def func(a, b):
    try:
        c = a / b
    # except Exception:
    #except ArithmeticError:
    except ZeroDivisionError:
        print 'ERROR'
func (10, 1)
