class Solution {
public:
    int maxLength(vector<int>& ribbons, int k)
    {
        std::sort(ribbons.begin(), ribbons.end());

        int vecSize = ribbons.size();

        int low = 1;
        int high = ribbons[vecSize - 1];
        int maxLengthOfRibbon = 0;
        while (low <= high)
        {
            int mid = low + (high - low + 1) / 2;
            int numRibbons = 0;
            for (int i = vecSize - 1; i >= 0; --i)
            {
                numRibbons += ribbons[i] / mid;
                if (numRibbons >= k)
                {
                    maxLengthOfRibbon = mid;
                    low = mid + 1;
                    break;
                }
            }
            if (numRibbons < k) high = mid - 1;
        }

        return maxLengthOfRibbon;
    }
};
