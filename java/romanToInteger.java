import java.util.HashMap;

class Solution {
    public int romanToInt(String s) {
        int value = 0;
        //make hashmap of values 
        HashMap<Character,Integer> roman= new HashMap<Character,Integer>();
        roman.put('I',1);
        roman.put('V',5);
        roman.put('X',10);
        roman.put('L',50);
        roman.put('C', 100);
        roman.put('D', 500);
        roman.put('M', 1000);
        //iterate through the values of the string
        int x = 0;
        while(x<s.length()-1) {
	    char nextLetter = s.charAt(x+1);
            switch (s.charAt(x)) {
                case 'I':
                    if (nextLetter == 'V' ||nextLetter == 'X') {
                        value -= roman.get(s.charAt(x));
                        x++;
                    } 
                    break;
                case 'X':
                    if (nextLetter == 'L' || nextLetter == 'C') {
                        value -= roman.get(s.charAt(x));
                        x++;
                    } 
                    break;
                case 'C':
                    if (nextLetter == 'D' || nextLetter == 'M') {
                        value -= roman.get(s.charAt(x));
                        x++;
                    }
                    break;
            }
            value += roman.get(s.charAt(x));
            x++;
        }
        //add up the values
	if(x < s.length())
        value += roman.get(s.charAt(x));
        return value;
    }
}

class romanToInteger {
	public static void main (String [] args) {
		System.out.println("helloWorld");
		Solution s = new Solution();
		System.out.println(s.romanToInt("V"));
		System.out.println(s.romanToInt("IV"));
		System.out.println(s.romanToInt("XVIV"));
	}
}
