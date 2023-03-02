import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):

    def test0(self):
        input = """
            printString("Hi");
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 200))

    def test1(self):
        input = """
            main: function void() {}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))

    def test2(self):
        input = """b = a + 1;"""
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
            for (i = 0, i < 4, i = i + 1) {
                row_sum: integer = row_sum(matrix, i);
                if (row_sum > largest_sum) {
                    largest_sum = row_sum;
                    largest_sum_row = i;
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 209))

    def test10(self):
        input = """
            continue;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 210))

    def test11(self):
        input = """
            IdentifierS1: integer;
            abc: float;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 211))

    def test12(self):
        input = """
            c, d, ggE: string = "David", "Monica", "_Tem";
            Arr: array [3] of string = {"Bob", "Dylan", "Garrr"};
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 212))

    def test13(self):
        input = """
            func1: function string (n: integer, b: string) {
                if (n == 0) return 1;
                else return n * 2;
            }
            main: function void () {
                delta: integer = func1(3, "abc_");
                inc(x, delta);
                inc2(x, y);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 213))

    def test14(self):
        input = """
            inc: function void (out n: integer, inherit delta: integer) {
                n = n + delta;
                return;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 214))

    def test15(self):
        input = """
            a = b - c;
            id1 = 1 + 2 * (grd * id2 + (7 - foo(4)));
            if (fosG2 % 3 == 0) {
                print("Hello");
            }
            else {return;}
            bc = 7 / (a + b);
            str1: string = "GJDS";
            str2: string;
            str3: string;
            str3 = str1::str2;
            str1 = str3::str1;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 215))

    def test16(self):
        input = """
            i = (a >= b);
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 216))

    def test17(self):
        input = """
            arr: array [4] of boolean = {true, false, true, true};
            g = arr[2, 3];
            x = x && y;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 217))

    def test18(self):
        input = """
            for (v = 100, v >= 9, v = v / 3) {
                if (v % 2 != 0) {
                    break;
                }
                continue;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 218))

    def test19(self):
        input = """
            main: function void()
            {
                preventDefault();
                readString();
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 219))

    def test20(self):
        input = """
            // Declare variables.
            x: integer = 5;
            y: integer = 3;
            z: integer;
            // Declare a function.
            myFunction: function void (a: integer, b: integer) { z = a + b; print(z);}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 220))

    def test21(self):
        input = """
            // Declare variables.
            bool_var: boolean = true;
            int_arr: array [4] of integer = {4, 3, 2, 1};
            float_var: float = 2.5;
            str: string = "Hey there!";
            for (i = 0, i < 4, i = i + 1) { int_arr[i] = int_arr[i] * 3;
            }
            if (bool_var == true) { print(str);
            }
            else { print("bool_var is false.");
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 221))

    def test22(self):
        input = """
            // Declare variables.
            a: integer = 5;
            b: integer = 10;
            // Declare a function.
            myFunction: function void (x: integer, y: integer) { if (x > y) { print("x is greater than y"); } else if (x < y) { print("x is less than y"); } else { print("x is equal to y"); }
            }
            // Call the function.
            myFunction(a, b);
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 222))

    def test23(self):
        input = """
            // Declare variables.
            a: integer = 5;
            b: integer = 10;
            // Declare a function.
            myFunction: function integer (x: integer, y: integer) { if (x > y) { return x - y; } else if (x < y) { return y - x; } else { return 0; }
            }
            // Call the function.
            c = myFunction(a, b);
            print(c);
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 223))

    def test24(self):
        input = """
            // Declare variables.
            int_arr: array [5] of integer = {1, 2, 3, 4, 5};
            bool_var: boolean = true;
            str: string = "I love Notion!";
            // Change variable values.
            int_arr[2] = int_arr[2] + 10;
            bool_var = false;
            str = "I love programming!";
            // Print variable values.
            print(int_arr);
            print(bool_var);
            print(str);
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 224))

    def test25(self):
        input = """
            // Declare variables.
            a: integer = 5;
            b: integer = 10;
            // Declare a function.
            myFunction: function void () { if (a < b) { print("a is less than b"); } else if (a > b) { print("a is greater than b"); } else { print("a is equal to b"); }
            }
            // Call the function.
            myFunction();
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 225))

    def test26(self):
        input = """
            Identifier1: integer;
            Identifier2: string = "Hello";
            Identifier3: boolean = true;
            myFunction: function void () { Identifier1 = 20; Identifier3 = false; print(Identifier2 + " World!");
            }
            // Call the function multiple times.
            myFunction();
            Identifier2 = "Goodbye";
            myFunction();
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 226))

    def test27(self):
        input = """
            // Declare variables.
            a: integer = 5;
            b: integer = 10;
            // Declare a function.
            myFunction: function integer (x: integer, y: integer) { if (x > y) { return x; } else { return y; }
            }
            // Call the function.
            c = myFunction(a, b);
            print("The larger number is " + c);
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 227))

    def test28(self):
        input = """
            // Declare variables.
            a: integer = 5;
            b: integer = 10;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 228))

    def test29(self):
        input = """
            // Declare a function.
            myFunction: function integer (a: integer, b: integer) { return a % b;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 229))

    def test30(self):
        input = """
            // Declare variables.
            int: array [5] of integer = {1, 2, 3, 4, 5};
            bool: boolean = true;
            str: string = "Hello, world!";
            // Declare a function.
            myFunction: function void () { for (i = 0, i < 5, i = i + 1) { print(int[i]); } if (bool == true) { print(str); } else { print("bool is false"); }
            }
            // Call the function.
            myFunction();
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 230))

    def test31(self):
        input = """
            // Call the function.
            c = myFunction(a, b);
            print(c);
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 231))
    
    def test32(self):
        input = """
            main: function void() {
                print("Hello, world!");
                b = c + 1;
                foo(2, 3);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 232))

    def test33(self):
        input = """xhId = !a && true;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 233))

    def test34(self):
        input = """
            if (b + c == 0) {
                y = temp % 10;
            }
            else {
                break;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 234))

    def test35(self):
        input = """
            if (a <= b + f(5))
            {
                print("SUCCESS");
            }
            if (g > cbf / 2)
            {
                printInteger(5);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 235))

    def test36(self):
        input = """
            printBoolean(abcdhFF_);
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 236))

    def test37(self):
        input = """
            do {
                x = a + b;
                s = r * r + myPI;
                a[0] = s;
            }
            while (y <= 9);
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 237))

    def test38(self):
        input = """
            bool: boolean = false;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 238))

    def test39(self):
        input = """
            {
                r, s: integer;
                r = 2.0;
                a, b: array [5] of integer;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 239))

    def test40(self):
        input = """
            foo(2 + x, 4.0 / y);
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 240))

    def test41(self):
        input = """
            IdentifierS1: integer;
            abc: float;
            gms: auto;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 241))

    def test42(self):
        input = """
            c, d, ggE: string = "Ben", "Monica", "_Tem";
            Arr: array [3] of string = {"Bob", "Dylan", "Garrr"};
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 242))

    def test43(self):
        input = """
            main: function void () {
                delta: integer = func1(3, "abc_");
                inc(x, delta);
                inc2(x, y);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 243))

    def test44(self):
        input = """
            {
                x = 2 / y;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 244))

    def test45(self):
        input = """
            a = b - c;
            id1 = 1 + 2 * (grd * id2 + (7 - foo(4)));
            if (fosG2 % 3 == 0) {
                print("Hello");
            }
            else {return;}
            bc = 7 / (a + b);
            str1: string = "GJDS";
            str3 = str1::str2;
            str1 = str3::str1;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 245))

    def test46(self):
        input = """
            do {
                // Nothing
            }
            while (false);
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 246))

    def test47(self):
        input = """
            arr: array [4] of boolean = {true, false, false, true};
            g = arr[2, 3];
            x = x && y;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 247))

    def test48(self):
        input = """
            for (v = 100, v >= 9, v = v / 3) {
                if (v % 2 != 0) {
                    break;
                }
                continue;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 248))

    def test49(self):
        input = """
            main: function void()
            {
                printInteger(inasd);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 249))

    def test50(self):
        input = """
            // Declare variables.
            x: integer = 5;
            y: integer = 3;
            z: integer;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 250))

    def test51(self):
        input = """
            test: function integer () {
                readString();
                return 3;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 251))

    def test52(self):
        input = """
            // Declare variables.
            a: integer = 5;
            b: integer = 10;
            // Declare a function.
            myFunction: function void (x: integer, y: integer) { if (x > y) { print("x is greater than y"); } else if (x < y) { print("x is less than y"); } else { print("x is equal to y"); }
            }
            // Call the function.
            myFunction(a, b);
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 252))

    def test53(self):
        input = """
            // Declare variables.
            a: integer = 5;
            b: integer = 10;
            // Declare a function.
            myFunction: function integer (x: integer, y: integer) { if (x > y) { return x - y; } else if (x < y) { return y - x; } else { return 0; }
            }
            // Call the function.
            c = myFunction(a, b);
            print(c);
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 253))

    def test54(self):
        input = """
            // Declare variables.
            str = "I love programming!";
            // Print variable values.
            print(int_arr);
            print(bool_var);
            print(str);
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 254))

    def test55(self):
        input = """
            // Declare variables.
            a: integer = 5;
            b: integer = 10;
            // Call the function.
            myFunction();
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 255))

    def test56(self):
        input = """
            Identifier1: integer;
            Identifier2: string = "REOS";
            Identifier3: boolean = false;
            myFunction: function void () { Identifier1 = 20; Identifier3 = false; print(Identifier2 + " World!");
            }
            myFunction();
            Identifier2 = "See ya";
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 256))

    def test57(self):
        input = """
            // Declare variables.
            a: integer = 5;
            // Declare a function.
            myFunction: function integer (x: integer, y: integer) { if (x > y) { return x; } else { return y; }
            }
            // Call the function.
            c = myFunction(a, b);
            print("The larger number is " + c);
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 257))

    def test58(self):
        input = """
            // Declare variables.
            a: integer = 5;
            b, c, x: string = "1", "//n", "//t//b";
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 258))

    def test59(self):
        input = """
            // Declare a function.
            myFunction: function integer (a: integer, b: integer) { return a % b;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 259))

    def test60(self):
        input = """
            // Declare variables.
            int: array [5] of integer = {1, 2, 3, 4, 5};
            // Call the function.
            myFunction();
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 260))

    def test61(self):
        input = """
            // Call the function.
            c = myFunction(a, b);
            print(c);
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 261))

    def test62(self):
        input = """
            {
                writeFloat(2.4e-16);
                bg = 9.0;
                writeFloat(bg);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 262))

    def test63(self):
        input = """
            a = b - c;
            id1 = 1 + 2 * (grd * id2 + (7 - foo(4)));
            if (fosG2 % 3 == 0) {
                print("Hello");
            }
            str3 = (str1::str2)::str1;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 263))

    def test64(self):
        input = """
            do {
                b = c * d;
            }
            while (b != c * d);
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 264))

    def test65(self):
        input = """
            do {
                x = a + b;
            }
            while (y <= 9);
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 265))

    def test66(self):
        input = """
            bool: boolean = true;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 266))

    def test67(self):
        input = """
            c, d, ggE: string = "David", "Monica", "_Tem";
            Arr: array [3] of string = {"Bob", "Dylan", "Garrr"};
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 267))

    def test68(self):
        input = """
            func1: function string (n: integer, b: string) {
                if (n == 0) return 1;
                else return n * 2;
            }
            main: function void () {
                delta: integer = func1(3, "abc_");
                inc(x, delta);
                inc2(x, y);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 268))

    def test69(self):
        input = """
            inc: function void (out n: integer, inherit delta: integer) {
                n = n + delta;
                return;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 269))

    def test70(self):
        input = """
            a = b - c;
            id1 = 1 + 2 * (grd * id2 + (7 - foo(4)));
            if (fosG2 % 3 == 0) {
                print("Hello");
            }
            else {return;}
            bc = 7 / (a + b);
            str1: string = "GJDS";
            str2: string;
            str3: string;
            str3 = str1::str2;
            str1 = str3::str1;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 270))

    def test71(self):
        input = """
            i = (a >= b);
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 216))

    def test72(self):
        input = """
            arr: array [3] of boolean = {false, true, true};
            g = arr[2, 3];
            x = x && y;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 272))

    def test73(self):
        input = """
            arr1, arr2: array [2] of integer = {1, 2}, {3, 4};
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 273))

    def test74(self):
        input = """
            // Declare variables.
            int: array [5] of integer = {1, 2, 3, 4, 5};
            bool: boolean = true;
            str: string = "Hello, world!";
            // Declare a function.
            myFunction: function void () { for (i = 0, i < 9, i = i + 1) { print(int[i]); } if (bool == true) { print(str); } else { print("bool is false"); }
            }
            // Call the function.
            myFunction();
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 274))

    def test75(self):
        input = """
            // Call the function.
            c = myFunction(a, b);
            print(c);
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 275))
    
    def test76(self):
        input = """
            main: function void() {
                print("Hello, world!");
                b = c + 1;
                foo(2, 3);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 276))

    def test77(self):
        input = """xhId = !a && true;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 277))

    def test78(self):
        input = """
            if (b + c - (foo(20) - 99) == 0) {
                y = temp % 10;
            }
            else {
                break;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 278))

    def test79(self):
        input = """
            if (a <= b + f(5))
            {
                print("SUCCESS");
            }
            if (g > cbf / 2)
            {
                printInteger(5);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 279))

    def test80(self):
        input = """
            printBoolean(abcdhFF_);
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 280))

    def test81(self):
        input = """
            do {
                x = a + b;
                a[0] = s;
            }
            while (y <= 9);
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 281))

    def test82(self):
        input = """
            bool: boolean = false;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 282))

    def test83(self):
        input = """ """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 283))

    def test84(self):
        input = """
            printBoolean(abcdhFF_ || true);
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 284))

    def test85(self):
        input = """
            do {
                x = a + b;
                s = r * r;
                a[0] = s;
            }
            while (y && ghse == false);
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 285))

    def test86(self):
        input = """
            {
                writeFloat(2.4e-16);
                bg = 9.0;
                writeFloat(bg);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 286))

    def test87(self):
        input = """
            a = b - c;
            id1 = 1 + 2 * (grd * id2 + (7 - foo(4)));
            if (fosG2 % 3 == 0) {
                print("Hello");
            }
            str3 = (str1::str2)::str1;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 287))

    def test88(self):
        input = """
            do {
                b = c * d;
            }
            while (0 <= c * d);
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 288))

    def test89(self):
        input = """
            do {
                x = a + b;
            }
            while (y <= 9);
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 289))

    def test90(self):
        input = """
            bool: boolean = true;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 290))

    def test91(self):
        input = """
            c, d, ggE: string = "David", "Monica", "_Tem";
            Arr: array [3] of string = {"Bob", "Dylan", "Garrr"};
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 291))

    def test92(self):
        input = """
            func1: function string (n: integer, b: string) {
                if (n == 0) return 1;
                else return n * 2;
            }
            main: function void () {
                delta: integer = func1(3, "abc_");
                inc(x, delta);
                inc2(x, y);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 292))

    def test93(self):
        input = """
            inc: function void (out n: integer, inherit delta: integer) {
                n = n + delta;
                return;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 293))

    def test94(self):
        input = """
            st: string;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 294))

    def test95(self):
        input = """
            max: function integer (inherit a: integer, out b: integer) {
                if (a > b) return a;
                return b;
            }
            main: function void () {
                a = readInteger();
                b = readInteger();
                ans = max(a, b);
                printInteger(ans);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 295))

    def test96(self):
        input = """
            maxlst: function integer (arr: array [5] of integer) {
                max = arr[0];
                for (i = 1, i < 5, i = i + 1) {
                    if (arr[i] > max) max = arr[i];
                }
                return max - 1;
            }
            main: function void () {
                arr: array [5] of integer = {77, 93, 23, 1, 87};
                ans = maxlst(arr);
                preventDefault();
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 296))

    def test97(self):
        input = """
            printString("What is your name?");
            name = readString();
            printString("Hello, " + name + "!");
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 297))

    def test98(self):
        input = """
            printString("Lonely, I am so lonely, I have nobody for my own.");
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 298))

    def test99(self):
        input = """
            printString("Finally, test99!!!");
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 299))