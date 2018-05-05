(ns dots.core
  (:require [quil.core :as q]
            [quil.middleware :as m]))

(defn setup []
  (q/frame-rate 30)
  (q/color-mode :hsb))

(defn draw-state [state]
  (q/background 255)
  (let [myrand #(+ 50 (rand-int 400))
        xs [(myrand) (myrand) (myrand)]
        ys [(myrand) (myrand)]
        ys (conj ys (/ (+ (first ys) (second ys)) 2))]
    (dotimes [i 3]
      (q/no-stroke)
      (q/fill (rand-int 255) (rand-int 255) (rand-int 255))
      ;; Swap xs and ys to generate horizontals
      (q/ellipse (xs i) (ys i) 25 25)))
  ;; swap verticals with horizontals when generating horizontals
  (q/save-frame "verticals/####.png")
  (when (= (q/frame-count) 100)
    (q/no-loop)))

(defn -main [& args]
  (q/defsketch dots
    :title "dots"
    :size [500 500]
    :draw draw-state
    :setup setup
    :features [:keep-on-top]
    :middleware [m/fun-mode]))
