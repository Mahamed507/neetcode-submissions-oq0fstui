class Solution {
    public boolean hasDuplicate(int[] nums) {

        HashMap<Integer,Integer>map = new HashMap<Integer, Integer>();

        for(int k : nums){

            if(map.containsKey(k) && map.get(k) >=1){
                return true;
            }
            map.put(k , map.getOrDefault(k , 0) + 1);
        }

        return false;
        
    }
}