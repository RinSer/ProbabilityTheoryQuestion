#!/usr/bin/env python

# Finds the number of positive integer triples which sum equals 10
# and the number of such combinations containing 4

three_sum_to_ten = 0;
containing_four = 0;
for x in range(1, 10):
    for y in range(1, 10):
        for z in range(1, 10):
           if (x + y + z) == 10:
               three_sum_to_ten += 1
               if x == 4 or y == 4 or z == 4:
                   containing_four += 1
                   print('contains 4! \#' + str(containing_four))
               print(str(x) + ' + ' + str(y) + ' + ' + str(z) + ' \#' + str(three_sum_to_ten))

print(str(containing_four) + '/' + str(three_sum_to_ten))
