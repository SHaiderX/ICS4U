Verses = [ayas]
last = Sadaqallah
start = 0
end = 0
for x in Verses:
    end = end + x
    concat (range(start, end)) + (last) -> output
    start = end + 1