(ns miu.core
  (:require [clojure.string :as s]
            [clojure.set :refer [difference intersection]]))

(defn indices-of
  ([s v] (indices-of s v 0 []))
  ([s v i res]
   (if-let [j (s/index-of s v i)]
     (recur s v (+ j 1) (conj res j))
     res)))

(defn all-replacements [s v r]
  (mapv #(str (subs s 0 %) r (subs s (+ % (count v)))) (indices-of s v)))

(defn axiom1 [x]
  (if (s/ends-with? x "I") (str x "U") []))

(defn axiom2 [x]
  (str (subs x 0 1) (subs x 1) (subs x 1)))

(defn axiom3 [x]
  (all-replacements x "III" "U"))

(defn axiom4 [x]
  (all-replacements x "UU" ""))

(def apply-axioms
  (comp flatten (juxt axiom1 axiom2 axiom3 axiom4)))

(def miu-tree
  (iterate
   (->> (juxt axiom1 axiom2 axiom3 axiom4)
        (partial map)
        (comp set flatten))
   #{"MI"}))

(defn solve [ys]
  (let [tree (iterate
              (->> (juxt axiom1 axiom2 axiom3 axiom4)
                   (partial map)
                   (comp set flatten))
              #{"MI"})]
    (reduce
     (fn [[depth ys sum] level]
       (if (empty? ys)
         (reduced sum)
         (let [common (intersection ys level)]
           (prn "remaining "(count ys))
           [(inc depth)
            (difference ys common)
            (->> (count common) (* depth) (+ sum))])))
     [0 (set ys) 0] miu-tree)))

(defn solve-file [fname]
  (->> (slurp fname) s/split-lines solve))

(defn generate-testcases [n d]
  (let [tests (atom #{})
        tree (iterate
              (->> (juxt axiom1 axiom2 axiom3 axiom4)
                   (partial map)
                   (comp flatten))
              '("MI"))]
    (while (< (count @tests) n)
      (->> (rand-int d) (nth tree) (rand-nth)
           (swap! tests conj)))
    (->> @tests sort)))

(defn generate-test-file
  ([] (generate-test-file "mius" 100 9))
  ([fname] (generate-test-file fname 100 9))
  ([fname n] (generate-test-file fname n 9))
  ([fname n d]
   (->> (generate-testcases n d)
        (s/join "\n")
        (spit fname))))
