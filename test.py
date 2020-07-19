def pow(x, y):
  if not (y == 0):
    return (x * pow(x, y - 1))
  return 1

print(pow(2,3))

(define pow (lambda (x y) (cond ((not y 0) (* x (pow x (- y 1)))) (t (1))))) 


