class Solution {
    public boolean isAnagram(String s, String t) {

        // check the length 
        if(s.length() != t.length()){
            return false;
        }

        // create hashMap
        HashMap<Character, Integer> map1 = new HashMap<Character, Integer>();
         HashMap<Character, Integer> map2 = new HashMap<Character, Integer>();

         // iterate through the strings of each Chararcter

         for(int i = 0; i<s.length(); i++){
            // add it inside the hashMap, and keep track how many character in the value(keep default to 0).
            map1.put(s.charAt(i), map1.getOrDefault(s.charAt(i), 0) + 1);
            map2.put(t.charAt(i), map2.getOrDefault(t.charAt(i), 0) + 1);

         }// check to see if it is equals 
         return map1.equals(map2);


    }
}
