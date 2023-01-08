  ;; Print statement
  (print "Hello world")
  (println "Hello world")

  ;; Variables & Lexical Scoping
    ;; Let
    (let [conf "Kanchilugers"
        cloj "clojure"]
        (println (str "Hello to all " conf))
        (println (str "Say Howdy to " cloj))
        (let [conf "Linux"]
          (print conf))
        )

    ;; Def
    (def conf "KanchiLug")
    

    ;; Atoms
    (def atom-conf (atom "Some Linux Meetup"))
    (deref atom-conf)
    @atom-conf
    (reset! atom-conf "KanchiLug Meetup")
  
  ;; Format String

    (def conf "KanchiLug")
    (format "Hello there, %s" conf)

    ;; Other way to achieve
    (print (str "Hello there " conf))

  ;; DataType and DataStructure

    ;; Boolean
    (boolean false)

    ;; Integer
    (+ 4 3 67 67)
    (/ 4 3)
    (quot 4 3)
    (mod 4 3)

    ;; String
    (str "Good " "Evening")

    ;; List
    (list 1 2 3)
    (nth '(1 2 3) 1)
    (count `(1 2 3))

    ;; Vector
    [1 2 3]

    ;; Set
    #{1 2 3}
    (conj #{1 2 3} 2)

    ;; Map
    (def sample-map {:Apple "Paper" :Linux "Rock" :Microsoft "Scissor"})
    sample-map
    (get sample-map :Linux)
    (assoc {:Apple "Paper" :Linux "Rock" :Microsoft "Scissor"} :Some "Nope")

  ;; Conditional Statement

    ;; If
    (if false
        (println "This is always printed")
        (println "This is never printed"))

    (if true
      (do
        (println "This is always printed")
        (println "This is never printed")))

    ;; When
    (when true
         (println "Hello")
         (println "Hello2"))

    ;; Conditional
    (def n 15)
    (cond
        (and (= (mod n 3) 0) (= (mod n 5) 0)) "fizzbuzz"
        (= (mod n 3) 0) "fizz"
        (= (mod n 5) 0) "buzz"
        :else "Nope")

  ;; Functions

    (defn greet-hello [name]
      (println (str "Vanakam " name)))

    (defn
      greet-hello
      "Intha Function summa vanakam sollum"
      [name]
      (println (str "Vanakam " name)))

    (greet-hello "Kanchilug")

    (doc greet-hello)

    ;; Tail call recursion
    (defn count-down [result n]
        (if (= n 0)
          result
          (recur (conj result n) (dec n))))

    (count-down [] 5)

  ;; Loop
    (loop [x 10]
        (when (> x 1)
            (println x)
            (recur (- x 2))))

    (dotimes [n 5] (println "n is" n))

    (for [x [0 1 2 3 4 5]
      :let [y (* x 3)]
      :when (even? y)]
      (println y)
      )
    
  ;; Macro
    (conj (conj (conj [] 1) 2) 3)

    ;; Thread First
    (-> []
        (conj 1)
        (conj 2)
        (conj 3))

    ;; Thread Last - | linux
    (->> ["KanchiLug" "Linuxers"]
        (map clojure.string/upper-case)
        (map #(str "Hello " %))) 

  ;; Higer Order Function

    ;; Filter
    (filter even? (range 10))

    ;; Map
    (map inc [1 2 3 4 5])

    ;; Reduce
    (reduce + [1 2 3 4 5])
    (reduce + 10 [1 2 3 4 5])

