class Solution:
    def mediana(self, v, pv, uv):
        n = uv - pv + 1
        m = (uv + pv) // 2
        if n % 2 == 0:
            return (v[m] + v[m + 1]) / 2
        else:
            return v[m]

    def calculMediana(self, pa, ua, pb, ub, a, b, r):
        print(pa, ua, pb, ub)
        n = ua - pa + 1
        m = (pb + ub) // 2
        #calcul direct pentru n=1,2- in functie de pozitia lui a[pa] in b fata de mediana
        if n == 0:
            return self.mediana(b, pb, ub)
        if n == 1:
            if r == 1:
                if a[pa] <= b[m]:
                    return b[m]
                elif b[m] <= a[pa] <= b[m + 1]:
                    return a[pa]
                else:
                    return min(b[m + 1], a[pa])
            else:
                if pb == ub:
                    return (a[pa] + b[pb]) / 2.0
                v = [a[pa], b[m], b[m + 1], b[m - 1]]
                return (sum(v) - min(v) - max(v)) / 2.0
        if n == 2:
            if r == 1:
                if a[pa] <= b[m] <= a[ua]:
                    return b[m]
                elif a[ua] <= b[m]:
                    return max(b[m - 1], a[ua])
                else:
                    return min(b[m + 1], a[pa])
            else:
                if a[ua] <= b[m]:
                    if m > 0:
                        return (max(b[m - 1], a[ua]) + b[m]) / 2.0
                    else:
                        return (a[ua] + b[m]) / 2.0
                elif a[pa] >= b[m + 1]:
                    if m + 2 <= ub:
                        return (b[m + 1] + min(b[m + 2], a[pa])) / 2.0
                    else:
                        return (a[pa] + b[m + 1]) / 2.0
                else:
                    return (max(a[pa], b[m]) + min(a[ua], b[m + 1])) / 2.0

        m1 = self.mediana(a, pa, ua)
        m2 = self.mediana(b, pb, ub)

        if m1 == m2:
            return m1
        if m1 > m2: #renuntam la acelasi numar de elemente
            return self.calculMediana(pa, pa + n // 2, pb + (n - 1) // 2, ub, a, b, r)
        else:
            return self.calculMediana(pa + (n - 1) // 2, ua, pb, ub - (n - 1) // 2, a, b, r)

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a = nums1
        b = nums2
        n = len(a)
        m = len(b)
        if n > m:
            a, b = b, a
            n, m = m, n
        return self.calculMediana(0, n - 1, 0, m - 1, a, b, (m + n) % 2)
