(ns dots.core
  (:require [quil.core :as q]
            [quil.middleware :as m]))

(defn setup []
  (q/frame-rate 30)
  (q/color-mode :hsb)
  :vertical)

(defn update-state [state]
  ({:vertical :horizontal :horizontal :vertical} state))

(defn draw-state [state]
  (q/background 255)
  (let [myrand #(+ 50 (rand-int 400))
        xs (loop [xs (vec (sort [(myrand) (myrand) (myrand)]))]
             (if (< (Math/abs (- (quot (+ (xs 0) (xs 2)) 2) (xs 1))) 20)
               (recur (vec (sort [(myrand) (myrand) (myrand)])))
               xs))
        [x1 x3] ((juxt min max) (myrand) (myrand))
        x2 (+ x1 25 (rand-int (- x3 25)))
        xs [x1 x2 x3]
        ys [(myrand) (myrand)]
        ys (conj ys (/ (+ (first ys) (second ys)) 2))]
    (dotimes [i 3]
      (q/no-stroke)
      (q/fill (rand-int 255) (rand-int 255) (rand-int 255))
      (case state
        :vertical (q/ellipse (xs i) (ys i) 25 25)
        :horizontal (q/ellipse (ys i) (xs i) 25 25))))
  ;; swap verticals with horizontals when generating horizontals
  (q/save-frame (str (name state) "/####.png"))
  (when (= (q/frame-count) 18)
    (q/no-loop)))

(defn -main [& args]
  (q/defsketch dots
    :title "dots"
    :size [500 500]
    :update update-state
    :draw draw-state
    :setup setup
    :features [:keep-on-top]
    :middleware [m/fun-mode]))
