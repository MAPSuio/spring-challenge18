import Control.Monad (join)

main = print $ (!!10000) $ concatMap (join replicate) [1..]
