#Упражнение 1
def dec1(func):
    def wrapper():
        try:
            func()
        except ZeroDivisionError:
            print("Error dividing by zero")
        except StopIteration:
            print("EError: there are no more elements in the iterator")
        except ValueError:
            print("Error converting to a number")
        except EOFError:
            print("Error: function could not read what it wanted")
        except AttributeError:
            print("Error: object does not have this attribute")
        except ArithmeticError:
            print("arithmetic error")
        except ImportError:
            print("Error: Failed to import the module or its attribute")
        except LookupError:
            print("Error: invalid index or key")
        except NameError:
            print("Error: no variable with this name was found")
        except OSError:
            print("system error")
        except TypeError:
            print("Error: operation applied to object of inappropriate type")
        except SyntaxError:
            print("syntax error")
        except RuntimeError:
            print("Error!!!")
    return wrapper

#Упражнение 2
def commit_after_execute(func):
    def wrapper():
        func()
        conn.commit()
    return wrapper
