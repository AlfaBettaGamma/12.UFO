def UFO(N, data, octal):
  n = 0
  f = 0
  st = []
  fst = []
  if N != len(data):
    return 'Неверно введенные данные!'
  if octal == True:
    for i in range(N):
      n = data[i]
      n = str(n)
      st = list(n)
      st.reverse()
      f = 0
      for j in range(len(st)):
        if st[j] != 8 or st[j] != 9:
          f = f + int(st[j])*8**j
      fst.append(f)
      st.clear()
    return fst
  else:
    for i in range(N):
      n = data[i]
      n = str(n)
      st = list(n)
      st.reverse()
      f = 0
      for j in range(len(st)):
        f = f + int(st[j])*16**j
      fst.append(f)
      st.clear()
    return fst


print(UFO(2,[1234,1877],True))