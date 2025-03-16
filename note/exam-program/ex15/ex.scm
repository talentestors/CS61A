;;; non-empty subsets of integer list s that have an even sum
(define (even-subsets s)
  (if (null? s)
    nil
    (append (even-subsets (cdr s))
      (subset-helper even? s))))

;;; non-empty subsets of integer list s that have an odd sum
(define (odd-subsets s)
  (if (null? s)
    nil
    (append (odd-subsets (cdr s))
      (subset-helper odd? s))))

(define (subset-helper f s)
  (append 
    (map (lambda (t)
           (cons (car s) t))
      (if (odd? (car s))
        (even-subsets (cdr s))
        (odd-subsets (cdr s))))
    (if (odd? (car s))
      (list (list (car s)))
      nil)))
