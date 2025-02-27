(defun binom (n k)
    (if (or (= k 0) (= k n)) 1 (+ (binom (- n 1) k) (binom (- n 1) (- k 1)))))
