import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test1(self):
        input = """
            main: function void() {}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))

    def test2(self):
        input = """a + 1;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 202))

    def test3(self):
        input = """
            if (true) {
                y = temp % 10;
            }
            else {
                continue;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 203))

    def test4(self):
        input = """
            if (a <= b + f(5))
            {
                print("SUCCESS");
            }
            else break;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 204))

    def test5(self):
        input = """
            for (i = 0, i < 20, i = i + 1) {
                fib_nums[i] = fibonacci(i);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 205))

    def test6(self):
        input = """
            while (x <= 5) {
                x = x + 1;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 206))

    def test7(self):
        input = """
            do {
                x = a + b;
            }
            while (y <= 9);
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 207))

    def test8(self):
        input = """
            bool: boolean = true;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 208))

    def test9(self):
        input = """
            // Declare and initialize variables.
            int: array [5] of integer = {1, 2, 3, 4, 5};
            int2: integer = 10;
            bool: boolean = true;
            amon: string = "Hello World";

            fib_nums: array [20] of integer;
            for (i = 0, i < 20, i = i + 1) {
                fib_nums[i] = fibonacci(i);
            }

            matrix: array [4, 4] of integer = {
                {1, 2, 3, 4},
                {5, 6, 7, 8},
                {9, 10, 11, 12},
                {13, 14, 15, 16}
            };

            // Find the largest Fibonacci number.
            largest_fib: integer = find_largest(fib_nums);

            // Find the row with the largest sum in the matrix.
            largest_sum: integer = 0;
            largest_sum_row: integer = -1;
            for (i = 0, i < 4, i = i + 1) {
                row_sum: integer = row_sum(matrix, i);
                if (row_sum > largest_sum) {
                    largest_sum = row_sum;
                    largest_sum_row = i;
                }
            }

            // Output the results.
            printf("int: %d\n", int[0]);
            printf("int2: %d\n", int2);
            printf("bool: %s\n", bool ? "true" : "false");
            printf("string: %s\n", string);
            printf("The largest Fibonacci number is %d.\n", largest_fib);
            printf("The row with the largest sum in the matrix is row %d, with a sum of %d.\n", largest_sum_row, largest_sum);
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 209))

    def test10(self):
        input = """
            continue;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 210))