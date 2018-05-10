import Data.List

toHist = map (length . filter (/=' ')) . filter (not . all (==' ')) . transpose . lines

solve xs = sum $ map (max 0 . uncurry (-)) $ zip ys xs
    where ys = zipWith min (scanl max 0 xs) (scanr max 0 xs)

main = getContents >>= print . solve . toHist
