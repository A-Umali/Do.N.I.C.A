

con = 0
cur = 0
modules = {}
def insert_words(con, cur, name, words, priority):
    # If words is a lsit
    if isinstance(words, type([])):
        function_name = name + ' ' + 'handle'
        try:
            cur.execute("INSERT INTO functions (function, priority) "
                        + "values ('{fn}',{p})"
                        .format(fn=function_name,p=priority))
        except IndexError:
            print("Error")