class Solution {
    public boolean isAnagram(String s, String t) {
        HashMap<Character, Integer> see1 = new HashMap<Character, Integer>();
        HashMap<Character, Integer> see2 = new HashMap<Character, Integer>();

        if(s.length() != t.length()){return false;}


        for(int i = 0; i< s.length(); i++){

            see1.put(s.charAt(i), see1.getOrDefault(s.charAt(i), 0)+ 1);
            see2.put(t.charAt(i), see2.getOrDefault(t.charAt(i), 0)+ 1);


        }
        if(see1.equals(see2)){
            return true;
        }
return false;
    }
}
