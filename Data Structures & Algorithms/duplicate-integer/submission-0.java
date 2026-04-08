class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> set = new HashSet<Integer>();

        for(int index : nums){

            if(set.contains(index)){
                return true;
               
            } set.add(index);
           
        } return false;
    }
}