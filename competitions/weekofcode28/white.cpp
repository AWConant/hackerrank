#include <iostream>
#include <unordered_map>
#include <cmath>
#include <utility>
#include <iomanip>

using namespace std;

struct SHash {
    size_t operator()(const pair<int, int>& p) const {
        return p.first ^ p.second;
    }
};

unordered_map< pair<int,int>, double, SHash > dp;

int reverse(int b, int n) {
    int sum = 0;
    for (int i = 0; i < n; i++) {
        if ((b >> i) & 1) {
            sum += (1 << (n-1-i));
        }
    }
    return sum;
}

int get_bit(int b, int i) {
    return (b >> i) & 1;
}

int remove_bit(int x, int n, int i) {
    int mask = (int)pow(2, (i+1)) - 1;
    int bits = x & ~mask;
    x &= ~(1<<i);
    x &= ~(1<<n-1);
    return (bits >> 1) | (x & mask);
}

double white(int b, int n, int k) {
    pair<int,int> args(b, k);
    unordered_map< pair<int,int>, double, SHash>::iterator it = dp.find(args);
    if (it != dp.end()) {
        return (*it).second;
    }

    double ev;
    if (k == 1) { 
        int summ = 0;
        int lo = 0; int hi = n - 1;
        while (lo <= hi) {
            if (get_bit(b, lo) || get_bit(b, hi)) {
                summ += lo == hi ? 1 : 2;
            } 
            lo++; hi--;
        }
        ev = (double)summ/n;
    } else {
        ev = 0.0;
        int lo = 0; int hi = n - 1;
        while (lo <= hi) {
            double lo_ev = white(remove_bit(b, n, lo), n-1, k-1);
            if (get_bit(b, lo) == 1) lo_ev += 1;
            if (lo == hi) {
                ev += lo_ev;
            } else {
                double hi_ev = white(remove_bit(b, n, hi), n-1, k-1);
                if (get_bit(b, hi) == 1) hi_ev += 1;
                ev += 2*(lo_ev > hi_ev ? lo_ev : hi_ev);
            }
            lo++; hi--;
        }
        ev = ev/(double)n;
    }

    dp[args] = ev;
    dp[make_pair(reverse(b, n), k)] = ev;
    return ev;
}

int main() {
    int n,k;
    cin >> n >> k;
    char c;
    int b;
    cin.get(c);
    for (int i = 0; i < n; i++) {
        cin.get(c);
        if (c == 'W') {
            b |= (int)pow(2, i);
        }
    }
    
    double ans = white(b, n, k);
    cout << fixed << showpoint << setprecision(10) << ans << endl;
}
