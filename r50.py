def parse_string(s):
 tag_list = []
 l = []
 f = False
 r = []

 for i in list(s):
  if f:
   l.append(i)
   if i == ">":
    r.append("".join(l))
    l = []
    f = False
  else:
   if i == "<":
    l.append(i)
    f = True
 return r


def check_tags(tags):
 for i in tags:
  if len(i.split("<")) != 2 or len(i.split(">")) != 2:
   print("Bad tag:",i)

#получаем имя тега, без < > или </ >
def tag_name(t):
 if t.startswith("</"):
  return t[2:-1]
 else:
  return t[1:-1]


def check_syntax(tags):
 r = [] #стек

 for i in tags:
  n = tag_name(i)
  
  #если тег закрывающий и ему есть соответсвующий в стеке, удаляем, если нету то ошибка синтаксиса
  if i.startswith("</"):
   if not n in r:
    print("Bad syntax",i)
    return
   r.remove(n)

  #если тег открывающий то заносим в стек
  else:
   r.append(n)

 #проверяем стек, в нём не должно быть тегов
 if len(r) != 0:
  print("Bad closer tags for",r)
 else:
  print("Syntax good!")



s = "<t1> <t2></t2></t1>"
#s = "<t1> <t2></t2></t3>"
#s = "<t1> <t2></t2>"

#парсим только теги, пропускаем текст и тд
tag = parse_string(s)

#проверяем теги на наличие лишних символов
check_tags(tag)

#проверяем синтаксис
check_syntax(tag)

