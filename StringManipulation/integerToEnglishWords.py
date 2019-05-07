def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "Zero"
        num_str_d = {
            1: 'One',
            2: 'Two',
            3: 'Three',
            4: 'Four',
            5: 'Five',
            6: 'Six',
            7: 'Seven',
            8: 'Eight',
            9: 'Nine',
            10: 'Ten',
            11: 'Eleven',
            12: 'Twelve',
            13: 'Thirteen',
            14: 'Fourteen',
            15: 'Fifteen',
            16: 'Sixteen',
            17: 'Seventeen',
            18: 'Eighteen',
            19: 'Nineteen',
            20: 'Twenty',
            30: 'Thirty',
            40: 'Forty',
            50: 'Fifty',
            60: 'Sixty',
            70: 'Seventy',
            80: 'Eighty',
            90: 'Ninety'
        }
        i = 0
        string = ""
        bucket = ['', 'Thousand ', 'Million ', 'Billion ']
        while num != 0:
            curr_num = num % 1000
            curr_str = ""
            if curr_num > 99:
                curr_str = num_str_d[curr_num / 100] + " Hundred "
                curr_num %= 100
            if 0 < curr_num < 20:
                curr_str += num_str_d[curr_num] + " "
            elif curr_num != 0:
                curr_str += num_str_d[(curr_num / 10) * 10] + " "
                curr_num %= 10
                if curr_num in num_str_d:
                    curr_str +=num_str_d[curr_num] + " "
            if bucket[i] and curr_str:
                string = curr_str + bucket[i] + string
            else:
                string = curr_str + string
            num /= 1000
            i += 1
        return string[:-1]