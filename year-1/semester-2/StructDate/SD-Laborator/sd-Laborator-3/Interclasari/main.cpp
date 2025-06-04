#include <iostream>
#include <fstream>

using namespace std;

const int NMAX = 20;
int a[21][1000001], p[NMAX + 1];
int sz;

struct Heap {
	int val, sir;
};
Heap H[NMAX + 1];

int parent(int pos) {
	return pos / 2;
}

int left_son(int pos) {
	return 2 * pos;
}

int right_son(int pos) {
	return 2 * pos + 1;
}

void up(int pos) {
	while(pos > 1 && H[pos].val < H[parent(pos)].val) {
		swap(H[pos], H[parent(pos)]);
		pos = parent(pos);
	}
}

void down(int pos) {
	while(1) {
		//daca nu are fiu stanga atunci nu mai putem sa coboram
		if(left_son(pos) > sz) {
			break;
		}
		int next_pos = left_son(pos);
		if(right_son(pos) <= sz && H[right_son(pos)].val < H[next_pos].val) {
			next_pos = right_son(pos);
		}
		if(H[pos].val < H[next_pos].val) {
			break;
		} else {
			swap(H[pos], H[next_pos]);
			pos = next_pos;
		}

	}
}

void sterge_radacina() {
	swap(H[1], H[sz]);
	sz--;
	down(1);
}

void inserare(int x, int s) {
	sz++;
	H[sz].val = x;
	H[sz].sir = s;
	up(sz);
}

int minim() {
	return H[1].val;
}

int main() {
	ifstream f("interclasari.in");
	ofstream g("interclasari.out");
	int k;
	f >> k;
	int nr = 0;
	for(int i = 1; i <= k; i++) {
		f >> a[i][0];
		nr += a[i][0];
		for(int j = 1; j <= a[i][0]; j++) {
			f >> a[i][j];
		}
	}
	for(int i = 1; i <= k; i++) {
		if(a[i][0] > 0) {
			inserare(a[i][1], i);
			p[i] = 1;
		}
		
	}
	g << nr << '\n';
	for(int i = 1; i <= nr; i++) {
		g << minim() << ' ';
		int s = H[1].sir;
		sterge_radacina();
		p[s]++;
		if(p[s] <= a[s][0]) {
			inserare(a[s][p[s]], s);
		}
	}
	return 0;
}