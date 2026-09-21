class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> vals = new HashSet<Integer>();
        for (int num: nums) {
            if (vals.contains(num)) {
                return true;
            }
            vals.add(num);
        }
        return false;
    }
}
