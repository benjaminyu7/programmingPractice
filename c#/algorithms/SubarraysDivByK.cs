public class Solution {
    public int SubarraysDivByK(int[] nums, int k) {
        Dictionary<int, int> modCount = new Dictionary<int, int>();
        modCount[0] = 1;
        int sumMod = 0;
        for (int i = 0; i < nums.Length; i++)
        {
            int mod = nums[i] % k;
            sumMod = (sumMod + mod) % k;
            if(sumMod < 0) sumMod += k;
            if(modCount.ContainsKey(sumMod))
            {
                modCount[sumMod]++;
            }
            else
            {
                modCount[sumMod] = 1;
            }
        }
        int divByK=0;
        foreach(var entry in modCount)
        {
            // Sum of series of incrementing numbers
            divByK += ((entry.Value - 1)* (entry.Value)/2);
        }
        return divByK;
    }
}